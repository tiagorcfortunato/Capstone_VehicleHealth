# Vehicle Health Monitor & Fault Predictor 🚗🛠️

This project was developed as part of the Capstone for the Master's in Software Engineering at the University of Europe. The goal was to simulate an intelligent vehicle health monitoring system that can predict failures using sensor data and machine learning.

---

## 🧠 Objective

Develop a system capable of:

- Analyzing sensor data from vehicles (e.g., engine temperature, vibration, oil pressure, RPM, speed)
- Detecting abnormal patterns related to failures
- Predicting failures in advance using Machine Learning (Random Forest)
- Displaying the results interactively through a dashboard built with Streamlit

---

## 🧱 Project Structure

The project is structured into 4 notebooks and 1 dashboard script:

> - Os notebooks cobrem desde a geração dos dados até a modelagem e avaliação.
> - O script Python final (`Capstone_05_Dashboard_Streamlit.py`) implementa o dashboard interativo com Streamlit.


```
Capstone_VehicleHealth/
│
├── data/                      # Dataset simulado
│   └── vehicle_sensor_data.csv
│
├── notebooks/                 # Notebooks organizados por etapa
│   ├── Capstone_01_Simulated_Dataset.ipynb
│   ├── Capstone_02_ETL_and_EDA.ipynb
│   ├── Capstone_03_Machine_Learning.ipynb
│   └── Capstone_04_Reporting_Results.ipynb
│
├── dashboard/                 # Dashboard interativo em Streamlit
│   └── Capstone_05_Dashboard_Streamlit.py
│
├── assets/                    # Recursos visuais
│   └── imgs/                  # (imagens futuras, logos, gráficos, etc.)
│
├── requirements.txt           # Bibliotecas e dependências
└── README.md                  # Este arquivo
```
---
📊 Dataset Description

The dataset `vehicle_sensor_data.csv` contains the following simulated features:

- `engine_temp`: Engine temperature (°C)
- `vibration`: Vibration intensity (g)
- `oil_pressure`: Oil pressure (bar)
- `rpm`: Revolutions per minute
- `speed`: Vehicle speed (km/h)
- `failure`: Binary target (1 = failure, 0 = normal)

## 📊 Results

The developed system allows monitoring the condition of a vehicle in real time and predicting potential failures in advance, increasing reliability and vehicle safety.

## 📈 Visual Results

Below are some example outputs from the dashboard developed with Streamlit:

### 📊 General Statistics
<p align="center">
  <img src="assets/imgs/dashboard_stats.png" width="600"/>
</p>

### 📉 Distributions
<p align="center">
  <img src="assets/imgs/dashboard_distributions.png" width="600"/>
</p>

### 🔗 Correlation Matrix
<p align="center">
  <img src="assets/imgs/dashboard_corr_matrix.png" width="600"/>
</p>

<p align="center">
  <a href="https://capstonevehiclehealth.streamlit.app">
    <img src="https://img.shields.io/badge/Dashboard%20Online-Streamlit-blue?style=for-the-badge&logo=streamlit" alt="Streamlit App">
  </a>
</p>

## 📊 Dashboard Preview

- [🔗 Streamlit App (Live Demo)](https://capstonevehiclehealth.streamlit.app)
- [📄 Dashboard Report (PDF)](assets/dashboard_resultados.pdf)

---

## 📈 Key Results

- Accuracy: **99.9%**
- Precision & Recall: **1.00 for 'Normal'**, **0.86 for 'Failure'**
- Only **1 false negative** in the test set
- Highly imbalanced data handled using `class_weight='balanced'` in the model

---
🛠️ Future Improvements

- Experiment with additional ML models (e.g., XGBoost, SVM)
- Include real-world sensor datasets (e.g., from UCI or Kaggle)
- Add time-series analysis for failure prediction
- Improve dashboard interactivity with Streamlit widgets
- Deploy dashboard using Streamlit Cloud (already done ✅)

## 🚀 How to Run the Project

1. Clone this repository:
   ```bash
   git clone https://github.com/tiagorcfortunato/Capstone_VehicleHealth.git
   cd Capstone_VehicleHealth

2. Install dependencies 
pip install -r requirements.txt

3. Run the notebooks step-by-step (data, ETL, ML, reporting)

4. Launch the dashboard:
streamlit run dashboard/Capstone_05_Dashboard_Streamlit.py

🛠️ Technologies Used

Python
Pandas, NumPy, scikit-learn, seaborn, matplotlib
Streamlit (dashboard)
Git & GitHub


👨‍💻 Author

Tiago Fortunato
Software Engineering Student | Mechanical Engineer
-
🔗 LinkedIn: www.linkedin.com/in/tiagorcfortunato
-
🔗 GitHub: https://github.com/tiagorcfortunato
-

















