import pandas as pd
import joblib
from flask import Flask, request, render_template

app = Flask(__name__)
model = joblib.load("D:/ds/models/rf_model_clean.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    predictions = None
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".csv"):
            df = pd.read_csv(file)

            # Clean column names
            df.columns = df.columns.str.strip().str.replace(" ", "_")

            # Drop label column if present
            if "Attack_type" in df.columns:
                df = df.drop(columns=["Attack_type"])

            # Align with model
            df = df[model.feature_names_in_]

            # Predict for all rows
            preds = model.predict(df)
            predictions = preds.tolist()

    return render_template("index.html", predictions=predictions)

if __name__ == "__main__":
    app.run(debug=True)