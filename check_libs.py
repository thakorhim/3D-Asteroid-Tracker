required_libs = {
    "requests": "requests",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
    "plotly": "plotly",
    "seaborn": "seaborn",
    "scikit-learn": "sklearn",        # ← FIX
    "streamlit": "streamlit",
    "python-dotenv": "dotenv"         # ← FIX
}

for pip_name, import_name in required_libs.items():
    try:
        __import__(import_name)
        print(f"✅ {pip_name} is installed")
    except ImportError:
        print(f"❌ {pip_name} is NOT installed")
