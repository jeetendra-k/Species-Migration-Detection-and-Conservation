import streamlit as st
import pandas as pd
import pydeck as pdk
import matplotlib.pyplot as plt
import numpy as np

from models.predict import predict_population, predict_migration_path
from ai.explanation import generate_detailed_explanation
from utils.preprocessing import habitat_score

# -----------------------------
# Species Selection
# -----------------------------

species = st.sidebar.selectbox(
    "Select Species",
    [
        "Elephant",
        "Flamingos(aerial)",
        "barheaded goose(aerial)",
        "sarus crane(aerial)",
        "steppe eagle(aerial)",
        "Bengal Tiger",
        "Rhinoceros",
        "Sambar Deer",
        "asian elephant",
        "barasingha",
        "chital",
        "gaur",
        "golden jackal",
        "indian wolf",
        "macaque",
        "rhinoceros",
        "wild boar",
        "Sloth Bear",


        "indian leopard (land)",
        "asiatic lion (land)",
        "sloth bear (land)",
        "wild water buffalo (land)",
        "blackbuck (land)",
        "hog deer (land)",
        "barking deer (land)",
        "mouse deer (land)",
        "dhole (land)",
        "striped hyena (land)",
        "indian fox (land)",
        "desert fox (land)",
        "jungle cat (land)",
        "fishing cat (land)",
        "rusty-spotted cat (land)",
        "caracal (land)",
        "clouded leopard (land)",
        "snow leopard (land)",
        "red panda (land)",
        "himalayan black bear (land)",
        "brown bear (land)",
        "indian rhinoceros (land)",
        "indian pangolin (land)",
        "small indian civet (land)",
        "large indian civet (land)",
        "common palm civet (land)",
        "smooth-coated otter (land)",
        "indian hare (land)",
        "porcupine (land)",
        "indian giant squirrel (land)",
        "bonnet macaque (land)",
        "rhesus macaque (land)",
        "lion-tailed macaque (land)",
        "nilgiri langur (land)",
        "hanuman langur (land)",
        "capped langur (land)",
        "hoolock gibbon (land)",
        "indian muntjac (land)",
        "four-horned antelope (land)",
        "serow (land)",
        "himalayan tahr (land)",
        "bar-headed goose (aerial)",
        "sarus crane (aerial)",
        "demoiselle crane (aerial)",
        "greater flamingo (aerial)",
        "lesser flamingo (aerial)",
        "painted stork (aerial)",
        "asian openbill (aerial)",
        "black-necked stork (aerial)",
        "woolly-necked stork (aerial)",
        "spot-billed pelican (aerial)",
        "great white pelican (aerial)",
        "oriental darter (aerial)",
        "little cormorant (aerial)",
        "indian cormorant (aerial)",
        "grey heron (aerial)",
        "purple heron (aerial)",
        "pond heron (aerial)",
        "cattle egret (aerial)",
        "great egret (aerial)",
        "little egret (aerial)",
        "black kite (aerial)",
        "brahminy kite (aerial)",
        "steppe eagle (aerial)",
        "indian spotted eagle (aerial)",
        "crested serpent eagle (aerial)",
        "changeable hawk eagle (aerial)",
        "shikra (aerial)",
        "peregrine falcon (aerial)",
        "laggar falcon (aerial)",
        "common kestrel (aerial)",
        "barn owl (aerial)",
        "indian eagle owl (aerial)",
        "brown fish owl (aerial)",
        "rose-ringed parakeet (aerial)",
        "alexandrine parakeet (aerial)",
        "plum-headed parakeet (aerial)",
        "indian peafowl (aerial)",
        "grey junglefowl (aerial)",
        "red junglefowl (aerial)",
        "indian roller (aerial)",
        "white-throated kingfisher (aerial)",
        "stork-billed kingfisher (aerial)",
        "common kingfisher (aerial)",
        "green bee-eater (aerial)",
        "indian pitta (aerial)",
        "common myna (aerial)",
        "jungle myna (aerial)",
        "house crow (aerial)",
        "large-billed crow (aerial)",
        "others"
    ]
)


