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

results = []

print("\n========== PREDICTIVE HYPERVISOR DECISION ENGINE ==========")

for vm, path in files.items():

    df = pd.read_csv(path)
    latest = df[features].tail(1)

    probability = model.predict_proba(latest)[0][1] * 100

    if probability < 30:
        status = "NORMAL"
        action = "Continue normal monitoring"

    elif probability < 60:
        status = "CAUTION"
        action = "Increase monitoring frequency and review resource usage"

    else:
        status = "HIGH RISK"
        action = "Recommend CPU/RAM allocation review and consider migration"

    print("\nVM:", vm)
    print("Warning Probability:", round(probability, 2), "%")
    print("Resource Status:", status)
    print("Recommended Action:", action)

    results.append({
        "VM": vm,
        "Warning_Probability": round(probability, 2),
        "Resource_Status": status,
        "Recommended_Action": action
    })

report = pd.DataFrame(results)

report.to_csv(
    "/media/sf_HypervisorData/resource_recommendations.csv",
    index=False
)

print("\nRecommendation report saved successfully!")
print("File: resource_recommendations.csv")

print("\n============================================================")
