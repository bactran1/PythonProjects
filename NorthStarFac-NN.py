import keras.optimizers
import tensorflow as tf

def isThereGPU():
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
    print("Num CPUs Available: ", len(tf.config.list_physical_devices('CPU')))

isThereGPU()


import tensorflow as tf
import matplotlib.pyplot as plt
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(160, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(192, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(224, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

print(model.summary())

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy', tf.keras.metrics.RootMeanSquaredError()])

model.fit(x_train, y_train, batch_size=64, epochs=20)
model.evaluate(x_test, y_test)

# print(x_train.shape, y_train.shape)

# pick a sample to plot
sample = 7
image = x_train[sample]
# plot the sample
fig = plt.figure
plt.imshow(image, cmap='gray')
plt.show()
print(y_train[sample])