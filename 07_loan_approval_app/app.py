# 📱 Streamlit Loan Default Prediction App with SHAP

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt

# Load trained model and preprocessor
model = joblib.load("final_stacked_model.pkl")
preprocessor = joblib.load("preprocessing_pipeline_pca.pkl")

st.set_page_config(page_title="Loan Default Predictor", layout="centered")
st.title("🏦 Loan Default Risk Predictor")

st.markdown("""
This app predicts the risk of a customer defaulting on a loan based on their demographic and financial information.
""")

# ✅ Validation function

def validate_input_features(input_df, preprocessor, model):
    expected_raw = list(preprocessor.feature_names_in_)
    provided_raw = list(input_df.columns)
    missing = set(expected_raw) - set(provided_raw)
    extra = set(provided_raw) - set(expected_raw)

    if missing:
        st.warning(f"⚠️ Missing required features: {missing}")
    if extra:
        st.warning(f"⚠️ Unexpected extra features: {extra}")

    if missing or extra:
        raise ValueError("Input feature mismatch. Prediction aborted.")

    processed = preprocessor.transform(input_df)
    if processed.shape[1] != model.n_features_in_:
        raise ValueError(
            f"❌ Feature mismatch after preprocessing. "
            f"Model expects {model.n_features_in_} features, but got {processed.shape[1]}"
        )

    st.success("✅ Input features validated successfully.")
    return processed

# Example input fields (you can add more based on your actual feature set)
with st.form("input_form"):
    gender = st.selectbox("Gender", ["M", "F"])
    own_car = st.selectbox("Owns a car?", ["Y", "N"])
    income_total = st.number_input("Annual Income", min_value=1000, step=500)
    credit_amount = st.number_input("Loan Amount Requested", min_value=1000, step=500)
    annuity = st.number_input("Monthly Annuity Amount", min_value=0.0, step=100.0)
    days_birth = st.number_input("Customer Age (in days, negative)", value=-12000)
    days_employed = st.number_input("Days Employed (negative, or 365243 for not employed)", value=-2000)
    children = st.number_input("Number of Children", min_value=0, step=1)
    family_members = st.number_input("Family Members Count", min_value=1, step=1)
    education = st.selectbox("Education", ["Secondary / secondary special", "Higher education", "Incomplete higher", "Lower secondary"])
    housing_type = st.selectbox("Housing Type", ["House / apartment", "With parents", "Rented apartment", "Municipal apartment"])
    submit = st.form_submit_button("Predict")

# Prepare the input
if submit:
    input_dict = {
        'CODE_GENDER': gender,
        'FLAG_OWN_CAR': own_car,
        'AMT_INCOME_TOTAL': income_total,
        'AMT_CREDIT': credit_amount,
        'AMT_ANNUITY': annuity,
        'DAYS_BIRTH': days_birth,
        'DAYS_EMPLOYED': days_employed,
        'CNT_CHILDREN': children,
        'CNT_FAM_MEMBERS': family_members,
        'NAME_EDUCATION_TYPE': education,
        'NAME_HOUSING_TYPE': housing_type
    }

    input_df = pd.DataFrame([input_dict])

    try:
        processed_input = validate_input_features(input_df, preprocessor, model)
        prediction = model.predict(processed_input)[0]
        proba = model.predict_proba(processed_input)[0][1]

        st.subheader("📊 Prediction Result")
        if prediction == 1:
            st.error(f"🚨 High Risk of Default: {proba:.2%} chance")
        else:
            st.success(f"✅ Low Risk of Default: {proba:.2%} chance")

        # SHAP explanation
        st.subheader("🔍 Feature Contribution (SHAP Explanation)")
        explainer = shap.Explainer(model)
        shap_values = explainer(processed_input)

        # Plot SHAP values
        fig, ax = plt.subplots(figsize=(10, 1))
        shap.plots.waterfall(shap_values[0], max_display=10, show=False)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")

