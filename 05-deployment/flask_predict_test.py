import requests

url = "http://localhost:9696/predict"

customer = {
    #"customerid": "8879-zkjof",
    "gender": "male", #"female",
    "seniorcitizen": 1,#0,
    "partner": "yes",#"no",
    "dependents": "no",
    "tenure": 1, #64
    "phoneservice": "no",#"yes",
    "multiplelines": "no",
    "internetservice": "dsl",
    "onlinesecurity": "no",#"yes",
    "onlinebackup": "no",
    "deviceprotection": "no", #"yes",
    "techsupport": "yes",
    "streamingtv": "yes",
    "streamingmovies": "yes",
    "contract": "one_year",
    "paperlessbilling": "yes",
    "paymentmethod": "bank_transfer_(automatic)",
    "monthlycharges": 7.1,#79.85,
    "totalcharges": 332 #3320.75
}

print(requests.post(url, json=customer))

response = requests.post(url, json=customer).json()
print(response)


if response["churn"]==True:
    print("Sending Promo email to %s" % ("abc@yeehaw.kom"))
else:
    print("Not Sending Promo email to %s" % ("abc@yeehaw.kom"))