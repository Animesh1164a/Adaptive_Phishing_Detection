from src.text_detection.predict_text import predict_text

message = input("Enter Message : ")

result = predict_text(message)

print("\n")

print(result)