file_map = {
    "Elephant": "elephant_clustered.csv",
    "Flamingos(aerial)": "flamingos_clustered.csv",
    "Bengal Tiger": "tiger_clustered.csv",
    "Sloth Bear": "slothbear_clustered.csv",
    "Rhinoceros": "rhinoceros_clustered.csv",
    "Sambar Deer": "sambardeer_clustered.csv",
    "asian elephant": "asianelephants_clustered.csv",
    "barasingha": "barasingha_clustered.csv",
    "chital": "chital_clustered.csv",
    "gaur": "gaur_clustered.csv",
    "golden jackal": "goldenjackal_clustered.csv",
    "indian wolf": "indianwolf_clustered.csv",
    "macaque": "macaque_clustered.csv",
    "rhinoceros": "rhinoceros_clustered.csv",
    "wild boar": "wildboar_clustered.csv",
    "barheaded goose(aerial)": "barheadedgoose_clustered.csv",
    "sarus crane(aerial)": "saruscrane_clustered.csv",
    "steppe eagle(aerial)": "steppeeagle_clustered.csv",


    "indian leopard (land)": "general_clustered.csv",
    "asiatic lion (land)": "general_clustered.csv",
    "sloth bear (land)": "general_clustered.csv",

    "wild water buffalo (land)": "general_clustered.csv",
   
    "blackbuck (land)": "general_clustered.csv",
    
    "hog deer (land)": "general_clustered.csv",
    "barking deer (land)": "general_clustered.csv",
    "mouse deer (land)": "general_clustered.csv",
 
    "dhole (land)": "general_clustered.csv",
    "striped hyena (land)": "general_clustered.csv",
    "indian fox (land)": "general_clustered.csv",
    "desert fox (land)": "general_clustered.csv",
    "jungle cat (land)": "general_clustered.csv",
    "fishing cat (land)": "general_clustered.csv",
    "rusty-spotted cat (land)": "general_clustered.csv",
    "caracal (land)": "general_clustered.csv",
    "clouded leopard (land)": "general_clustered.csv",
    "snow leopard (land)": "general_clustered.csv",
    "red panda (land)": "general_clustered.csv",
    "himalayan black bear (land)": "general_clustered.csv",
    "brown bear (land)": "general_clustered.csv",
    "indian rhinoceros (land)": "general_clustered.csv",
    "indian pangolin (land)": "general_clustered.csv",
    "small indian civet (land)": "general_clustered.csv",
    "large indian civet (land)": "general_clustered.csv",
    "common palm civet (land)": "general_clustered.csv",
    "smooth-coated otter (land)": "general_clustered.csv",
    "indian hare (land)": "general_clustered.csv",
    "porcupine (land)": "general_clustered.csv",
    "indian giant squirrel (land)": "general_clustered.csv",
    "bonnet macaque (land)": "general_clustered.csv",
    "rhesus macaque (land)": "general_clustered.csv",
    "lion-tailed macaque (land)": "general_clustered.csv",
    "nilgiri langur (land)": "general_clustered.csv",
    "hanuman langur (land)": "general_clustered.csv",
    "capped langur (land)": "general_clustered.csv",
    "hoolock gibbon (land)": "general_clustered.csv",
    "indian muntjac (land)": "general_clustered.csv",
    "four-horned antelope (land)": "general_clustered.csv",
    "serow (land)": "general_clustered.csv",
    "himalayan tahr (land)": "general_clustered.csv",

    "bar-headed goose (aerial)": "general_clustered.csv",
    "sarus crane (aerial)": "general_clustered.csv",
    "demoiselle crane (aerial)": "general_clustered.csv",
    "greater flamingo (aerial)": "general_clustered.csv",
    "lesser flamingo (aerial)": "general_clustered.csv",
    "painted stork (aerial)": "general_clustered.csv",
    "asian openbill (aerial)": "general_clustered.csv",
    "black-necked stork (aerial)": "general_clustered.csv",
    "woolly-necked stork (aerial)": "general_clustered.csv",
    "spot-billed pelican (aerial)": "general_clustered.csv",
    "great white pelican (aerial)": "general_clustered.csv",
    "oriental darter (aerial)": "general_clustered.csv",
    "little cormorant (aerial)": "general_clustered.csv",
    "indian cormorant (aerial)": "general_clustered.csv",
    "grey heron (aerial)": "general_clustered.csv",
    "purple heron (aerial)": "general_clustered.csv",
    "pond heron (aerial)": "general_clustered.csv",
    "cattle egret (aerial)": "general_clustered.csv",
    "great egret (aerial)": "general_clustered.csv",
    "little egret (aerial)": "general_clustered.csv",
    "black kite (aerial)": "general_clustered.csv",
    "brahminy kite (aerial)": "general_clustered.csv",
    "steppe eagle (aerial)": "general_clustered.csv",
    "indian spotted eagle (aerial)": "general_clustered.csv",
    "crested serpent eagle (aerial)": "general_clustered.csv",
    "changeable hawk eagle (aerial)": "general_clustered.csv",
    "shikra (aerial)": "general_clustered.csv",
    "peregrine falcon (aerial)": "general_clustered.csv",
    "laggar falcon (aerial)": "general_clustered.csv",
    "common kestrel (aerial)": "general_clustered.csv",
    "barn owl (aerial)": "general_clustered.csv",
    "indian eagle owl (aerial)": "general_clustered.csv",
    "brown fish owl (aerial)": "general_clustered.csv",
    "rose-ringed parakeet (aerial)": "general_clustered.csv",
    "alexandrine parakeet (aerial)": "general_clustered.csv",
    "plum-headed parakeet (aerial)": "general_clustered.csv",
    "indian peafowl (aerial)": "general_clustered.csv",
    "grey junglefowl (aerial)": "general_clustered.csv",
    "red junglefowl (aerial)": "general_clustered.csv",
    "indian roller (aerial)": "general_clustered.csv",
    "white-throated kingfisher (aerial)": "general_clustered.csv",
    "stork-billed kingfisher (aerial)": "general_clustered.csv",
    "common kingfisher (aerial)": "general_clustered.csv",
    "green bee-eater (aerial)": "general_clustered.csv",
    "indian pitta (aerial)": "general_clustered.csv",
    "common myna (aerial)": "general_clustered.csv",
    "jungle myna (aerial)": "general_clustered.csv",
    "house crow (aerial)": "general_clustered.csv",
    "large-billed crow (aerial)": "general_clustered.csv",
    "others": "general_clustered.csv"

}

