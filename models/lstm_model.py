import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# Load data
data = pd.read_csv("data/processed/elephant_data.csv")

features = data[["temperature", "rainfall", "ndvi", "population"]].values

scaler = MinMaxScaler()
scaled = scaler.fit_transform(features)
import pickle

# Save scaler
with open("models/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

# Create sequences
X, y = [], []
seq_len = 3

for i in range(len(scaled) - seq_len):
    X.append(scaled[i:i+seq_len])
    y.append(scaled[i+seq_len][3])  # population

X, y = np.array(X), np.array(y)

# Model
model = Sequential([
    LSTM(50, activation='relu', input_shape=(seq_len, 4)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, y, epochs=100, verbose=0)

model.save("models/lstm.h5")
print("LSTM model trained!")