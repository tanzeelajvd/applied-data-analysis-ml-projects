# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# from PIL import Image

# # Load models
# full_model = joblib.load("full_model.pkl")
# full_features = joblib.load("full_features.pkl")

# light_model = joblib.load("light_model.pkl")
# light_features = joblib.load("light_features.pkl")

# soil_cnn_model = load_model("soil_type_cnn_model.h5")
# soil_labels = ['Black Soil', 'Cinder Soil', 'Laterite Soil', 'Peat Soil', 'Yellow Soil']

# # Soil classification function
# def predict_soil_type(uploaded_file):
#     img = Image.open(uploaded_file).convert("RGB")
#     img = img.resize((128, 128))
#     img_array = image.img_to_array(img) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)
#     prediction = soil_cnn_model.predict(img_array)
#     return soil_labels[np.argmax(prediction)]

# def encode_soil_type(soil_type):
#     encoding = [0] * len(soil_labels)
#     if soil_type in soil_labels:
#         encoding[soil_labels.index(soil_type)] = 1
#     return dict(zip(soil_labels, encoding))

# # UI setup
# st.set_page_config(page_title="🌱 Soil Erosion Predictor", layout="wide")
# st.title("🌍 Soil Erosion Risk Analyzer")
# st.markdown("Get erosion category predictions using either a light model or a full model with manual entry and soil image classification.")

# tab1, tab2 = st.tabs(["🧮 Light Model (Manual)", "📋 Full Model (All Features + Image)"])

# # ========== LIGHT MODEL TAB ==========
# with tab1:
#     st.header("📝 Light Model Inputs")
#     with st.form("light_form"):
#         year = st.selectbox("📅 Year", [2020, 2021, 2022, 2023])
#         slope = st.slider("🛋️ Terrain Slope Angle", 0.0, 60.0, 10.0)
#         openness = st.slider("🌿 Terrain Openness", 0.0, 100.0, 20.0)
#         curvature_up = st.slider("📈 Upslope Curvature", -50.0, 50.0, 0.0)
#         curvature_down = st.slider("📉 Downslope Curvature", -50.0, 50.0, 0.0)
#         ndvi = st.slider("🌱 NDVI", 0.0, 1.0, 0.5)
#         red = st.slider("🔴 Red Reflectance", 0, 255, 100)
#         green = st.slider("🟢 Green Reflectance", 0, 255, 100)
#         blue = st.slider("🔵 Blue Reflectance", 0, 255, 100)
#         nir = st.slider("🌕 NIR Reflectance", 0, 255, 100)
#         temperature = st.slider("🌡️ Temperature (°C)", -20.0, 60.0, 25.0)
#         precipitation = st.slider("☔ Precipitation (mm)", 0, 3000, 1000)
#         lithology = st.slider("🪨 Lithology % (Unconsolidated Sediment)", 0.0, 100.0, 50.0)

#         uploaded_image = st.file_uploader("📸 Upload Soil Image (Optional)", type=["jpg", "jpeg", "png", "webp"])
#         manual_soil_type = st.selectbox("🌍 Or select soil type manually", ["Unknown"] + soil_labels)

#         submitted = st.form_submit_button("🔍 Predict")

#     if submitted:
#         if uploaded_image is not None:
#             predicted_soil = predict_soil_type(uploaded_image)
#             st.success(f"📷 Predicted Soil Type: **{predicted_soil}** (used for display only)")
#         elif manual_soil_type != "Unknown":
#             predicted_soil = manual_soil_type
#             st.info(f"🖐️ Using manually selected soil type: **{predicted_soil}** (used for display only)")
#         else:
#             st.warning("⚠️ Please provide soil type (image or manual).")
#             st.stop()

#         light_vector = [
#             year, slope, openness, curvature_up, curvature_down,
#             ndvi, red, green, blue, nir, temperature, precipitation, lithology
#         ]
#         input_light = pd.DataFrame([light_vector], columns=light_features)
#         input_light = input_light.reindex(columns=light_features, fill_value=0)

#         try:
#             prediction_light = light_model.predict(input_light)[0]
#             st.success(f"🌱 Light Model Erosion Prediction: **{prediction_light}**")
#         except Exception as e:
#             st.error(f"❌ Light Model Prediction failed: {e}")

# # ========== FULL MODEL TAB ==========
# with tab2:
#     st.header("📋 Full Feature Manual Input")

#     full_input = {}
#     with st.form("full_form"):
#         st.markdown("#### 🧮 Enter Feature Values:")

