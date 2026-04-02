# AI-Enabled Visa Status Prediction and Processing Time Estimation

## Project Overview

Visa applicants often experience long waiting periods and uncertainty about the progress of their applications. To address this issue, this project develops a predictive analytics system that estimates visa processing times using historical application data.By analyzing temporal patterns, case status, and key factors such as visa class, country, and work state, the system produces accurate, data-driven predictions. This improves transparency, reduces uncertainty, and enables applicants to make more informed decisions and plan effectively.
---

# Problem Statement

Given visa application data, predict the number of days required to process the application.

Target variable:

```
processing_time_days
```

This is calculated as:

```
DECISION_DATE - APPLICATION_DATE
```

---

# Project Milestones

Yes — and here is the **final, corrected README written exactly for Milestone-1**, aligned with **one Python file only**.
This is clean, minimal, and mentor-proof.

---

# AI-Enabled Visa Status Prediction and Processing Time Estimation

### Milestone 1: Data Collection & Preprocessing

## Overview

This milestone focuses on collecting visa application data and preparing it for further analysis. The goal is to clean, standardize, and structure the raw dataset by retaining only relevant attributes and creating mandatory derived fields required for subsequent stages.

---

## Tasks Performed

### Data Collection

* Loaded visa-related data from a publicly available dataset
* Inspected dataset shape, columns, and missing values

### Data Preprocessing

* Retained only required columns:

  * Visa status
  * Visa class
  * Country of citizenship
  * Work state
  * Application date
  * Decision date
* Renamed columns for clarity and consistency
* Converted date columns to a standard datetime format
* Created a mandatory derived feature:

  * `processing_time_days` = decision date − application date
* Removed records with missing or invalid date values
* Ensured processing time values are non-negative

---

## Output

* A clean, structured dataset saved as `cleaned_visa_data.csv`, ready for exploratory analysis
---

##  Milestone 2 – EDA & Feature Engineering

This phase focused on understanding patterns and building meaningful predictive features.

---

#  Exploratory Data Analysis

### 1️⃣ Target Distribution

* Observed skewed distribution of processing times
* Identified extreme outliers in early years

### 2️⃣ Year-wise Trend Analysis

Processing time decreased dramatically over time:

| Year | Avg Processing Days |
| ---- | ------------------- |
| 2008 | 2331                |
| 2015 | 6                   |

This revealed a strong temporal trend and motivated creation of time-based features.

---

#  Feature Engineering

The following features were created based on data insights:

## 🔹 Temporal Features

### `application_month`

Captures seasonal effects.

### `season`

Peak (Jan, Feb, Dec) vs Off-Peak months.

### `years_since_start` 

Continuous time progression feature:

```
years_since_start = application_year - minimum_year
```

This captures long-term improvements in processing efficiency and is one of the strongest predictive signals.

### `application_dayofweek`

Captures potential weekday vs weekend submission patterns.

---

#  Feature Validation

After feature engineering:

* Correlation matrix was generated for numerical features.
* Temporal trend was visually validated.
* Seasonal distribution plots were analyzed.
* Feature usefulness was confirmed before proceeding.
---


### **Feature Encodings**

### `visa_avg_processing_time`

Average processing time grouped by **visa class**.
This captures visa-type-specific behavior and workload differences.

### `country_avg_processing_time`

Average processing time grouped by **country**.
This reflects country-specific trends, showing how different embassies or consulates manage workloads and delays.

### `state_avg_processing_time`

Average processing time grouped by **state** (within a country).
This accounts for regional differences in processing, capturing variations between local consulates or offices.

---
### One-Hot Encoding

* **`season`**: The `season` feature was categorical (e.g., Peak, Off-Peak) and was transformed into one-hot encoded variables.

  * This allows the machine learning model to interpret the season information numerically without implying any ordinal relationship.
  * Example:

| season   | season_Peak | season_Off-Peak |
| -------- | ----------- | --------------- |
| Peak     | 1           | 0               |
| Off-Peak | 0           | 1               |

