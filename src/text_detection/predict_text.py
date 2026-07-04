import joblib

from src.text_detection.text_rule_engine import TextRuleEngine
from src.core.decision_engine import DecisionEngine

# ==========================================================
# Load Model
# ==========================================================

model = joblib.load(
    "models/saved_models/Text_Model.pkl"
)

vectorizer = joblib.load(
    "models/saved_models/tfidf_vectorizer.pkl"
)

# ==========================================================


def predict_text(message):

    # ======================================================
    # Machine Learning Prediction
    # ======================================================

    X = vectorizer.transform([message])

    probability = float(model.predict_proba(X)[0][1])

    ml_score = probability * 100

    # ======================================================
    # Rule Engine
    # ======================================================

    rule = TextRuleEngine(message).calculate()

    rule_score = rule["rule_score"]

    reasons = rule["reasons"]

    # ======================================================
    # Adaptive Fusion
    # ======================================================

    if rule_score >= 80:

        final_score = 100

    elif rule_score >= 50:

        final_score = max(

            (0.40 * ml_score) +

            (0.60 * rule_score),

            65

        )

    else:

        final_score = (

            (0.70 * ml_score) +

            (0.30 * rule_score)

        )

    # ======================================================
    # Final Decision
    # ======================================================

    decision = DecisionEngine().text_decision(
        final_score
    )

    return {

        "prediction": decision["prediction"],

        "risk": decision["risk"],

        "score": decision["score"],

        "ml_score": round(ml_score, 2),

        "rule_score": rule_score,

        "probability": round(probability, 4),

        "reasons": reasons

    }


# ==========================================================

if __name__ == "__main__":

    message = input("Enter Message : ")

    result = predict_text(message)

    print("\n")

    print(result)