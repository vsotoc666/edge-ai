import tensorflow as tf 
import numpy as np
import matplotlib.pyplot as plt

mnist=tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test)=mnist.load_data()
x_train, x_test = x_train/255.0,  x_test/255.0 

plt.figure(figsize=(7,7))

for i, img in enumerate(x_train[:8]):
    plt.subplot(2, 4, 1+i)
    plt.imshow(img, cmap="Grays")
    plt.axis="off"

plt.show()



model= tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28, 28)), 
                                   tf.keras.layers.Dense(128, activation="relu"), 
                                   tf.keras.layers.Dropout(0.2), 
                                   tf.keras.layers.Dense(10) ])

model.compile(optimizer="adam",loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))

model.fit(x_train, y_train, epochs=5)

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()
with open('model_mnist.tflite', 'wb') as f:
    f.write(tflite_model)