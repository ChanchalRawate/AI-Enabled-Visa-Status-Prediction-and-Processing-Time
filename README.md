# AI-Enabled Visa Status Prediction and Processing Time Estimation

## Project Overview

This project analyzes historical U.S. visa application data to build a predictive model for estimating **visa processing time (in days)**.

The project follows a structured Machine Learning workflow:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model-Ready Dataset Preparation

Currently, **Milestone 1 and Milestone 2 are completed**.

---

#  Problem Statement

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

##  Milestone 1 – Data Cleaning & Preprocessing

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

#  Feature Validation

After feature engineering:

* Correlation matrix was generated for numerical features.
* Temporal trend was visually validated.
* Seasonal distribution plots were analyzed.
* Feature usefulness was confirmed before proceeding.

---

#  Feature Encoding
Perfect! Here’s a clean, professional section for your README that includes all three features together:

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

### Encoding

One-Hot Encoding applied to:

* season
---

#  Milestone 2 Output

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

# Modeling Consideration

Due to strong temporal trends, a random train-test split may introduce:

* Distribution shift
* Temporal leakage
* Misleading performance metrics

---

## Milestone 3 – Model Development & Evaluation

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

---
Here’s a compact and professional section you can add to your README for **Milestone 4 – Web Application & Deployment**:

---

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

  * URL: `https://<your-render-backend>.onrender.com/predict`
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
# Project Structure

```
visa-processing-prediction/
│
├── data/
│    └── processed/
│       ├── cleaned_visa_data.csv
│       └── final_ml_ready_visa_data.csv
│__MIT license.txt
├─eda.py
│── eda.ipynb
│__visa_prediction.py
|__ visa_prediction.ipynb
├──raw dataset
│── preprocessing.py
│
└── README.md
```


---

# Skills Demonstrated (Updated)

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Regression Modeling
* Model Evaluation (MAE, RMSE)
* Hyperparameter Tuning
* Feature Importance Analysis
* End-to-End Machine Learning Workflow

---

## Tools Used

* **Python**
* **Pandas**
* **VS Code**
* **jupyter notetbook**
---

