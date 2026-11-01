import pandas as pd

heavy = pd.read_csv("/media/sf_HypervisorData/heavy_advanced_metrics.csv")
light = pd.read_csv("/media/sf_HypervisorData/light_advanced_metrics.csv")

def prepare_data(df, vm_name):
    df = df.copy()

    future_cpu = pd.concat(
        [df["CPU_Usage"].shift(-i) for i in range(1, 6)],
        axis=1
    ).max(axis=1)

    df["Early_Warning"] = (future_cpu >= 40).astype(int)
    df["VM"] = vm_name

    return df.iloc[:-5].copy()

heavy_data = prepare_data(heavy, "Heavy")
light_data = prepare_data(light, "Light")

combined = pd.concat([heavy_data, light_data], ignore_index=True)

combined.to_csv(
    "/media/sf_HypervisorData/early_warning_dataset.csv",
    index=False
)

print("Dataset created successfully!")
print("Total samples:", len(combined))
print("\nWarning labels:")
print(combined["Early_Warning"].value_counts())
print("\nVM distribution:")
print(combined.groupby("VM")["Early_Warning"].value_counts())
