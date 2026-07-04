import joblib
import pandas as pd

# Load trained stacking model
MODEL_PATH = "models/saved_models/Stacking_Model.pkl"

model = joblib.load(MODEL_PATH)

def predict_phishing(features: dict):
    """
    Predict phishing website

    Parameters
    ----------
    features : dict

    Returns
    -------
    prediction
    confidence
    probability
    """

    X = pd.DataFrame([features])

    prediction = model.predict(X)[0]

    probability = model.predict_proba(X)[0]

    confidence = max(probability)

    return prediction, confidence, probability