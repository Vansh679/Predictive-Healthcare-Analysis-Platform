Predictive Healthcare Analytics Platform & Population Insights Dashboard
An end-to-end machine learning platform and interactive clinical analytics dashboard for clinical risk assessment and diabetes prevalence tracking. Analyzes CDC Behavioral Risk Factor Surveillance System (BRFSS) data to predict patient-level diabetes risk using an ensemble ML pipeline and presents population-level health trends via interactive BI visual analytics.

Stack: Python, Pandas, NumPy, Scikit-learn, XGBoost, Imbalanced-learn (SMOTE), Streamlit, Power BI, DAX.

Project Structure
diabetes-health-analytics/
├── data/
│   ├── raw/                      # CDC BRFSS raw survey dataset
│   └── processed/                # Cleaned, encoded & transformed dataset
├── models/
│   ├── train_model.py            # Preprocessing pipeline & model training
│   ├── evaluate_model.py         # Confusion matrix, ROC-AUC & metrics calculation
│   └── saved_models/             # Exported model artifacts (.joblib / .pkl)
├── dashboard/
│   ├── app.py                    # Streamlit real-time patient risk calculator
│   └── components/               # Custom UI inputs, visual widgets & style logic
├── powerbi/
│   └── Population_Insights.pbix  # Multi-layer corporate Power BI report & DAX measures
├── .env.example                  # Environment configurations
├── requirements.txt              # Python dependencies
└── README.md
Running it Locally
1. Prerequisites
Ensure you have Python 3.10+ and Power BI Desktop (for viewing .pbix reports) installed.

2. Environment Setup & Dependencies
Clone the repository, set up a virtual environment, and install dependencies:

Bash
git clone https://github.com/Vansh679/diabetes-health-analytics.git
cd diabetes-health-analytics

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
3. Data Preprocessing & Model Training
Run the pipeline to clean the CDC dataset, handle class imbalances using SMOTE, and train ensemble architectures:

Bash
python models/train_model.py
This outputs optimized model artifacts directly to models/saved_models/.

4. Launch the Streamlit User Inference Application
Start the interactive real-time patient risk calculator:

Bash
streamlit run dashboard/app.py
Open http://localhost:8501 in your browser to interactively adjust patient health metrics and receive instant model inference risks.

How It Works
Data Engineering & Imbalance Handling: Preprocesses 20+ clinical and lifestyle variables (BMI, High Blood Pressure, Age, Physical Activity, General Health, etc.) from the CDC BRFSS dataset. Employs SMOTE (Synthetic Minority Over-sampling Technique) to resolve severe class imbalances between non-diabetic, pre-diabetic, and diabetic profiles.

Ensemble Architecture: Trains and evaluates high-performance Random Forest and XGBoost models, optimizing specifically for recall/sensitivity to minimize critical medical false negatives.

Real-Time Patient Risk Inference: The Streamlit frontend loads the pre-trained pipeline, exposing interactive sliders and toggles for clinical parameters. Upon evaluation, the app runs feature-vector inference and displays immediate risk categories (Healthy, Pre-Diabetic, High-Risk Diabetic) alongside probability confidence scores.

Population Health Visual Analytics: Power BI dashboards ingest model evaluation logs and demographic subsets to analyze macro-level health patterns. Includes custom DAX measures for model precision/recall metrics, population prevalence, and conditional risk heatmaps (e.g., Average BMI vs. General Health ratings).

Key Features
Real-Time Clinical Scoring: Web application calculates dynamic patient risk instantly from lifestyle and biomarker inputs.

Robust ML Pipeline: Fully reproducible feature selection, scaling, imbalance correction, and model serialization workflow.

Multi-Layer Corporate BI Dashboard: Interactive matrix drill-downs, line-trend analyses across age brackets, and cross-filtered sliceable risk reports.

Production-Ready Artifacts: Exported models serialized via joblib for modular deployment into production API environments.

Deploying a Live Demo
Streamlit Community Cloud (Free Hosting for Web UI)
Push your repository to GitHub.

Visit share.streamlit.io and connect your repository.

Set the main file path to dashboard/app.py and deploy.

Streamlit automatically manages dependencies from requirements.txt and hosts the live app at a public web URL.
