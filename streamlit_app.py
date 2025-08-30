import plotly.express as px
import pandas as pd
import streamlit as st

df = pd.read_csv(r"E:\project ai\coding\src\asteroid_data.csv")

st.title("🪐 Realistic Asteroid Distance View")
st.markdown("This chart shows how close asteroids passed by Earth (center)")

fig = px.scatter(
    df,
    x="miss_distance_km",
    y="diameter_max_km",
    color="is_hazardous",
    size="diameter_max_km",
    hover_data=["name", "miss_distance_km", "diameter_max_km"],
    labels={"miss_distance_km": "Distance from Earth (km)", "diameter_max_km": "Max Diameter (km)"},
    title="🌍 Earth is at origin, Asteroids are placed based on miss distance"
)

fig.update_layout(
    xaxis_type="log",  # optional: use log scale if distance varies a lot
    yaxis_type="log",
    height=600,
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)
