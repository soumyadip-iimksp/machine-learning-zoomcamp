
# #import tensorflow.lite as tflite
# import tflite_runtime.interpreter as tflite

# #import tensorflow.lite as tflite
# from io import BytesIO
# from urllib import request
# #from keras_image_helper import create_preprocessor

# import numpy as np
# from PIL import Image

# #preprocessor = create_preprocessor('xception', target_size=(299, 299))

# interpreter = tflite.Interpreter(model_path="clothing-model.tflite")
# interpreter.allocate_tensors()

# input_index = interpreter.get_input_details()[0]["index"]
# output_index = interpreter.get_output_details()[0]["index"]

# classes = ['dress',
#         'hat',
#         'longsleeve',
#         'outwear',
#         'pants',
#         'shirt',
#         'shoes',
#         'shorts',
#         'skirt',
#         't-shirt']

# def download_image(url):
#     with request.urlopen(url) as resp:
#         buffer = resp.read()
#     stream = BytesIO(buffer)
#     img = Image.open(stream)
#     return img

# def preprocess_input(url):
    
#     x = download_image(url)
#     x = x.resize((299, 299), Image.NEAREST)
#     #with Image.open(url) as f_in:
#     #    x = f_in.resize((299,299), Image.NEAREST)
#     arr = np.array(x, dtype="float32")
#     arr = np.array([arr])
#     arr /= 127.5
#     arr -= 1.
#     return arr


# def predict(img_arr):
#     interpreter.set_tensor(input_index, img_arr)
#     interpreter.invoke()

#     preds = interpreter.get_tensor(output_index)
#     return preds[0]

# def decode_result(pred):
#     result = {c: float(p) for c, p in zip(classes, pred)}
#     return result

# def lambda_handler(event, context):
#     url = event["url"]
#     #X = preprocessor.from_url(url)
#     X = preprocess_input(url)
#     preds = predict(X)
#     results = decode_result(preds)
#     return results


import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor


preprocessor = create_preprocessor('xception', target_size=(299, 299))


interpreter = tflite.Interpreter(model_path='clothing-model.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
input_index = input_details[0]['index']

output_details = interpreter.get_output_details()
output_index = output_details[0]['index']


def predict(X):
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()

    preds = interpreter.get_tensor(output_index)
    return preds[0]


labels = [
    'dress',
    'hat',
    'longsleeve',
    'outwear',
    'pants',
    'shirt',
    'shoes',
    'shorts',
    'skirt',
    't-shirt'
]

def decode_predictions(pred):
    result = {c: float(p) for c, p in zip(labels, pred)}
    return result


def lambda_handler(event, context):
    url = event['url']
    X = preprocessor.from_url(url)
    preds = predict(X)
    results = decode_predictions(preds)
    return results