import joblib
import pandas as pd

from src.url_detection.rule_engine import RuleEngine
from src.url_detection.feature_extractor import URLFeatureExtractor
from src.url_detection.website_analyzer import WebsiteAnalyzer
from src.core.decision_engine import DecisionEngine


# ==========================================================
# Load Model
# ==========================================================

runtime_model = joblib.load(
    "models/saved_models/Runtime_URL_Model.pkl"
)

feature_order = joblib.load(
    "models/saved_models/runtime_features.pkl"
)

# ==========================================================


def predict_url(url):

    # ------------------------------------------------------

    if not url.startswith(("http://", "https://")):

        url = "https://" + url

    # ------------------------------------------------------
    # Rule Engine
    # ------------------------------------------------------

    rule = RuleEngine(url).calculate()

    rule_score = rule["risk_score"]

    reasons = rule["reasons"]

    # ------------------------------------------------------
    # URL Features
    # ------------------------------------------------------

    url_features = URLFeatureExtractor(url).extract()

    # ------------------------------------------------------
    # Website Features
    # ------------------------------------------------------

    try:

        web_features = WebsiteAnalyzer(url).extract()

    except:

        web_features = {}

    # ------------------------------------------------------
    # Merge Features
    # ------------------------------------------------------

    all_features = {}

    all_features.update(url_features)

    all_features.update(web_features)

    row = []

    for feature in feature_order:

        row.append(

            all_features.get(feature,0)

        )

    X = pd.DataFrame(

        [row],

        columns=feature_order

    )

    # ------------------------------------------------------
    # ML Prediction
    # ------------------------------------------------------

    probability = runtime_model.predict_proba(X)[0][1]

    ml_score = probability*100

    # ------------------------------------------------------
    # Adaptive Fusion
    # ------------------------------------------------------

    if rule_score >= 80:

        final_score = 100

    elif rule_score >= 50:

        final_score = max(

            (0.40*ml_score)+(0.60*rule_score),

            65

        )

    else:

        final_score = (

            (0.70*ml_score)+(0.30*rule_score)

        )

    # ------------------------------------------------------
    # Decision
    # ------------------------------------------------------

    decision = DecisionEngine().url_decision(
    ml_score,
    rule_score
)
    # decision = DecisionEngine().text_decision(

    #     final_score

    # )

    # ------------------------------------------------------

    return{

        "prediction":decision["prediction"],

        "risk":decision["risk"],

        "score":decision["score"],

        "ml_score":round(ml_score,2),

        "rule_score":rule_score,

        "reasons":reasons,

        "url_features":url_features,

        "website_features":web_features

    }