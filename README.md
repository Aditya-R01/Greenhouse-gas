# 🌿 Supply Chain Emission Factors with Margins Predictor

Instant, AI-powered prediction and benchmarking of supply chain emission factors for sustainability analysis.  
Built with **machine learning** and an interactive **Streamlit** UI for effortless carbon footprint assessment.

**🌐 [Try the web app here!](https://emissionghg.streamlit.app/)**

## 🚀 Features

- **Interactive Interface:** User-friendly Streamlit web app for setting inputs, adjusting margins, and getting instant predictions.
- **AI-powered Predictions:** Uses trained ML models (XGBoost) for supply chain emission factor estimation.
- **Data Quality Scores:** Incorporate reliability, temporal, and technological quality for responsible benchmarking.
- **Sustainability Insights:** Focus on greenhouse gas emissions (e.g., carbon dioxide) by commodity, industry, unit, and source.

## 📑 How It Works

1. **Configure Inputs:**  
   - Select substance (e.g., carbon dioxide).
   - Choose unit, source, and data context.
   - Adjust margin and emission factor sliders.
2. **Set Data Quality Scores:**  
   - Reliability
   - Temporal correlation
   - Technological correlation
3. **Prediction:**  
   - The model predicts the emission factor based on your configuration.
   - Results display instantly below with context.

## 🛠️ Installation

### Requirements

- Python 3.7+
- Streamlit
- Pandas, NumPy, Scikit-learn, XGBoost, Joblib
- (Optional) Seaborn, Matplotlib, streamlit-lottie


## 📊 Data

- **Supply Chain Emissions dataset** (commodities and industries; CO2, CH₄, N₂O, and other GHGs)
- Units: `kg/2018 USD, purchaser price`
- Margin & emission factor benchmarking
- Data quality meta-scores per row

## 🏗️ Model Training

See `Notebook.ipynb` for:

- Data cleaning
- Feature engineering
- Model selection & training (XGBoost)
- Evaluation (RMSE, R², etc.)

## 👨‍💻 Author

**Aditya Raj**  
ECE Undergrad, Birla Institute of Technology, Mesra

## 🙏 Acknowledgements

- [US Input-Output Supply Chain Emission Factors Data]
- [Streamlit](https://streamlit.io)
- [Scikit-learn](https://scikit-learn.org/)
- [XGBoost](https://xgboost.readthedocs.io/)

## 📣 Contributing

Pull requests and suggestions welcome!  
Open an issue or contact the author for collaboration.

<!-- Badges, demo GIFs or links can be added here if available -->

**Built with dedication and data.**