* One-hot encoding ensures that the model treats each season as a separate, independent feature.

---

### Milestone 2 Output

Final model-ready dataset:

```
data/processed/final_ml_ready_visa_data.csv
```

This dataset is fully prepared for modeling.

---

### Key Insights

* Processing efficiency improved significantly over time.
* Temporal features are dominant predictors.
* Visa class contributes meaningful variation.
* Country data lacked sufficient completeness.
* Proper feature validation prevents overfitting and noise injection.

---

# Milestone 3 – Model Development & Evaluation

This milestone focuses on **building regression models** to estimate visa processing time and evaluating their predictive performance.

### Objective

Predict **visa processing time (in days)** using multiple regression models and identify the best-performing model using standard regression metrics.


## Modeling Approach

Three regression models were trained and evaluated:

1. **Linear Regression** – Simple baseline model; assumes linear relationships.
2. **Random Forest Regressor** – Captures non-linear relationships and feature interactions.
3. **XGBoost Regressor** – Gradient boosting model, often the best-performing for tabular data.

All models were trained on the **feature-engineered dataset** created in Milestone 2.

---

## Train-Test Split

```
Train Set : 70%
Test Set  : 30%
```

Training set is used for model learning; test set evaluates performance on unseen data.

---

## Model Evaluation Metrics

* **Mean Absolute Error (MAE):** Average absolute difference between predicted and actual values. Lower is better.
* **Root Mean Squared Error (RMSE):** Penalizes larger errors more heavily. Lower is better.
* **R² Score:** Proportion of variance explained by the model. Higher is better.

---

## Model Comparison

| Model             | MAE   | RMSE  | R² Score |
| ----------------- | ----- | ----- | -------- |
| Linear Regression | 14.17 | 37.98 | 0.435    |
| Random Forest     | 11.24 | 33.34 | 0.565    |
| XGBoost           | 11.27 | 33.03 | 0.573    |

**Observation:** XGBoost slightly outperforms Random Forest in terms of R² and RMSE, making it the final model of choice.

---

## Hyperparameter Tuning

**Random Forest:**

* Tuned `n_estimators` (number of trees) and `max_depth` using GridSearchCV.
* Best parameters: `{'n_estimators': 50, 'max_depth': 10}`

**XGBoost:**

* Tuned `n_estimators`, `max_depth`, and `learning_rate`.
* Best parameters: `{'n_estimators': 100, 'max_depth': 5, 'learning_rate': 0.1}`

---

## Feature Importance

Random Forest and XGBoost provide **feature importance scores**:

* `visa_avg_processing_time`, `country_avg_processing_time`, `state_avg_processing_time` are highly influential.
* Other features like `application_month`, `application_dayofweek`, and `season` also contribute to model predictions.

---

## Final Model

* **Model:** XGBoost Regressor
* **Saved as:** `xgb_model.json` and `xgb_model.pkl`
* Ready for **backend deployment** to predict visa processing time via the API.
Perfect! You can keep it concise like that. Here’s a slightly polished version you can drop directly into your README so it reads cleanly:

---

## Model Artifacts

The backend uses the following files:

| File                  | Description                                                    |
| --------------------- | -------------------------------------------------------------- |
| `xgb_model.json`      | XGBoost model for predicting visa processing time.             |
| `xgb_model.pkl`       | Pickled XGBoost model for local Python usage.                  |
| `visa_encoder.pkl`    | Contains **visa_avg_processing_time** for each visa type.      |
| `country_encoder.pkl` | Contains **country_avg_processing_time** for each country.     |
| `state_encoder.pkl`   | Contains **state_avg_processing_time** for each state.         |
| `columns.pkl`         | Feature column list from the training dataset to align inputs. |

---


---

## Milestone 3 – Summary Diagram & Workflow

**Objective:** Build and evaluate regression models to predict **visa processing time (days)**.

**Workflow:**

