from website_analyzer import WebsiteAnalyzer

url = "https://www.google.com"

analyzer = WebsiteAnalyzer(url)

features = analyzer.extract()

print("=" * 60)
print("Website Features")
print("=" * 60)

for key, value in features.items():
    print(f"{key:<25} : {value}")