#         for feature in full_features:
#             if "year" in feature.lower():
#                 full_input[feature] = st.selectbox(f"📅 {feature}", [2020, 2021, 2022, 2023])
#             elif "curv" in feature or "slope" in feature or "openness" in feature or "precip" in feature or "temp" in feature:
#                 full_input[feature] = st.slider(f"📐 {feature}", -100.0, 100.0, 0.0)
#             elif "ndvi" in feature or "evi" in feature or "index" in feature:
#                 full_input[feature] = st.slider(f"🌿 {feature}", 0.0, 1.0, 0.5)
#             elif "reflectance" in feature or "red" in feature or "green" in feature or "blue" in feature or "nir" in feature:
#                 full_input[feature] = st.slider(f"🎨 {feature}", 0.0, 255.0, 100.0)
#             else:
#                 full_input[feature] = st.number_input(f"🔧 {feature}", value=0.0)

#         uploaded_image_full = st.file_uploader("📸 Upload Soil Image for Full Model", type=["jpg", "jpeg", "png", "webp"], key="full_image_input")
#         submitted_full = st.form_submit_button("🔍 Predict with Full Model")

#     if submitted_full:
#         if uploaded_image_full is not None:
#             predicted_soil = predict_soil_type(uploaded_image_full)
#             st.success(f"📷 Predicted Soil Type: **{predicted_soil}**")
#             full_input.update(encode_soil_type(predicted_soil))
#         else:
#             # If no image, default 0 to all soil encodings
#             full_input.update({label: 0 for label in soil_labels})

#         # Ensure all features present
#         for feature in full_features:
#             if feature not in full_input:
#                 full_input[feature] = 0

#         input_full = pd.DataFrame([full_input])
#         input_full = input_full.reindex(columns=full_features, fill_value=0)

#         try:
#             prediction = full_model.predict(input_full)[0]
#             st.success(f"✅ Full Model Erosion Prediction: **{prediction}**")
#         except Exception as e:
#             st.error(f"❌ Full Model Prediction failed: {e}")

# # ----------- Prompt / Recommendation -----------
# st.divider()
# st.markdown("### 🔮 Model Suggestions")
# st.info("""
# - This version lets you interact with all features manually (no CSV needed).
# - Soil type image classifier enriches the prediction with extra semantics.
# - Coming next: Auto-suggestion using Google Earth Engine.

# 📦 Let me know if you want a packaged app or deployment-ready version.
# """)




import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load models
full_model = joblib.load("full_model.pkl")
full_features = joblib.load("full_features.pkl")

light_model = joblib.load("light_model.pkl")
light_features = joblib.load("light_features.pkl")

soil_cnn_model = load_model("soil_type_cnn_model.h5")
soil_labels = ['Black Soil', 'Cinder Soil', 'Laterite Soil', 'Peat Soil', 'Yellow Soil']

# Category mapping for erosion prediction
erosion_labels = {
    0: "No Erosion",
    1: "Low Erosion",
    2: "Moderate Erosion",
    3: "High Erosion",
    4: "Severe Erosion"
}

