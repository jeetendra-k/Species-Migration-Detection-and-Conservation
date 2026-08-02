import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pickle

# Load data
data = pd.read_csv("data/processed/elephant_data.csv")

# Features
X = data[["temperature", "rainfall", "ndvi"]]

# Targets
y_pop = data["population"]
y_lat = data["latitude"]
y_lon = data["longitude"]

# Models
lr = LinearRegression()
rf = RandomForestRegressor(n_estimators=100, random_state=42)

# Train population models
lr.fit(X, y_pop)
rf.fit(X, y_pop)

# Predictions
lr_pred = lr.predict(X)
rf_pred = rf.predict(X)

# Compare
import numpy as np

lr_rmse = np.sqrt(mean_squared_error(y_pop, lr_pred))
rf_rmse = np.sqrt(mean_squared_error(y_pop, rf_pred))

print("Linear RMSE:", lr_rmse)
print("Random Forest RMSE:", rf_rmse)

# Train migration models (lat/lon)
rf_lat = RandomForestRegressor()
rf_lon = RandomForestRegressor()

rf_lat.fit(X, y_lat)
rf_lon.fit(X, y_lon)

# Save everything
models = {
    "lr": lr,
    "rf": rf,
    "rf_lat": rf_lat,
    "rf_lon": rf_lon
}

with open("models/models.pkl", "wb") as f:
    pickle.dump(models, f)

print("All models trained and saved!")