from feature_extractor import URLFeatureExtractor

url = "https://amazon-login-security.xyz/login.php?id=123"

extractor = URLFeatureExtractor(url)

features = extractor.extract()

print()

print("="*60)

print("Extracted Features")

print("="*60)

for k,v in features.items():

    print(f"{k:<35}{v}")