# -----------------------------
# Title
# -----------------------------

st.title(f"{species} Habitat & Migration Analysis 🌍")

# -----------------------------
# Load Dataset
# -----------------------------

clustered_data = pd.read_csv(
    f"data/processed/{file_map[species]}"
)

import numpy as np

# Simulate environmental data
clustered_data["temperature"] = np.random.uniform(25, 35, len(clustered_data))
clustered_data["rainfall"] = np.random.uniform(800, 1400, len(clustered_data))
clustered_data["ndvi"] = np.random.uniform(0.2, 0.6, len(clustered_data))
clustered_data["population"] = np.random.randint(1000, 2000, len(clustered_data))

# Sidebar filters
st.sidebar.header("Filters")
year = st.sidebar.slider(
    "Select Year",
    int(clustered_data.year.min()),
    int(clustered_data.year.max()),
    int(clustered_data.year.max())
)

filtered_data = clustered_data[clustered_data["year"] <= year]

# ==============================
# POPULATION TREND
# ==============================

# --- Smooth population trend ---
st.subheader("Population Trend")

yearly = filtered_data.groupby("year")["population"].mean().reset_index()

# Rolling average (smoothing)
yearly["smoothed"] = yearly["population"].rolling(window=3, min_periods=1).mean()

st.line_chart(yearly.set_index("year")[["smoothed"]])

# ==============================
# ENVIRONMENTAL FACTORS
# ==============================

st.subheader("Environmental Changes")

env = filtered_data.groupby("year")[["temperature", "rainfall", "ndvi"]].mean().reset_index()

# Smooth
env["temperature"] = env["temperature"].rolling(3, min_periods=1).mean()
env["rainfall"] = env["rainfall"].rolling(3, min_periods=1).mean()
env["ndvi"] = env["ndvi"].rolling(3, min_periods=1).mean()

st.line_chart(env.set_index("year"))
# ==============================
# FUTURE PREDICTION (ML)
# ==============================

st.subheader("Future Predictions (2025–2030)")

future_years = list(range(2025, 2031))
future_preds = []

temp_future = clustered_data["temperature"].iloc[-1]
rain_future = clustered_data["rainfall"].iloc[-1]
ndvi_future = clustered_data["ndvi"].iloc[-1]

for year in future_years:
    pred = predict_population(temp_future, rain_future, ndvi_future, "hybrid")
    future_preds.append(pred)

    temp_future += 1.0
    rain_future -= 50
    ndvi_future -= 0.02

future_df = pd.DataFrame({
    "year": future_years,
    "predicted_population": future_preds
})

st.line_chart(future_df.set_index("year"))

# ==============================
# LSTM PREDICTION
# ==============================

# --- USER INPUT ---
st.subheader("Environmental Inputs")

temp = st.slider("Temperature", 20, 45, 30)
rain = st.slider("Rainfall", 500, 1500, 1000)
ndvi = st.slider("NDVI", 0.1, 0.6, 0.3)
# ==============================
# MIGRATION PATH
# ==============================

# st.subheader("Predicted Migration (Herd Simulation)")

# # --- Ensure sliders exist ABOVE this ---
# # temp, rain, ndvi must be defined earlier

# sampled = filtered_data.sample(min(10, len(filtered_data)), random_state=42)

# all_points = []

# for i, row in sampled.iterrows():

#     path = predict_migration_path(
#         row["latitude"],
#         row["longitude"],
#         temp,
#         rain,
#         ndvi
#     )

