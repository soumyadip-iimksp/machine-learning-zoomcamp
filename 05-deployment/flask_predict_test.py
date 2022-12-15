import requests

url = "http://127.0.0.1:9696/predict"

customer = {
    "customerid": "8879-zkjof",
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "no",
    "dependents": "no",
    "tenure": 41,
    "phoneservice": "yes",
    "multiplelines": "no",
    "internetservice": "dsl",
    "onlinesecurity": "yes",
    "onlinebackup": "no",
    "deviceprotection": "yes",
    "techsupport": "yes",
    "streamingtv": "yes",
    "streamingmovies": "yes",
    "contract": "one_year",
    "paperlessbilling": "yes",
    "paymentmethod": "bank_transfer_(automatic)",
    "monthlycharges": 79.85,
    "totalcharges": 3320.75
}

print(requests.post(url, json=customer))

response = requests.post(url, json=customer).json()
print(response)


if response["churn"]==True:
    print("Sending Promo email to %s" % ("abc@yeehaw.kom"))
else:
    print("Not Sending Promo email to %s" % ("abc@yeehaw.kom"))