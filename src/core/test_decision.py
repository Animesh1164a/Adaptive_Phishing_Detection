from decision_engine import DecisionEngine

obj=DecisionEngine()

print()

print(obj.url_decision(

    ml_score=82,

    rule_score=95

))

print()

print(obj.text_decision(

    probability=0.97

))