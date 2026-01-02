from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
model = joblib.load('best_model.pkl')  # Your trained model

@app.route('/')
def home():
    return render_template('index.html')

# import pandas as pd
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    raw = data['features']

    # Convert Date string to numeric (e.g., day of year)
    date_value = pd.to_datetime(raw[0])
    numeric_date = date_value.dayofyear  # or .timestamp(), or .weekday()

    feature_values = [
        numeric_date,             # Replaces raw[0]
        int(raw[1]),              # CarCount
        int(raw[2]),              # BikeCount
        int(raw[3]),              # BusCount
        int(raw[4]),              # TruckCount
        int(raw[5]),              # Total
        int(raw[6]),              # Hour
        int(raw[7]),              # Minute
        raw[8]                    # Day of the week (string)
    ]

    feature_names = [
        "Date", "CarCount", "BikeCount", "BusCount",
        "TruckCount", "Total", "Hour", "Minute", "Day of the week"
    ]

    df_input = pd.DataFrame([feature_values], columns=feature_names)
    prediction = model.predict(df_input)
    return jsonify({'prediction': prediction.tolist()})


if __name__ == '__main__':
    app.run(debug=True)
