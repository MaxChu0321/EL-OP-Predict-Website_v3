from joblib import load



with open("./data/EL-RFA-Predict-clinical-ER/EL-RFA-Predict-clinical-ER-SmallTumor-STDscaler-v240508.joblib", "rb") as f:
    scaler = load(f)

print(scaler)