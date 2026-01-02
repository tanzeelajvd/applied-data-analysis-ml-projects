# Financial Fraud Detection System

This project implements an **end-to-end financial fraud detection pipeline**, combining data preprocessing, machine learning modeling, and a lightweight application layer. The objective is to demonstrate how structured financial data can be transformed into actionable insights and predictive models for identifying potentially fraudulent transactions.

The project is organized as a **step-by-step workflow**, making it easy to follow how raw data is cleaned, modeled, and finally consumed by an application.

---

## Problem Statement

Financial fraud poses significant risks to businesses and customers. Detecting fraudulent behavior requires careful data preprocessing, feature engineering, and the application of reliable machine learning models.

This project aims to:
- analyze financial transaction data,
- build a machine learning model for fraud detection,
- and demonstrate how the model can be integrated into an application-style workflow.

---

## Project Workflow

The project is structured into distinct stages:

### 1. Data Preprocessing
**`1.preprocessing.ipynb`**
- Loading raw financial datasets
- Handling missing values and inconsistencies
- Feature selection and transformation
- Preparing data for modeling

### 2. Model Development
**`2.model.ipynb`**
- Training machine learning models for fraud detection
- Model evaluation and performance analysis
- Comparison of results and interpretation

### 3. Application Layer
**`3.App.ipynb`**
- Demonstration of how the trained model can be used in an application context
- Simulating predictions on new or unseen data

### 4. End-to-End Notebook
**`Fraud_detection.ipynb`**
- Consolidated view of the full pipeline
- Useful for quick review and demonstration

---

## Dataset

The raw datasets used in this project are **not included in the repository** due to size constraints.

- The data consists of structured financial records used for fraud detection.
- Large CSV files are intentionally excluded to keep the repository lightweight.

To run the project, place the datasets locally under:

```

datasets/

```

> This repository focuses on methodology, modeling, and workflow design rather than dataset distribution.

---

## Repository Structure

```

02_financial_fraud_detection_system/
│
├── datasets/                 # Dataset directory (ignored in Git)
│   └── .gitkeep
├── 1.preprocessing.ipynb
├── 2.model.ipynb
├── 3.App.ipynb
├── Fraud_detection.ipynb
├── requirements.txt
└── README.md

````

---

## How to Run

1. Clone the main repository:
   ```bash
   git clone git@github.com:tanzeelajvd/applied-data-analysis-ml-projects.git
   ````

2. Navigate to this project:

   ```bash
   cd applied-data-analysis-ml-projects/02_financial_fraud_detection_system
   ```

3. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

6. Run notebooks in order:

   * `1.preprocessing.ipynb`
   * `2.model.ipynb`
   * `3.App.ipynb`

---

## Technologies Used

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Jupyter Notebook

---

## Key Learnings

* Importance of data preprocessing in fraud detection
* Feature-driven modeling for imbalanced datasets
* Translating ML models into application-ready workflows
* End-to-end thinking in applied machine learning projects

---

## Disclaimer

This project is intended for **educational and research purposes only**.
It is **not** intended for real-world financial decision-making.

---

## Author

**Tanzeela Javid**
Applied Machine Learning · Data Analysis · AI Systems





