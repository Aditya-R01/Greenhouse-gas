import streamlit as st
import pandas as pd
import joblib
import time
import requests
from streamlit_lottie import st_lottie




# ---------- Model Loading ----------
@st.cache_resource(show_spinner=True)
def load_model():
    return joblib.load("xgb_model_compressed.pkl")

model = load_model()

# ---------- Page Config ----------
st.set_page_config(page_title="Emission Factor Studio", page_icon="🌿", layout="centered")

# ---------- Styling ----------
st.markdown(
    """
    <style>
        .stCard {
            background: #439ba8;
            border-radius: 12px;
            padding: 0.5em 1em;
            box-shadow: 0 3px 15px #d3e4fa44;
            margin-bottom: 1em;
            font-size: 2rem;
        }
        .stCardTitle {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 0.5em;
        }
        .main-title {
            font-size: 2rem;
            font-weight: 800;
            color: #2e7d32;
            text-align: center;
        }
        .progress-text {
            text-align: center;
            font-size: 0.9rem;
            margin-top: -10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- UI Header ----------
st.markdown('<div class="main-title">🌿 Supply Chain Emission Factors with Margins Predictor</div>', unsafe_allow_html=True)
st.markdown('<div style="Text-align:center">Instant prediction powered by machine learning for sustainability benchmarking.</div>',unsafe_allow_html=True)

st.divider()

# ---------- Card-Based Input Section ----------
st.markdown('<div class="stCard" style="Text-align:center"> Configure Inputs', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

# Encoders
substance_map = {'carbon dioxide': 0, 'methane': 1, 'nitrous oxide': 2, 'other GHGs': 3}
unit_map = {'kg/2018 USD, purchaser price': 1, 'kg CO2e/2018 USD, purchaser price': 0}
source_map = {'Commodity': 0, 'Industry': 1}

with col1:
    st.markdown('<div class="stCardTitle">Substance</div>', unsafe_allow_html=True)
    substance = st.selectbox('Select Substance', list(substance_map.keys()) , label_visibility="hidden")
    st.caption('🧪 Type of greenhouse gas')

with col2:
    st.markdown('<div class="stCardTitle">Unit & Source</div>', unsafe_allow_html=True)
    unit = st.selectbox('Unit', list(unit_map.keys()))
    source = st.selectbox('Source', list(source_map.keys()))
    st.caption('📦 Price unit & emission data context')

with col3:
    st.markdown('<div class="stCardTitle">Margins & Factor</div>', unsafe_allow_html=True)
    margins = st.slider('Margins (0–10)', 0.0, 10.0, 0.0, step=0.001)
    scf = st.slider('Emission Factor (0–10)', 0.0, 10.0, 0.0, step=0.001)
    st.caption('🎯 Current and target values')
st.markdown('</div>', unsafe_allow_html=True)
st.divider()

# ---------- Data Quality Card ----------
st.markdown('<div class="stCard" style="Text-align:center">Data Quality Scores', unsafe_allow_html=True)
dq_col1, dq_col2, dq_col3 = st.columns(3)
with dq_col1:
    dq_reliability = st.number_input("Reliability (1–5)", 1, 5, 3)
with dq_col2:
    dq_temporal = st.number_input("Temporal Corr. (1–5)", 1, 5, 3)
with dq_col3:
    dq_technological = st.number_input("Technological Corr. (1–5)", 1, 5, 3)
st.markdown('</div>', unsafe_allow_html=True)
st.divider()

# ---------- Prepare Model Input ----------
input_dict = {
    "Substance": [substance_map[substance]],
    "Unit": [unit_map[unit]],
    "Supply Chain Emission Factors without Margins": [scf],
    "Margins of Supply Chain Emission Factors": [margins],
    "DQ ReliabilityScore of Factors without Margins": [dq_reliability],
    "DQ TemporalCorrelation of Factors without Margins": [dq_temporal],
    "DQ GeographicalCorrelation of Factors without Margins": [1],
    "DQ TechnologicalCorrelation of Factors without Margins": [dq_technological],
    "DQ DataCollection of Factors without Margins": [1],
    "Source": [source_map[source]]
}
X_input = pd.DataFrame(input_dict)

# ---------- Predict Button & Animation ----------
predict_btn = st.button("✨ Predict Emission Factor")
if predict_btn:
    with st.spinner("Calculating emission factor..."):
        time.sleep(1.2)  # simulate model delay
        y_pred = model.predict(X_input)[0]
        percent_green = max(0, min(100, int((10 - y_pred) * 10)))

    # Output Card
    st.markdown('<div class="stCard" style="text-align: center;">Result', unsafe_allow_html=True)
    if y_pred <= 3:
        st.success(f"**Green Supply Chain! Predicted Factor:** {y_pred:.4f}")
    elif y_pred <= 7:
        st.info(f"**Moderate! Predicted Factor:** {y_pred:.4f}")
    else:
        st.warning(f"⚡ **Warning: High Emissions! Predicted Factor:** {y_pred:.4f}")
    st.caption("Unit: as selected above.")
    st.progress(percent_green)
    st.markdown(f'<div class="progress-text">Greenness Scale: {percent_green}%</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown(
        '<div class="stCard" style="text-align: center;">🔎 Fill the inputs and Click Predict to see results.</div>',
        unsafe_allow_html=True
    )
st.markdown("""
<hr>
<div style="text-align:center; padding-top: 20px;">
    <p style="font-size: 1.1em; color: #555;">
        Built with dedication and data by <strong>Aditya Raj</strong> 🚀
    </p>
    <p style="font-size: 0.9em; color: #777;">
        An ECE Undergrad from Birla Institute of Technology, Mesra.
    </p>
    <p style="font-size: 1.0em; margin-top: 15px;">
        <a href="https://www.linkedin.com/in/adityaraj-bit/" target="_blank" style="text-decoration: none; color: #0077B5; margin: 0 10px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/480px-LinkedIn_logo_initials.png" width="20" height="20" style="vertical-align: middle;"> LinkedIn
        </a> |
        <a href="https://www.instagram.com/adityar_a_j_?igsh=MTZicm1qejZmMWg4MQ==/" target="_blank" style="text-decoration: none; color: #C13584; margin: 0 10px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/768px-Instagram_logo_2016.svg.png" width="20" height="20" style="vertical-align: middle;"> Instagram
        </a> |
        <a href="https://aditya-r01.github.io/Portfolio-website/" target="_blank" style="text-decoration: none; color: white; margin: 0 10px;">
            <img src="https://e7.pngegg.com/pngimages/875/395/png-clipart-internet-internet-security-earth-blue-globe-thumbnail.png" width="20" height="20" style="vertical-align: middle;"> My Portfolio
        </a> |
        <a href="https://github.com/Aditya-R01/Predicting-Supply-Chain-Emission-Factors-with-Margins" target="_blank" style="text-decoration: none; color: white; margin: 0 10px;">
            <img src="https://icones.pro/wp-content/uploads/2021/06/icone-github-orange.png" width="20" height="20" style="vertical-align: middle;"> View in GitHub
        </a>
    </p>
</div>
""", unsafe_allow_html=True)

