import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

def show_lossgraph(history):
    # get losses 
    loss = history.history["loss"][1:]
    val_loss = history.history["val_loss"][1:]
    # start at index 1 for epochs (first epoch is always far larger than the rest)
    epochs = range(1, len(loss) + 1)
    # plot
    plt.plot(epochs, loss, "g.", label="Training loss")
    plt.plot(epochs, val_loss, "b", label="Validation loss")
    plt.title("Training and validation loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()

def save_model(model):
    folder = "models/"
    model.save(f"{folder}bigwindmodel")

    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()

    # Save the TensorFlow Lite model
    with open(f"{folder}windmodel.tflite", "wb") as f:
        f.write(tflite_model)

def get_trainedmodel(showgraph = False):
    # read data
    data = pd.read_csv("windspeeds.csv")
    X = data.iloc[:, :-1].values 
    y = data.iloc[:, -1].values 
    # split data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    X_val = X_train[-1000:]
    y_val = y_train[-1000:]
    X_train = X_train[:-1000]
    y_train = y_train[:-1000]
    # create model
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(32, activation="relu", input_shape=(4,)),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(24, activation="relu"),
        tf.keras.layers.Dense(16, activation="relu"),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
    # fit & evaluate
    history = model.fit(X_train, y_train, epochs=50, batch_size=64, validation_data=(X_val, y_val))
    results = model.evaluate(X_test, y_test, batch_size=128)

    if showgraph:
        show_lossgraph(history)

    return model

if __name__ == "__main__":
    model = get_trainedmodel(showgraph=True)
    save_model(model)

    p = tf.constant([[1600, 2.0, 1.4, 1.9]])
    prediction = model.predict(p)
    print("prediction:", prediction)