import tensorflow as tf
import matplotlib.pyplot as plt
import time

print('Using Tensorflow version: ', tf.version.VERSION)

def isThereGPU():
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
    print("Num CPUs Available: ", len(tf.config.list_physical_devices('CPU')))

isThereGPU()


mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

def createModel():

    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28, 28)),
      tf.keras.layers.Dense(784, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(1568, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(2080, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(1568, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(784, activation='relu'),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.00001),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy', tf.keras.metrics.RootMeanSquaredError()])
    return model

model = createModel()

print(model.summary())

start_time = time.time()
history = model.fit(x_train, y_train, batch_size=64, epochs=1)
#model.evaluate(x_test, y_test)
print(f'Time taken: {time.time()-start_time}')
#print(x_train.shape, y_train.shape)

## Plot Accuracy and Loss
acc = history.history['accuracy']

loss = history.history['loss']


epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.title('Training Accuracy. Best: ' + acc[epochs])
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()

# pick a sample to plot
# sample = 8
# image = x_train[sample]
# plot the sample
# fig = plt.figure
# plt.imshow(image, cmap='gray')
# plt.show()
# print(y_train[sample])