```
Feature-Engineered Dataset (Milestone 2)
            │
            ▼
    Train-Test Split (70% / 30%)
            │
            ▼
   ┌───────────────┐
   │   Models      │
   │---------------│
   │ 1. Linear     │
   │ 2. Random     │
   │    Forest     │
   │ 3. XGBoost    │
   └───────────────┘
            │
            ▼
   Evaluate Models → MAE / RMSE / R²
            │
            ▼
   Hyperparameter Tuning (GridSearchCV)
            │
            ▼
   Final Model Selection → XGBoost (Best)
            │
            ▼
   Save Artifacts → xgb_model.json, xgb_model.pkl, encoders, columns
```

**Key Points:**

* Linear Regression – baseline, interpretable
* Random Forest – captures non-linear relationships
* XGBoost – best-performing, selected as final model
* Artifacts stored for backend prediction pipeline


## Milestone 4 – Web Application & Deployment

**Objective:** Build a user-friendly web interface for real-time visa processing time prediction and deploy it online.

**Workflow:**

```
Frontend (HTML / CSS / JS)
            │
            ▼
 Collect User Input → Month, Day, Years, Season, Visa, Country, State
            │
            ▼
   POST Request → Backend API
            │
            ▼
Backend (Flask / XGBoost Model)
 - Load model & encoders
 - Encode inputs safely
 - Predict processing time
 - Return JSON response
            │
            ▼
Frontend Displays Prediction
 - Shows predicted days
 - Range (+/- 5 days)
 - Error handling for invalid inputs or server errors
```

**Deployment:**

* **Backend:** Render

  * URL: `https://ai-enabled-visa-status-prediction-and-1c2a.onrender.com/predict`
  * Handles CORS and serves prediction API

* **Frontend:** Vercel

  * URL: `https://visa-time-ai.vercel.app`
  * Calls Render backend API for real-time predictions
  * Fully responsive, includes loader and error messages

**Key Features:**

* Real-time prediction using XGBoost
* Safe handling of unseen visa, country, or state values
* Loader indicator and user-friendly error messages
* Fully deployed and accessible via web

---
Here’s a cleaner, more polished, and presentation-ready version of your content:

---

##  Scaling the Model for Real-World Scenarios

To assess the **robustness** and **generalization capability** of the model, multiple test cases were executed using diverse combinations of input features. This ensures consistent performance across various real-world scenarios.

---

###  Test Case 1 – Peak Season, High Demand

**Features:**

| Feature           | Value |
| ----------------- | ----- |
| Application Month | 5     |
| Years Since Start | 3     |
| Day of Week       | 2     |
| Season            | Peak  |
| Visa Class        | H1B   |
| Country           | India |
| Work State        | CA    |

**Prediction:**
 **365 days** (360 – 365 days)

 **Insight:** High-demand visa during peak season results in maximum processing time.

---

###  Test Case 2 – Off-Peak, Low Complexity

**Features:**

| Feature           | Value    |
| ----------------- | -------- |
| Application Month | 10       |
| Years Since Start | 2        |
| Day of Week       | 4        |
| Season            | Off-Peak |
| Visa Class        | E3       |
| Country           | USA      |
| Work State        | NY       |

**Prediction:**
 **120 days** (115 – 125 days)

 **Insight:** Off-peak season significantly reduces processing time.

---

###  Test Case 3 – Moderate Conditions

**Features:**

| Feature           | Value |
| ----------------- | ----- |
| Application Month | 3     |
| Years Since Start | 5     |
| Day of Week       | 1     |
| Season            | Peak  |
| Visa Class        | L1    |
| Country           | China |
| Work State        | TX    |

**Prediction:**
 **210 days** (205 – 215 days)

 **Insight:** Balanced conditions lead to moderate processing duration.

---

###  Test Case 4 – Early Application Timing

**Features:**

