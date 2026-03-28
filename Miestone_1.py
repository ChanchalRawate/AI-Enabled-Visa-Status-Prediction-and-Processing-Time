import pandas as pd

df = pd.read_excel("../data/raw/USAforeignworkerssalarydata.csv")

print("Initial Shape:", df.shape)

print("\nInitial Columns:")
print(df.columns)

print("\nMissing values (before preprocessing):")
print(df.isnull().sum())

columns_to_keep = [
    "CASE_STATUS",
    "VISA_CLASS",
    "COUNTRY_OF_CITIZENSHIP",
    "WORK_STATE",
    "CASE_RECEIVED_DATE",
    "DECISION_DATE"
]

df = df[columns_to_keep]

df = df.rename(columns={
    "CASE_RECEIVED_DATE": "APPLICATION_DATE"
})

df["APPLICATION_DATE"] = pd.to_datetime(df["APPLICATION_DATE"], errors="coerce")
df["DECISION_DATE"] = pd.to_datetime(df["DECISION_DATE"], errors="coerce")

df["processing_time_days"] = (
    df["DECISION_DATE"] - df["APPLICATION_DATE"]
).dt.days

invalid_dates = df[
    df["APPLICATION_DATE"].isna() |
    df["DECISION_DATE"].isna() |
    (df["processing_time_days"] < 0)
]

print("\nNumber of invalid records:", invalid_dates.shape[0])

# ---- ACTUAL CLEANING (Milestone-2) ----
df = df.dropna(subset=["APPLICATION_DATE", "DECISION_DATE", "processing_time_days"])
df = df[df["processing_time_days"] >= 0]

print("\nFinal Shape after preprocessing:", df.shape)

print("\nFinal Columns:")
print(df.columns)

print("\nMissing values after preprocessing:")
print(df.isnull().sum())

# ---- SAVE CLEAN DATA FOR EDA ----
df.to_csv("../data/processed/cleaned_visa_data.csv", index=False)
print("\nCleaned dataset saved for EDA.")
