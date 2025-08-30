#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run the main pipeline
python src/main.py

# Start the dashboard
streamlit run dashboard/app.py