#     for lat, lon in path:
#         all_points.append({
#             "lat": lat,
#             "lon": lon,
#             "herd": i
#         })

# path_df = pd.DataFrame(all_points)

# st.map(path_df)

# ==============================
# HEATMAP
# ==============================

st.subheader("Migration Heatmap")

heatmap = pdk.Layer(
    "HeatmapLayer",
    data=filtered_data,
    get_position='[longitude, latitude]',
    radiusPixels=40,
)

view_state = pdk.ViewState(
    latitude=filtered_data["latitude"].mean(),
    longitude=filtered_data["longitude"].mean(),
    zoom=4,
)

st.pydeck_chart(pdk.Deck(layers=[heatmap], initial_view_state=view_state))
# ==============================
# MANUAL PREDICTION
# ==============================



if st.button("Predict"):
    prediction = predict_population(temp, rain, ndvi)
    st.success(f"Predicted {species} Population: {prediction}")

# ==============================
# MODEL COMPARISON
# ==============================

st.subheader("Model Comparison")

models = ["Linear Regression", "Random Forest"]
rmse_values = [60, 25]  # slightly realistic placeholder

fig, ax = plt.subplots()
ax.bar(models, rmse_values)
ax.set_ylabel("RMSE (Lower is Better)")
st.pyplot(fig)

# ==============================
# AI EXPLANATION
# ==============================

st.subheader("AI Explanation")

exp = generate_detailed_explanation(temp, rain, ndvi, 1500)
st.text_area("AI Explanation", exp, height=500)
# ==============================
# HABITAT SCORE (SDM)
# ==============================

st.subheader("Habitat Suitability Score")

score = habitat_score(temp_future, rain_future, ndvi_future)
st.metric("Suitability Score", score)

# ==============================
# DATA TABLE
# ==============================

st.subheader("Data")
st.write(filtered_data)

# animation

import time

st.subheader("Animated Herd Migration 🎬")

# Controls
steps = st.slider("Simulation Steps", 3, 15, 6)
speed = st.slider("Animation Speed", 0.2, 2.0, 0.8)

run_sim = st.button("Run Simulation ▶️")

colors = [
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255],
    [255, 165, 0],
    [128, 0, 128]
]

if run_sim:

    herd_positions = {}
    trail_history = {}
    initial_positions = {}

    for group in clustered_data["group"].unique():

        group_data = clustered_data[
            clustered_data["group"] == group
        ]

        sample = group_data.sample(
            min(5, len(group_data)),
            random_state=42
        )

        herd_positions[group] = []
        initial_positions[group] = []

        for _, row in sample.iterrows():

            pos = [row["latitude"], row["longitude"]]

            herd_positions[group].append(pos)

            # Store EVERY starting point
            initial_positions[group].append(pos)

        trail_history[group] = []

    map_placeholder = st.empty()

    temp = 30
    rain = 1000
    ndvi = 0.30

    for step in range(steps):

        scatter_points = []
        line_data = []

        for i, group in enumerate(herd_positions):

            new_positions = []

            for lat, lon in herd_positions[group]:

                new_lat, new_lon = predict_migration_path(
                    lat,
                    lon,
                    temp,
                    rain,
                    ndvi,
                    steps=1
                )[-1]

                new_positions.append([new_lat, new_lon])

                scatter_points.append({
                    "lat": new_lat,
                    "lon": new_lon,
                    "color": colors[i % len(colors)]
                })

            herd_positions[group] = new_positions

            for j in range(len(herd_positions[group])):

                start_lat, start_lon = initial_positions[group][j]
                end_lat, end_lon = herd_positions[group][j]

                line_data.append({

                    "start": [start_lon, start_lat],

                    "end": [end_lon, end_lat],

                    "color": colors[i % len(colors)]

                })

        scatter_df = pd.DataFrame(scatter_points)
        line_df = pd.DataFrame(line_data)

        line_layer = pdk.Layer(
            "LineLayer",
            data=line_df,
            get_source_position="start",
            get_target_position="end",
            get_color="color",
            get_width=8,
        )

        scatter_layer = pdk.Layer(
            "ScatterplotLayer",
            data=scatter_df,
            get_position="[lon, lat]",
            get_fill_color="color",
            get_radius=50000,
        )

        view_state = pdk.ViewState(
            latitude=scatter_df["lat"].mean(),
            longitude=scatter_df["lon"].mean(),
            zoom=5,
        )

        deck = pdk.Deck(
            layers=[line_layer, scatter_layer],
            initial_view_state=view_state,
        )

        map_placeholder.pydeck_chart(deck)

        temp += 1
        rain -= 50
        ndvi -= 0.02

        time.sleep(speed)

st.write(clustered_data.head())