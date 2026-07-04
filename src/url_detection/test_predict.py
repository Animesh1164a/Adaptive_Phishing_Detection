from src.url_detection.predict_url import predict_url

url = input("Enter URL: ")

result = predict_url(url)

print(result)