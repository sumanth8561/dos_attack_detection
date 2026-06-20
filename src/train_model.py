import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

# Load preprocessed dataset
df = pd.read_csv("D:/ds/dataset/WSN-DS-preprocessed.csv")

# Separate features and labels
y = df["Attack_type"]
X = df.drop("Attack_type", axis=1)

# Map subclasses to a single "DoS" label
y = y.replace({"Flooding": "DoS", "Grayhole": "DoS", "Blackhole": "DoS"})

# Scale features (important for energy/traffic values)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train Random Forest with class balancing
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)
model.fit(X_scaled, y)

# Save model and scaler
joblib.dump(model, "D:/ds/models/rf_model_balanced.pkl")
joblib.dump(scaler, "D:/ds/models/scaler.pkl")

print(" Model retrained with balanced classes, subclass mapping, and scaling")