import tensorflow.lite as tflite
import tensorflow as tf

interpreter = tflite.Interpreter(model_path="windmodel.tflite")
interpreter.allocate_tensors()

input_details  = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_data = tf.constant([[1600, 3.0, 1.4, 1.9]])  # Prepare your input data
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()

output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)