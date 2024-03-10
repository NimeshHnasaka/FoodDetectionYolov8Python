import tensorflowjs as tfjs
import tensorflow as tf


# Load your Keras model
keras_model = tf.keras.models.load_model('D:\Python\ObjectDetection\trained_new_mode.h5')

# Convert and save the model in TensorFlow.js format
tfjs.converters.save_keras_model(keras_model, 'ObjectDetection/tfjsmodel')