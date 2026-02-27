# AI-Enabled Visa Status Prediction and Processing Time Estimation

 ### Project Overview
This project analyzes historical U.S. visa application data to build a predictive model for estimating visa processing time (in days).
The project follows a structured Machine Learning workflow:

Data Cleaning
Exploratory Data Analysis (EDA)
Feature Engineering
Model-Ready Dataset Preparation
Currently, Milestone 1 and Milestone 2 are completed.
---
### Problem Statement

Given visa application data, predict the number of days required to process the application.
---
### Milestone 1: Data Collection & Preprocessing

This milestone focuses on collecting relevant visa application data and preparing it for further analysis. The objective is to clean, standardize, and structure the raw data so it can be reliably used in subsequent stages of the project.

## Tasks Performed

### 1. Data Collection

* Loaded visa-related data from a publicly available source
* Inspected dataset shape, columns, and missing values

### 2. Data Preprocessing

* Dropped irrelevant and redundant columns
* Renamed columns for clarity (e.g., application and decision dates)
* Converted date columns to standard datetime format
* Created a mandatory derived feature:

  * `processing_time_days` = decision date − application date
* Handled missing and inconsistent values

---

## Output

* A clean, structured dataset ready for exploratory analysis

---
### Milestone 2 – EDA & Feature Engineering

This phase focused on understanding patterns and building meaningful predictive features

---
### Exploratory Data Analysis
1️⃣ Target Distribution
Observed skewed distribution of processing times
Identified extreme outliers in early years

2️⃣ Year-wise Trend Analysis
Processing time decreased dramatically over time:

Year        	Avg Processing Days

2008        	2331
2015        	6
This revealed a strong temporal trend and motivated creation of time-based features.
---
🛠 Feature Engineering
The following features were created based on data insights:
---
🔹 Temporal Features
1 application_month : Captures seasonal effects.
2 season :Peak (Jan, Feb, Dec) vs Off-Peak months.
3 years_since_start : Continuous time progression feature

years_since_start = application_year - minimum_year

This captures long-term improvements in processing efficiency and is one of the strongest predictive signals.

4 application_dayofweek : Captures potential weekday vs weekend submission patterns.
---
🔹 Aggregated Feature
visa_avg_processing_time
---
⚠ Country Feature Analysis

COUNTRY_OF_CITIZENSHIP contained ~93% missing values.
To avoid noise and unreliable modeling:
Country-level aggregation was not used as a primary feature.
Feature selection decisions were made based on data quality, not assumption.
---
📈 Feature Validation

After feature engineering:
Correlation matrix was generated for numerical features.
Temporal trend was visually validated.
Seasonal distribution plots were analyzed.
Feature usefulness was confirmed before proceeding.

---
🔢 Encoding & Scaling

Encoding 
One-Hot Encoding applied to:
VISA_CLASS
CASE_STATUS
WORK_STATE
season

Scaling 
StandardScaler applied to:
application_month
visa_avg_processing_time
years_since_start
application_dayofweek

Target variable was not scaled.
---
📁 Milestone 2 Output
Final model-ready dataset: final_ml_ready_visa_data.csv
---
Key Insights

Processing efficiency improved significantly over time.
Temporal features are dominant predictors.
Visa class contributes meaningful variation.
Country data lacked sufficient completeness.
Proper feature validation prevents overfitting and noise injection.
---
visa-processing-prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── cleaned_visa_data.csv
│       └── final_ml_ready_visa_data.csv
│
├── notebooks/
│   └── eda.py
|
│
├── src/
│   └── preprocessing.py
│
└── README.md

---
Skills Demonstrated

Data Cleaning & Preprocessing
Exploratory Data Analysis
Feature Engineering
Temporal Trend Analysis
Handling Large-Scale Missing Data
Encoding & Scaling Techniques
---
## Tools Used

* **Python**
* **Pandas**
* **VS Code**

---

