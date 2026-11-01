import pandas as pd
import joblib

model = joblib.load(
    "/media/sf_HypervisorData/early_warning_model.pkl"
)

features = list(model.feature_names_in_)

files = {
    "Heavy VM": "/media/sf_HypervisorData/heavy_advanced_metrics.csv",
    "Light VM": "/media/sf_HypervisorData/light_advanced_metrics.csv"
}

for vm, path in files.items():
    df = pd.read_csv(path)

    latest = df[features].tail(1)

    prediction = model.predict(latest)[0]
    probability = model.predict_proba(latest)[0][1]

    print("\n", vm)
    print("Predicted warning:", "YES" if prediction == 1 else "NO")
    print("Warning probability:", round(probability * 100, 2), "%")

