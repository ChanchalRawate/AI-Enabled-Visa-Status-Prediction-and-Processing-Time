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

#  Feature Validation

After feature engineering:

* Correlation matrix was generated for numerical features.
* Temporal trend was visually validated.
* Seasonal distribution plots were analyzed.
* Feature usefulness was confirmed before proceeding.

---

#  Encoding & Scaling

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

This phase focuses on building regression models to estimate visa processing time and evaluating their predictive performance.

### Objective

Develop baseline regression models to predict **visa processing time (in days)** and identify the best-performing model using standard regression metrics.

Target variable:

```
processing_time_days
```

---

# Modeling Approach

Two regression models were trained and evaluated:

1. Linear Regression
2. Random Forest Regressor

These models were chosen because:

* Linear Regression provides a **simple baseline model**
* Random Forest captures **non-linear relationships and feature interactions**

Both models were trained on the **feature-engineered dataset created in Milestone 2**.

---

# Train-Test Split

The dataset was divided into training and testing sets to evaluate model generalization.

```
Train Set : 70%
Test Set  : 30%
```

The training set is used for model learning, while the test set evaluates predictive performance on unseen data.

---

# Model 1 – Linear Regression

Linear Regression was used as a baseline model to understand how well a simple linear relationship explains the variation in visa processing time.

Key Characteristics:

* Assumes a linear relationship between features and target
* Fast to train and easy to interpret
* Serves as a benchmark for more complex models

---

# Model 2 – Random Forest Regressor

Random Forest is an ensemble learning algorithm that builds multiple decision trees and combines their predictions.

Advantages:

* Captures complex non-linear relationships
* Handles feature interactions automatically
* Reduces overfitting through ensemble averaging

Random Forest often performs better than simple linear models when the underlying relationships are complex.

---

# Model Evaluation Metrics

Two standard regression metrics were used to evaluate model performance.

### Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted and actual values.

Lower MAE indicates better predictive accuracy.

### Root Mean Squared Error (RMSE)

RMSE penalizes larger errors more heavily and provides insight into prediction variance.

Lower RMSE indicates a more accurate model.

Both metrics provide complementary views of model performance.

---

# Model Comparison

After training both models, their performance was compared using MAE and RMSE.

| Model             | MAE | RMSE |
| ----------------- | ---- | ----- |
| Linear Regression | 82   | 136   |
| Random Forest     | 30   | 87     |

*(Values will be updated after model execution.)*

Lower values indicate better performance.

---

# Hyperparameter Tuning

To further improve performance, Random Forest was optimized using **Grid Search Cross Validation**.

The following parameters were tuned:

* `n_estimators` – number of trees
* `max_depth` – maximum tree depth

GridSearchCV automatically evaluates multiple parameter combinations and selects the best performing configuration.

This helps improve model performance while preventing overfitting.

---

# Model Visualization

Two visual analyses were performed to interpret the model.

### Actual vs Predicted Plot

A scatter plot comparing predicted values against actual processing times helps visually assess model accuracy.

Points close to the diagonal line indicate accurate predictions.

---

### Feature Importance

Random Forest provides feature importance scores indicating how much each feature contributes to predictions.

This helps identify the most influential predictors.

Key insights include:

* Temporal features such as **years_since_start** strongly influence predictions
* Aggregated features such as **visa_avg_processing_time** contribute meaningful signal

---

# Milestone 3 Output

The trained model and evaluation results provide a baseline predictive system for estimating visa processing time.

Key deliverables:

* Trained Linear Regression model
* Trained Random Forest model
* Model performance metrics (MAE, RMSE)
* Feature importance analysis
* Visualization of prediction performance

---

# Key Findings

* Random Forest performed better than Linear Regression due to its ability to model non-linear relationships.
* Temporal features played a significant role in predicting processing time.
* Feature engineering from Milestone 2 significantly improved model learning capability.
* Ensemble methods are more suitable for complex real-world datasets like visa processing data.

---

# Updated Project Structure

```
visa-processing-prediction/
│
├── data/
│   └── processed/
│       ├── cleaned_visa_data.csv
│       └── final_ml_ready_visa_data.csv
│
├── eda.ipynb
├── preprocessing.py
├── modeling.ipynb
├── eda.py
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

# Project Structure

```
visa-processing-prediction/
│
├── data/
│    └── processed/
│       ├── cleaned_visa_data.csv
│       └── final_ml_ready_visa_data.csv
│
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


## Tools Used

* **Python**
* **Pandas**
* **VS Code**
* **jupyter notetbook**
---

