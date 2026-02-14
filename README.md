---

# AI-Enabled Visa Status Prediction and Processing Time Estimation

### Milestone 1: Data Collection & Preprocessing

## Overview

This milestone focuses on collecting relevant visa application data and preparing it for further analysis. The objective is to clean, standardize, and structure the raw data so it can be reliably used in subsequent stages of the project.

---

## Project Structure

```
├── data/
│   ├── raw/                 # Original dataset
│          
├── src/
│   ├── load_data.py         # Data loading and basic inspection
│   ├── preprocessing.py    # Data cleaning and preparation
│
├── README.md
```

---

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

## Tools Used

* **Python**
* **Pandas**
* **VS Code**

---

