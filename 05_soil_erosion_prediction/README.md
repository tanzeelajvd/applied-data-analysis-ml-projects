
# Soil Erosion Risk Prediction System

This project implements an **end-to-end soil erosion risk prediction system** that combines classical machine learning models, a convolutional neural network (CNN) for soil type classification, and an interactive **Streamlit-based web application**.

The goal is to demonstrate how **heterogeneous data sources**—numerical environmental features and soil images—can be integrated into a unified prediction workflow for environmental risk assessment.

---

## Problem Overview

Soil erosion is a critical environmental issue influenced by terrain, vegetation, climate, soil composition, and land characteristics. Accurate erosion risk assessment requires combining multiple data modalities rather than relying on a single source.

This project aims to:
- predict soil erosion risk levels using structured environmental features,
- classify soil type from images using a CNN,
- integrate both sources into an interactive application for manual and image-based input.

---

## System Architecture

The system consists of three major components:

### 1. Classical Machine Learning Models
Two ML pipelines are used:
- **Light Model** – uses a reduced feature set for faster prediction
- **Full Model** – uses a comprehensive feature set for higher accuracy

Trained models and metadata:
- `light_model.pkl`
- `full_model.pkl`
- `light_features.pkl`
- `full_features.pkl`

---

### 2. Soil Type Classification (CNN)
A convolutional neural network is used to classify soil type from images.

- Model file: `soil_type_cnn_model.h5`
- Supported soil classes:
  - Black Soil
  - Cinder Soil
  - Laterite Soil
  - Peat Soil
  - Yellow Soil

The predicted soil type is encoded and incorporated into the erosion prediction pipeline.

---

### 3. Interactive Application (Streamlit)
**`app.py`**

- Built using Streamlit
- Allows manual feature input
- Supports optional soil image upload
- Displays erosion risk as human-readable categories:
  - No Erosion
  - Low Erosion
  - Moderate Erosion
  - High Erosion
  - Severe Erosion

The application provides two modes:
- **Light Model (Manual Input)**
- **Full Model (All Features + Image)**

---

## Dataset

The raw datasets used for training and evaluation are **not included in this repository** due to size constraints.

Local files used during experimentation include:
- `train_erosion.csv`
- `test_erosion.csv`
- `submission.csv`

These files are intentionally excluded from version control.

---

## Repository Structure

```

05_soil_erosion_prediction/
│
├── sample images/                 # Sample soil images
├── app.py                         # Streamlit application
├── soil-erosion.ipynb             # Data analysis & model training
├── soil_type_cnn_model.h5         # CNN model (local)
├── light_model.pkl                # Light ML model
├── full_model.pkl                 # Full ML model
├── light_features.pkl
├── full_features.pkl
├── correlation_heatmap.png
├── requirements.txt
└── README.md

````

---

## How to Run

### 1. Clone the repository
```bash
git clone git@github.com:tanzeelajvd/applied-data-analysis-ml-projects.git
cd applied-data-analysis-ml-projects/05_soil_erosion_prediction
````

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

The application will open in your browser automatically.

---

## Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* TensorFlow / Keras
* Streamlit
* Joblib
* Pillow
* Jupyter Notebook

---

## Key Learnings

* Integrating tabular and image-based data in ML systems
* Feature engineering for environmental modeling
* Combining CNNs with classical ML models
* Designing interactive ML applications with Streamlit
* Translating numeric predictions into interpretable risk categories

---

## Disclaimer

This project is intended for **educational and research purposes only**.
Predictions should not be used for real-world environmental or policy decisions.

---

## Author

**Tanzeela Javid**
Applied Machine Learning · Data Analysis · Environmental AI
