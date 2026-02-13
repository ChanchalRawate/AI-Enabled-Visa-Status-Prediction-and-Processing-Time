import pandas as pd


df = pd.read_excel("../data/USAforeignworkerssalarydata.csv")

print("Raw Shape:", df.shape)


df = df[
    [
        "CASE_STATUS",
        "CASE_RECEIVED_DATE",
        "DECISION_DATE",
        "VISA_CLASS",
        "COUNTRY_OF_CITIZENSHIP",
        "WORK_STATE",
    ]
]


df.rename(
    columns={"CASE_RECEIVED_DATE": "APPLICATION_DATE"},
    inplace=True
)


df["APPLICATION_DATE"] = pd.to_datetime(
    df["APPLICATION_DATE"], errors="coerce"
)
df["DECISION_DATE"] = pd.to_datetime(
    df["DECISION_DATE"], errors="coerce"
)


df["processing_time_days"] = (
    df["DECISION_DATE"] - df["APPLICATION_DATE"]
).dt.days


df = df[df["processing_time_days"].notna()]
df = df[df["processing_time_days"] >= 0]


categorical_cols = [
    "VISA_CLASS",
    "COUNTRY_OF_CITIZENSHIP",
    "WORK_STATE",
]

df[categorical_cols] = df[categorical_cols].fillna("Unknown")


df.to_csv("../data/cleaned_visa_data.csv", index=False)

print("Preprocessing completed.")
print("Cleaned Shape:", df.shape)
print("\nMissing values after preprocessing:")
print(df.isnull().sum())
