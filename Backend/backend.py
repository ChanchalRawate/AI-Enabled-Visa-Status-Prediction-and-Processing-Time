from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import pickle
from xgboost import XGBRegressor

app = Flask(__name__)
CORS(app)

# ================= LOAD MODEL =================
model = XGBRegressor()
model.load_model("xgb_model.json")

# ================= LOAD FILES =================
columns = pickle.load(open("columns.pkl", "rb"))
visa_encoder = pickle.load(open("visa_encoder.pkl", "rb"))
country_encoder = pickle.load(open("country_encoder.pkl", "rb"))
state_encoder = pickle.load(open("state_encoder.pkl", "rb"))

print("✅ Everything loaded successfully")


# ================= SAFE MEAN FUNCTION =================
def get_safe_mean(enc):
    try:
        # if dictionary
        return float(np.mean(list(enc.values())))
    except:
        # if numpy array
        return float(np.mean(enc))


# ================= API =================
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        print("Incoming Data:", data)

        # ===== INPUTS =====
        month = int(data.get("month", 0))
        years = int(data.get("years", 0))
        day = int(data.get("day", 0))
        season = data.get("season", "Peak")

        visa = data.get("visa", "")
        country = data.get("country", "")
        state = data.get("state", "")

        # ===== ENCODING (SAFE) =====
        visa_avg = (
            float(visa_encoder[visa])
            if visa in visa_encoder
            else get_safe_mean(visa_encoder)
        )

        country_avg = (
            float(country_encoder[country])
            if country in country_encoder
            else get_safe_mean(country_encoder)
        )

        state_avg = (
            float(state_encoder[state])
            if state in state_encoder
            else get_safe_mean(state_encoder)
        )

        # ===== CREATE INPUT =====
        input_df = pd.DataFrame({
            "application_month": [month],
            "years_since_start": [years],
            "application_dayofweek": [day],
            "season": [season],
            "visa_avg_processing_time": [visa_avg],
            "country_avg_processing_time": [country_avg],
            "state_avg_processing_time": [state_avg]
        })

        print("Before Encoding:\n", input_df)

        # ===== MATCH TRAIN FORMAT =====
        input_df = pd.get_dummies(input_df)
        input_df = input_df.reindex(columns=columns, fill_value=0)

        print("After Encoding:\n", input_df)

        # ===== PREDICT =====
        prediction = model.predict(input_df)

        # Fix ndarray issue
        if isinstance(prediction, np.ndarray):
            prediction = prediction[0]

        prediction = float(prediction)

        # ===== RESPONSE =====
        return jsonify({
            "prediction": round(prediction, 2),
            "range": [
                round(prediction - 5, 2),
                round(prediction + 5, 2)
            ]
        })

    except Exception as e:
        print("🔥 ERROR:", str(e))
        return jsonify({"error": str(e)})


# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)