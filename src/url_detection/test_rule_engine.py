from rule_engine import RuleEngine

url = "http://paypal-login-security-update.xyz/login.php?id=123"

engine = RuleEngine(url)

result = engine.calculate()

print("=" * 60)
print("RULE ENGINE RESULT")
print("=" * 60)

print("\nRisk Score:", result["risk_score"])

print("\nReasons:")

for reason in result["reasons"]:

    print("✔", reason)