import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("/media/sf_HypervisorData/early_warning_dataset.csv")

# Select input features
features = [
    "CPU_Usage",
    "RAM_Usage",
    "PageFault_Rate",
    "MajorFault_Rate",
    "ContextSwitch_Rate",
    "Interrupt_Rate",
    "Memory_Pressure",
    "Disk_Read_Rate_MB",
    "Disk_Write_Rate_MB"]

X = df[features]
y = df["Early_Warning"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Train the classifier
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# Predict early warnings
y_pred = model.predict(X_test)

# Display results
print("CONFUSION MATRIX:")
print(confusion_matrix(y_test, y_pred))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred, zero_division=0))

# Save trained model
import joblib
joblib.dump(model, "/media/sf_HypervisorData/early_warning_model.pkl")

print("\nModel saved successfully!")
