import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model("xception_v6_ep_07_ac_0.868.h5")

tf.saved_model.save(model, "clothing-model")