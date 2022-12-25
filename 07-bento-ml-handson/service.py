import bentoml
from bentoml.io import JSON

model_ref = bentoml.xgboost.get("credit_risk_xgb_model:latest")
dv = model_ref.custom_objects["dict_vectorizer"]


model_runner = model_ref.to_runner()

svc = bentoml.Service("credit_risk_classifier", runners=[model_runner])

@svc.api(input=JSON(), output=JSON())
def classify(application_data):
    vector = dv.transform(application_data)
    prediction = model_runner.predict.run(vector)
    print(f"PredictionOutput: {prediction}")
    return {"status": "Approved"}

# Exit VIM
# press Esc
# Press :
# Type :wq!

# To serve the model
# bentoml serve service.py:svc

# To serve the model that reloads automatically after changes (do not need to restart service after each changes)
# bentoml serve service.py:svc --reload

# Swagger UI
# http://localhost:3000/

# {
#   "seniority": 3,
#   "home": "owner",
#   "time": 36,
#   "age": 26,
#   "marital": "single",
#   "records": "no",
#   "job": "freelance",
#   "expenses": 35,
#   "income": 0.0,
#   "assets": 60000.0,
#   "debt": 3000.0,
#   "amount": 800,
#   "price": 1000
# }

