import tensorflow.lite as tflite
import numpy as np
from PIL import Image


interpreter = tflite.Interpreter(model_path="clothing-model.tflite")
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

classes = ['dress',
        'hat',
        'longsleeve',
        'outwear',
        'pants',
        'shirt',
        'shoes',
        'shorts',
        'skirt',
        't-shirt']

def preprocess_input(url):
    with Image.open(url) as f_in:
        x = f_in.resize((299,299), Image.NEAREST)
    arr = np.array(x, dtype="float32")
    arr = np.array([arr])
    arr /= 127.5
    arr -= 1.
    return arr


def predict(img_arr):
    interpreter.set_tensor(input_index, img_arr)
    interpreter.invoke()

    preds = interpreter.get_tensor(output_index)
    return preds[0]

def decode_result(pred):
    result = {c: float(p) for c, p in zip(classes, pred)}
    return result

def lambda_handler(event, context):
    url = event["url"]
    X = preprocess_input(url)
    preds = predict(X)
    results = decode_result(preds)
    return results