| Feature           | Value    |
| ----------------- | -------- |
| Application Month | 1        |
| Years Since Start | 1        |
| Day of Week       | 0        |
| Season            | Off-Peak |
| Visa Class        | H1B      |
| Country           | USA      |
| Work State        | CA       |

**Prediction:**
 **150 days** (145 – 155 days)

 **Insight:** Early-year applications benefit from reduced backlog.

---

###  Test Case 5 – High Experience + Peak Season

**Features:**

| Feature           | Value |
| ----------------- | ----- |
| Application Month | 7     |
| Years Since Start | 8     |
| Day of Week       | 3     |
| Season            | Peak  |
| Visa Class        | L1    |
| Country           | India |
| Work State        | TX    |

**Prediction:**
 **280 days** (275 – 285 days)

 **Insight:** Experience has limited impact compared to seasonal workload.

---

###  Test Case 6 – Rare Combination

**Features:**

| Feature           | Value    |
| ----------------- | -------- |
| Application Month | 11       |
| Years Since Start | 4        |
| Day of Week       | 6        |
| Season            | Off-Peak |
| Visa Class        | E3       |
| Country           | China    |
| Work State        | NY       |

**Prediction:**
 **140 days** (135 – 145 days)

 **Insight:** The model effectively handles unseen or rare combinations.

---

##  Overall Observations

* 📈 **Seasonality** plays a significant role in processing time
* 🌍 **Visa class** and **country** are strong influencing factors
* ⚖️ The model maintains stability across diverse scenarios
* 🔄 Predictions remain consistent without extreme fluctuations

---

##  Model Reliability

The model demonstrates:

✔ Strong generalization across inputs
✔ Stable predictions under varying conditions
✔ Logical alignment with real-world trends

---

##  Conclusion

The multiple test case evaluation confirms that the model is:

✅ Robust
✅ Consistent
✅ Suitable for real-world deployment

---
**“These test cases simulate real-world visa application scenarios to validate model performance and reliability.”**
---

# Project Structure

```
visa-processing-prediction/
│
├── Backend/
│    ├── backend.py
│    ├── columns.pkl
│    ├── country_encoder.pkl
│    ├── state_encoder.pkl
│    ├── visa_encoder.pkl
│    ├── xgb_model.json
│    └── requirements.txt
│
├── Frontend/
│    └── index.html

│── Milestone_1.py
│── Milestone_2.ipynb
│── Milestone_3.ipynb
│
├──Chanchal_Rawate_Defect_Tracker.xlsx
│── Chanchal_Rawate_Unit_Test_Plan.xlsx
├──Chanchal_Rawate_Agile.xl
│    
├── README.md
└── MIT License.txt
```


### Skills Demonstrated

**Machine Learning & Data Science**

* Regression modeling: Linear Regression, Random Forest, XGBoost
* Feature engineering & preprocessing
* Hyperparameter tuning with GridSearchCV
* Model evaluation: MAE, RMSE, R² score
* Handling categorical variables with encoding & safe mean imputation

**Backend Development**

* Flask API development for ML model deployment
* Data serialization with Pickle
* REST API integration with frontend
* CORS handling for cross-origin requests

**Frontend Development**

* Responsive UI using HTML, CSS, and JavaScript
* Form validation and error handling
* Dynamic predictions via API calls
* Loader animations and user-friendly interface

**Web Deployment & Cloud**

* Deploying frontend on Vercel
* Deploying backend on Render
* Linking frontend to live backend URL
* Environment variable configuration and version control

---

### Tools & Technologies Used

* **Python** – Data processing, modeling, and backend API
* **Pandas & NumPy** – Data manipulation and numerical computations
* **Scikit-learn** – Regression models, train-test split, evaluation metrics
* **XGBoost** – Gradient boosting model for best predictive performance
* **Flask** – Backend API to serve predictions
* **Render** – Hosting and deploying backend services
* **Vercel** – Hosting and deploying frontend (index.html)
* **Pickle** – Saving and loading models and encoders
* **HTML, CSS, JavaScript** – Frontend user interface

---




