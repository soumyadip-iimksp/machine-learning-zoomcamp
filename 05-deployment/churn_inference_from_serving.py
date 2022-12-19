import requests

host = "churn-serve-env.eba-<code>.<region>.elasticbeanstalk.com"
url = f"http://{host}/predict"

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
    "contract": "month_to_month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
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