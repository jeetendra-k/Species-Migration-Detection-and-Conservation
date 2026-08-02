import pickle
import numpy as np
import pandas as pd


# ==============================
# LOAD ML MODELS
# ==============================

with open("models/models.pkl", "rb") as f:
    models = pickle.load(f)

# Load LSTM model


# Load scaler for LSTM
with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)


# ==============================
# POPULATION PREDICTION
# ==============================

def predict_population(temp, rain, ndvi, model_type="hybrid"):
    """
    model_type:
    - 'rf' → Random Forest
    - 'lr' → Linear Regression
    - 'hybrid' → average of both
    """

    if model_type == "rf":
        return int(models["rf"].predict([[temp, rain, ndvi]])[0])

    elif model_type == "lr":
        return int(models["lr"].predict([[temp, rain, ndvi]])[0])

    elif model_type == "hybrid":
        rf_pred = models["rf"].predict([[temp, rain, ndvi]])[0]
        lr_pred = models["lr"].predict([[temp, rain, ndvi]])[0]
        return int((rf_pred + lr_pred) / 2)


# ==============================
# MIGRATION PATH (Agent-Based + SDM logic)
# ==============================

import random

def predict_migration_path(start_lat, start_lon, temp, rain, ndvi, steps=6):

    path = []
    lat, lon = start_lat, start_lon

    for _ in range(steps):

        # --- Habitat score ---
        score = (ndvi * 0.5) + (rain / 1500 * 0.3) - (temp / 50 * 0.2)

        # --- Natural random movement ---
        lat_change = random.uniform(-0.3, 0.3)
        lon_change = random.uniform(-0.3, 0.3)

        # --- Environmental influence ---
        if temp > 32:
            lat_change += 0.2   # move slightly north

        if rain < 900:
            lon_change += 0.2   # move toward wetter area

        if ndvi < 0.3:
            lat_change += 0.2   # search vegetation

        # --- Apply movement ---
        lat += lat_change
        lon += lon_change

        # --- HARD CONSTRAINTS (VERY IMPORTANT) ---
        
        # Stay within India ecological bounds
        lat = max(8, min(lat, 30))   # avoid Himalayas (>30)
        lon = max(68, min(lon, 90))  # avoid China/Bangladesh extremes

        path.append([lat, lon])

        # --- Simulate environment ---
        temp += 0.5
        rain -= 20
        ndvi -= 0.01

    return path


# ==============================
# LSTM PREDICTION (Time-Series)
# ==============================

def predict_lstm(data):
    """
    Predict next-step population using LSTM
    """

    features = data[["temperature", "rainfall", "ndvi", "population"]].values

    # Use SAME scaler from training
    scaled = scaler.transform(features)

    # Take last 3 timesteps
    seq = scaled[-3:]
    seq = np.reshape(seq, (1, 3, 4))

    # Predict
    pred = lstm_model.predict(seq)

    # Inverse scaling
    dummy = np.zeros((1, 4))
    dummy[0][3] = pred[0][0]

    inv = scaler.inverse_transform(dummy)

    return int(inv[0][3])