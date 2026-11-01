import pandas as pd
import joblib

model = joblib.load("/media/sf_HypervisorData/early_warning_model.pkl")

features = model.feature_names_in_

importance = pd.DataFrame({
    "Signal": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFEATURE IMPORTANCE:")
print(importance.to_string(index=False))
