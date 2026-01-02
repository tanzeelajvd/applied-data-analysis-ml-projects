# Drug Recommendation and Analysis

This project explores medicine-related data to perform **data analysis and feature-driven exploration** aimed at supporting a **drug recommendation workflow**. The focus is on understanding structured healthcare data, extracting meaningful insights, and demonstrating how classical machine learning techniques can be applied in a medical data context.

Rather than building a black-box recommender system, this project emphasizes **interpretability, exploratory analysis, and practical ML pipelines**, which are critical in healthcare-related applications.

---

## Problem Overview

Healthcare datasets often contain detailed information about medicines, their usage, and associated attributes. Extracting useful insights from such data requires careful preprocessing, exploratory analysis, and structured modeling.

This project aims to:
- analyze medicine datasets to understand usage patterns,
- explore relationships between drugs and relevant attributes,
- demonstrate how recommendation logic can be derived from data-driven insights.

---

## Workflow

The project follows a standard applied machine learning workflow:

1. **Data Ingestion**
   - Loading structured medicine data
   - Initial inspection and sanity checks

2. **Data Cleaning**
   - Handling missing and inconsistent values
   - Formatting and normalizing relevant fields

3. **Exploratory Data Analysis (EDA)**
   - Distribution analysis of medicines and features
   - Identification of common trends and patterns
   - Visual exploration using plots and summaries

4. **Feature Engineering**
   - Transforming raw attributes into usable features
   - Encoding categorical variables where necessary

5. **Analytical / ML Techniques**
   - Applying basic machine learning and statistical techniques
   - Demonstrating how recommendations can be inferred from data patterns

6. **Result Interpretation**
   - Interpreting outputs with a focus on healthcare relevance and clarity

---

## Dataset

The raw dataset is **not included in this repository** due to size constraints.

- The dataset consists of structured information related to medicines and their attributes.
- Large data files are intentionally excluded to keep the repository lightweight and reproducible.

To run the project, place the dataset locally in:

```

dataset/

```

> This repository focuses on methodology and analysis rather than data distribution.

---

## Repository Structure

```

01_drug_recommendation_and_analysis/
│
├── dataset/                       # Dataset directory (ignored in Git)
│   └── .gitkeep
├── drug_recommendation_and_analysis.ipynb
├── requirements.txt
└── README.md

````

---

## How to Run

1. Clone the main repository:
   ```bash
   git clone git@github.com:tanzeelajvd/applied-data-analysis-ml-projects.git
   ````
---
2. Navigate to the project directory:

   ```bash
   cd applied-data-analysis-ml-projects/01_drug_recommendation_and_analysis
   ```

3. (Recommended) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Launch the notebook:

   ```bash
   jupyter notebook drug_recommendation_and_analysis.ipynb
   ```

---

## Technologies Used

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Jupyter Notebook

---

## Key Learnings

* Practical handling of real-world healthcare datasets
* Importance of exploratory analysis before modeling
* Feature-driven thinking for recommendation-style problems
* Emphasis on clarity and interpretability in ML workflows

---

## Disclaimer

This project is intended for **educational and research purposes only**.
It does **not** provide medical or clinical recommendations.

---

## Author

**Tanzeela Javid**
Applied Machine Learning · Data Analysis · AI Systems



