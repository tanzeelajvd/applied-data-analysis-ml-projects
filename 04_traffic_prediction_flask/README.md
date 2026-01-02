# Traffic Prediction System (Flask Application)

This project implements an **end-to-end traffic prediction system** that combines data analysis, machine learning, and a Flask-based web application. The goal is to demonstrate how traffic-related data can be used to train a predictive model and expose it through a simple, interactive application.

The project covers the complete workflow—from exploratory analysis and model training to serving predictions via a REST-style interface.

---

## Problem Overview

Accurate traffic prediction is essential for traffic management, urban planning, and congestion reduction. By analyzing historical traffic data, machine learning models can learn patterns related to time, vehicle counts, and temporal features.

This project aims to:
- analyze traffic data,
- train a machine learning model for traffic prediction,
- deploy the trained model using a Flask web application.

---

## Project Workflow

### 1. Data Analysis and Model Training
**`Traffic-Predication.ipynb`**
- Loading and exploring traffic datasets
- Feature engineering (date, time, vehicle counts)
- Training and evaluating machine learning models
- Selecting and saving the best-performing model

The trained model is saved as:
```

best_model.pkl

```

---

### 2. Application Layer
**`app.py`**
- Flask-based web application
- Loads the trained model using `joblib`
- Accepts input features via a POST request
- Returns traffic predictions in JSON format

Key features used by the model include:
- Date (converted to numerical representation)
- Vehicle counts (cars, bikes, buses, trucks)
- Total traffic count
- Time information (hour, minute)
- Day of the week

---

### 3. User Interface
- **`templates/`**: HTML templates for the web interface
- **`static/`**: Static assets (CSS, JS, images)

---

## Dataset

The raw datasets used in this project are **not included in the repository** due to size constraints.

Files used locally include:
- `Traffic.csv`
- `TrafficTwoMonth.csv`

To run the project, place the datasets in the project root or the appropriate local directory as expected by the notebook.

> The repository focuses on code, modeling, and deployment rather than dataset distribution.

---

## Repository Structure

```

04_traffic_prediction_flask/
│
├── static/
├── templates/
├── app.py
├── best_model.pkl          # Trained ML model (generated locally)
├── Traffic-Predication.ipynb
├── Traffic.csv             # Local dataset (not tracked in Git)
├── TrafficTwoMonth.csv     # Local dataset (not tracked in Git)
├── requirements.txt
└── README.md

````

---

## How to Run

### 1. Clone the repository
```bash
git clone git@github.com:tanzeelajvd/applied-ml-projects.git
cd applied-ml-projects/04_traffic_prediction_flask
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

### 4. Run the Flask application

```bash
python app.py
```

The application will be available at:

```
http://127.0.0.1:5000/
```

---

## API Usage (Prediction Endpoint)

**Endpoint**

```
POST /predict
```

**Request Format (JSON)**

```json
{
  "features": [
    "2024-01-15",
    120,
    45,
    10,
    8,
    183,
    14,
    30,
    "Monday"
  ]
}
```

**Response**

```json
{
  "prediction": [<predicted_value>]
}
```

---

## Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Flask
* Joblib
* Jupyter Notebook

---

## Key Learnings

* Feature engineering for time-series–like traffic data
* Training and persisting ML models
* Integrating ML models into Flask applications
* Designing simple ML inference APIs

---

## Disclaimer

This project is intended for **educational and demonstration purposes only**.
Predictions should not be used for real-world traffic control decisions.

---

## Author

**Tanzeela Javid**
Applied Machine Learning · Data Analysis · AI Systems
