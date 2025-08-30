# Orbitbit AI - Asteroid Risk Analysis

A comprehensive system for analyzing and predicting asteroid impact risks using NASA API data.

## Project Structure

- `data/`: Contains raw and processed asteroid data
- `notebooks/`: Jupyter notebooks for exploratory data analysis
- `src/`: Core Python source code
- `dashboard/`: Web application interface
- `models/`: Machine learning models
- `assets/`: Static assets and visualizations

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your NASA API key:
```bash
cp .env.example .env
# Edit .env with your NASA API key
```

## Running the Project

```bash
python src/main.py
```

## Dashboard

```bash
streamlit run dashboard/app.py
```
