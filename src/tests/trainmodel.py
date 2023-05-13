import numpy as np
import pandas as pd
from tensorflow import keras

from sklearn.model_selection import train_test_split

INS  = 3
OUTS = 1

# import data & split
data = pd.read_csv('windspeeds.csv')
X = data.iloc[:, :-1].values # all columns except the last one
y = data.iloc[:, -1].values # only the last column
# msk = np.random.rand(len(df)) <= 0.8
# train = df[msk]
# test = df[~msk]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Split the training and testing data into input and output layers
X_train_inputs = np.split(X_train, 3, axis=1)
X_test_inputs = np.split(X_test, 3, axis=1)
y_train_output = y_train
y_test_output = y_test

print(y_train_output, y_test_output)

# model = keras.Sequential([
#     keras.layers.Dense(64, activation='relu', input_shape=(3,)),
#     keras.layers.Dense(32, activation='relu'),
#     keras.layers.Dense(1)
# ])

# # Compile the model
# model.compile(optimizer='adam', loss='mean_squared_error')

# # Train the model
# model.fit(X_train, y_train, epochs=2, batch_size=2560, validation_data=(X_test, y_test))

# X_new = np.array([[1.0, 2.0, 3.0],
#                   [4.0, 5.0, 6.0],
#                   [7.0, 8.0, 9.0]])

# y_pred = model.predict(X_new)

# # Print the predictions
# print(y_pred)