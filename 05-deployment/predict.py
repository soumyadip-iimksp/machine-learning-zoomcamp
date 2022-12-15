import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = "churn-predict-model.bin"

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


app = Flask("churn")

@app.route("/predict", methods=["POST"])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = round(model.predict_proba(X)[0][1], 4)
    churn = y_pred > 0.5
    result = {"churn_probability": float(y_pred),
                "churn": bool(churn)
                }

    return jsonify(result)

if __name__ == "__main__":
# print("Input:", customer)
# print(f"Churn Probability: {y_pred*100}%")
    app.run(debug=True, host="0.0.0.0", port=9696)