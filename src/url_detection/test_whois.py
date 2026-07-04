from whois_analyzer import WhoisAnalyzer

url = "https://www.google.com"

obj = WhoisAnalyzer(url)

features = obj.extract()

print("="*60)
print("WHOIS FEATURES")
print("="*60)

for k,v in features.items():

    print(f"{k:<20} : {v}")