# Soil classification function
def predict_soil_type(uploaded_file):
    img = Image.open(uploaded_file).convert("RGB")
    img = img.resize((128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = soil_cnn_model.predict(img_array)
    return soil_labels[np.argmax(prediction)]

def encode_soil_type(soil_type):
    encoding = [0] * len(soil_labels)
    if soil_type in soil_labels:
        encoding[soil_labels.index(soil_type)] = 1
    return dict(zip(soil_labels, encoding))

# UI setup
st.set_page_config(page_title="🌱 Soil Erosion Predictor", layout="wide")
st.title("🌍 Soil Erosion Risk Analyzer")
st.markdown("Get erosion category predictions using either a light model or a full model with manual entry and soil image classification.")

tab1, tab2 = st.tabs(["🧮 Light Model (Manual)", "📋 Full Model (All Features + Image)"])

# ========== LIGHT MODEL TAB ==========
with tab1:
    st.header("📝 Light Model Inputs")
    with st.form("light_form"):
        year = st.selectbox("📅 Year", [2020, 2021, 2022, 2023])
        slope = st.slider("🛋️ Terrain Slope Angle", 0.0, 60.0, 10.0)
        openness = st.slider("🌿 Terrain Openness", 0.0, 100.0, 20.0)
        curvature_up = st.slider("📈 Upslope Curvature", -50.0, 50.0, 0.0)
        curvature_down = st.slider("📉 Downslope Curvature", -50.0, 50.0, 0.0)
        ndvi = st.slider("🌱 NDVI", 0.0, 1.0, 0.5)
        red = st.slider("🔴 Red Reflectance", 0, 255, 100)
        green = st.slider("🟢 Green Reflectance", 0, 255, 100)
        blue = st.slider("🔵 Blue Reflectance", 0, 255, 100)
        nir = st.slider("🌕 NIR Reflectance", 0, 255, 100)
        temperature = st.slider("🌡️ Temperature (°C)", -20.0, 60.0, 25.0)
        precipitation = st.slider("☔ Precipitation (mm)", 0, 3000, 1000)
        lithology = st.slider("🪨 Lithology % (Unconsolidated Sediment)", 0.0, 100.0, 50.0)

        uploaded_image = st.file_uploader("📸 Upload Soil Image (Optional)", type=["jpg", "jpeg", "png", "webp"])
        manual_soil_type = st.selectbox("🌍 Or select soil type manually", ["Unknown"] + soil_labels)

        submitted = st.form_submit_button("🔍 Predict")

    if submitted:
        if uploaded_image is not None:
            predicted_soil = predict_soil_type(uploaded_image)
            st.success(f"📷 Predicted Soil Type: **{predicted_soil}** (used for display only)")
        elif manual_soil_type != "Unknown":
            predicted_soil = manual_soil_type
            st.info(f"🖐️ Using manually selected soil type: **{predicted_soil}** (used for display only)")
        else:
            st.warning("⚠️ Please provide soil type (image or manual).")
            st.stop()

        light_vector = [
            year, slope, openness, curvature_up, curvature_down,
            ndvi, red, green, blue, nir, temperature, precipitation, lithology
        ]
        input_light = pd.DataFrame([light_vector], columns=light_features)
        input_light = input_light.reindex(columns=light_features, fill_value=0)

        try:
            prediction_light = light_model.predict(input_light)[0]
            erosion_level = erosion_labels.get(prediction_light, "Unknown")
            st.success(f"🌱 Light Model Erosion Prediction: **{prediction_light} - {erosion_level}**")
        except Exception as e:
            st.error(f"❌ Light Model Prediction failed: {e}")

# ========== FULL MODEL TAB ==========
with tab2:
    st.header("📋 Full Feature Manual Input")

    full_input = {}
    with st.form("full_form"):
        st.markdown("#### 🧮 Enter Feature Values:")

        for feature in full_features:
            if "year" in feature.lower():
                full_input[feature] = st.selectbox(f"📅 {feature}", [2020, 2021, 2022, 2023])
            elif "curv" in feature or "slope" in feature or "openness" in feature or "precip" in feature or "temp" in feature:
                full_input[feature] = st.slider(f"📐 {feature}", -100.0, 100.0, 0.0)
            elif "ndvi" in feature or "evi" in feature or "index" in feature:
                full_input[feature] = st.slider(f"🌿 {feature}", 0.0, 1.0, 0.5)
            elif "reflectance" in feature or "red" in feature or "green" in feature or "blue" in feature or "nir" in feature:
                full_input[feature] = st.slider(f"🎨 {feature}", 0.0, 255.0, 100.0)
            else:
                full_input[feature] = st.number_input(f"🔧 {feature}", value=0.0)

        uploaded_image_full = st.file_uploader("📸 Upload Soil Image for Full Model", type=["jpg", "jpeg", "png", "webp"], key="full_image_input")
        submitted_full = st.form_submit_button("🔍 Predict with Full Model")

    if submitted_full:
        if uploaded_image_full is not None:
            predicted_soil = predict_soil_type(uploaded_image_full)
            st.success(f"📷 Predicted Soil Type: **{predicted_soil}**")
            full_input.update(encode_soil_type(predicted_soil))
        else:
            full_input.update({label: 0 for label in soil_labels})

        for feature in full_features:
            if feature not in full_input:
                full_input[feature] = 0

        input_full = pd.DataFrame([full_input])
        input_full = input_full.reindex(columns=full_features, fill_value=0)

        try:
            prediction = full_model.predict(input_full)[0]
            erosion_level = erosion_labels.get(prediction, "Unknown")
            st.success(f"✅ Full Model Erosion Prediction: **{prediction} - {erosion_level}**")
        except Exception as e:
            st.error(f"❌ Full Model Prediction failed: {e}")

# ----------- Prompt / Recommendation -----------
st.divider()
st.markdown("### 🔮 Model Suggestions")
st.info("""
- This version lets you interact with all features manually (no CSV needed).
- Soil type image classifier enriches the prediction with extra semantics.
- Erosion category is now interpreted as meaningful labels.
- Coming next: Auto-suggestion using Google Earth Engine.

📦 Let me know if you want a packaged app or deployment-ready version.
""")
