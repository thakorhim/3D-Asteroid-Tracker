import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ----------------------------------
# Page setup
# ----------------------------------
st.set_page_config(page_title="🪐 All Near-Earth Asteroids Viewer", layout="wide")
st.title("🌍 All Near-Earth Asteroids 3D Tracker")
st.markdown("This 3D simulation shows all asteroids from the dataset near Earth.")

# ----------------------------------
# Load asteroid data
# ----------------------------------
df = pd.read_csv("asteroid_data.csv")  # path adjust as needed

# ----------------------------------
# Check data
# ----------------------------------
if df.empty:
    st.warning("CSV file is empty or not loaded properly.")
else:
    st.success(f"Total asteroids found: {len(df)}")

    # Display table (optional)
    columns_to_show = ['name', 'close_approach_date']
    if 'miss_distance_km' in df.columns:
        columns_to_show.append('miss_distance_km')
    if 'velocity_kmph' in df.columns:
        columns_to_show.append('velocity_kmph')

    st.dataframe(df[columns_to_show], use_container_width=True)

    # ----------------------------------
    # Prepare 3D plot
    # ----------------------------------
    fig = go.Figure()

    # Earth at center
    fig.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[0],
        mode='markers+text',
        marker=dict(size=12, color='blue'),
        name='🌍 Earth',
        text=["Earth"],
        textposition="bottom center"
    ))

    df = df.reset_index(drop=True)

    # Plot each asteroid
    for idx, row in df.iterrows():
        try:
            distance_km = float(row['miss_distance_km'])
        except:
            continue  # skip if invalid distance

        distance_million_km = distance_km / 1_000_000
        angle = idx * (360 / len(df))

        x = distance_million_km * np.cos(np.radians(angle))
        y = distance_million_km * np.sin(np.radians(angle))
        z = np.random.uniform(-5, 5)

        fig.add_trace(go.Scatter3d(
            x=[x], y=[y], z=[z],
            mode='markers+text',
            marker=dict(size=6, color='orange'),
            name=row['name'],
            text=[f"{row['name']}<br>{round(distance_million_km, 2)} M km"],
            textposition="top center"
        ))

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            aspectmode='data',
        ),
        height=700,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

    # ----------------------------------
    # Optional: Image display
    # ----------------------------------
    st.subheader("🌌 Visual Representation")
    col1, col2 = st.columns(2)
    with col1:
        st.image("earth.jpg", caption="Earth", use_column_width=True)
    with col2:
        st.image("asteroid.jpg", caption="Asteroid", use_column_width=True)
