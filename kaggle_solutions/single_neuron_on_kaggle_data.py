# importing libraries
import matplotlib.pyplot as plt
import pandas as pd
from learntools.core import binder
binder.bind(globals())
from learntools.deep_learning_intro.ex1 import *
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf
import matplotlib.pyplot as plt


plt.style.use('seaborn-whitegrid')
# Set Matplotlib defaults
plt.rc('figure', autolayout=True)
plt.rc('axes', labelweight='bold', labelsize='large',
       titleweight='bold', titlesize=18, titlepad=10)

red_wine = pd.read_csv('../input/dl-course-data/red-wine.csv')
red_wine.head()

red_wine.shape # (rows, columns)

input_shape = [11]

model = keras.Sequential([
    layers.Dense(units=1, input_shape=[11])
])

w, b = model.weights

print("Weights\n{}\n\nBias\n{}".format(w, b))

model = keras.Sequential([
    layers.Dense(1, input_shape=[1]),
])

x = tf.linspace(-1.0, 1.0, 100)
y = model.predict(x)

plt.figure(dpi=100)
plt.plot(x, y, 'k')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xlabel("Input: x")
plt.ylabel("Target y")
w, b = model.weights # you could also use model.get_weights() here
plt.title("Weight: {:0.2f}\nBias: {:0.2f}".format(w[0][0], b[0]))
plt.show()
