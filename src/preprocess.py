import pandas as pd

# Load raw dataset
df = pd.read_csv("D:/ds/dataset/WSN-DS.csv")

#  Clean column names: strip spaces and replace with underscores
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Save preprocessed dataset
df.to_csv("D:/ds/dataset/WSN-DS-preprocessed.csv", index=False)

print(" Preprocessing complete. Cleaned dataset saved.")