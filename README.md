# AI-Enabled Visa Status Prediction and Processing Time Estimation

## 📌 Project Overview

This project analyzes historical U.S. visa application data to build a predictive model for estimating **visa processing time (in days)**.

The project follows a structured Machine Learning workflow:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model-Ready Dataset Preparation

Currently, **Milestone 1 and Milestone 2 are completed**.

---

# 🎯 Problem Statement

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

# 🧱 Project Milestones

## ✅ Milestone 1 – Data Cleaning & Preprocessing

### Key Tasks Completed

* Converted date columns to proper datetime format
* Created target variable (`processing_time_days`)
* Removed invalid or inconsistent records
* Handled missing values
* Standardized categorical values
* Verified logical consistency

### Output

```
data/processed/cleaned_visa_data.csv
```

---

## ✅ Milestone 2 – EDA & Feature Engineering

This phase focused on understanding patterns and building meaningful predictive features.

---

# 📊 Exploratory Data Analysis

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

# 🛠 Feature Engineering

The following features were created based on data insights:

---

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

## 🔹 Aggregated Feature

### `visa_avg_processing_time`

Average processing time grouped by visa class.

This captures visa-type-specific behavior and workload differences.

---

## ⚠ Country Feature Analysis

`COUNTRY_OF_CITIZENSHIP` contained ~93% missing values.

To avoid noise and unreliable modeling:

* Country-level aggregation was not used as a primary feature.
* Feature selection decisions were made based on data quality, not assumption.

---

# 📈 Feature Validation

After feature engineering:

* Correlation matrix was generated for numerical features.
* Temporal trend was visually validated.
* Seasonal distribution plots were analyzed.
* Feature usefulness was confirmed before proceeding.

---

# 🔢 Encoding & Scaling

### Encoding

One-Hot Encoding applied to:

* VISA_CLASS
* CASE_STATUS
* WORK_STATE
* season

### Scaling

StandardScaler applied to:

* application_month
* visa_avg_processing_time
* years_since_start
* application_dayofweek

Target variable was not scaled.

---

# 📁 Milestone 2 Output

Final model-ready dataset:

```
data/processed/final_ml_ready_visa_data.csv
```

This dataset is fully prepared for modeling.

---

#  Key Insights

* Processing efficiency improved significantly over time.
* Temporal features are dominant predictors.
* Visa class contributes meaningful variation.
* Country data lacked sufficient completeness.
* Proper feature validation prevents overfitting and noise injection.

---

# ⚠ Modeling Consideration

Due to strong temporal trends, a random train-test split may introduce:

* Distribution shift
* Temporal leakage
* Misleading performance metrics

Milestone 3 will implement a time-aware validation strategy.

---

# 🗂 Project Structure

```
visa-processing-prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── cleaned_visa_data.csv
│       └── final_ml_ready_visa_data.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   └── preprocessing.py
│
└── README.md
```

---

# 💡 Skills Demonstrated

* Data Cleaning & Preprocessing
* Exploratory Data Analysis
* Feature Engineering
* Temporal Trend Analysis
* Handling Large-Scale Missing Data
* Encoding & Scaling Techniques
* Structured ML Workflow Design

---


## Tools Used

* **Python**
* **Pandas**
* **VS Code**

---

