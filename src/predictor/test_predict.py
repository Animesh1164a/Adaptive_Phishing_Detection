from predict import predict_phishing

sample = {

"having_IPhaving_IP_Address":1,
"URLURL_Length":1,
"Shortining_Service":0,
"having_At_Symbol":1,
"double_slash_redirecting":0,
"Prefix_Suffix":1,
"having_Sub_Domain":1,
"SSLfinal_State":1,
"Domain_registeration_length":1,
"Favicon":1,
"port":0,
"HTTPS_token":0,
"Request_URL":1,
"URL_of_Anchor":1,
"Links_in_tags":0,
"SFH":1,
"Submitting_to_email":0,
"Abnormal_URL":0,
"Redirect":0,
"on_mouseover":0,
"RightClick":1,
"popUpWidnow":0,
"Iframe":0,
"age_of_domain":1,
"DNSRecord":1,
"web_traffic":1,
"Page_Rank":1,
"Google_Index":1,
"Links_pointing_to_page":0,
"Statistical_report":1

}

prediction, confidence, probability = predict_phishing(sample)

print("="*60)

print("Prediction :", prediction)

print("Confidence :", confidence)

print("Probability :", probability)