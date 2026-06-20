import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load model and scaler
rf = joblib.load("D:/ds/models/rf_model_balanced.pkl")
scaler = joblib.load("D:/ds/models/scaler.pkl")

# Load preprocessed dataset
df = pd.read_csv("D:/ds/dataset/WSN-DS-preprocessed.csv")

# Separate features and labels
y = df["Attack_type"]
X = df.drop(columns=["Attack_type"])

# Map subclasses to "DoS" for evaluation
# Map subclasses to DoS BEFORE training
y = y.replace({"Flooding": "DoS", "Grayhole": "DoS", "Blackhole": "DoS"})


# Scale features
X_scaled = scaler.transform(X)

# Predictions
y_pred = rf.predict(X_scaled)

# Evaluation
print("Evaluation Results:")
print(classification_report(y, y_pred))

cm = confusion_matrix(y, y_pred)
print("Confusion Matrix:\n", cm)

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=rf.classes_,
            yticklabels=rf.classes_)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - DoS Detection in WSN")
plt.show()