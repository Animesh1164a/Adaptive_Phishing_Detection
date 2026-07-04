class DecisionEngine:

    def __init__(self):
        pass

    # ==========================================================
    # Generic Decision
    # ==========================================================

    def final_decision(self, final_score):

        if final_score >= 80:

            prediction = "PHISHING"
            risk = "HIGH"

        elif final_score >= 35:

            prediction = "SUSPICIOUS"
            risk = "MEDIUM"

        else:

            prediction = "SAFE"
            risk = "LOW"

        return {

            "prediction": prediction,

            "risk": risk,

            "score": round(final_score,2)

        }

    # ==========================================================

    def url_decision(self, ml_score, rule_score):

        if rule_score >= 80:

            return self.final_decision(100)

        elif rule_score >= 40:

            return self.final_decision(50)

        final_score = (

            (0.70 * ml_score) +

            (0.30 * rule_score)

        )

        return self.final_decision(final_score)

    # ==========================================================

    def text_decision(self, final_score):

        return self.final_decision(final_score)