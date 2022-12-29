import requests

data = {
    "url": "http://bit.ly/mlbookcamp-pants" #"5089843a-ecf8-4cb6-8f35-587f19125046.jpg", #
}

#url = "http://localhost:8080/2015-03-31/functions/function/invocations" # For docker
url = <"invoke_url> + "/predict" #for lambda funtion

results = requests.post(url, json=data).json()

print(results)