# -*- coding: utf-8 -*-
"""allPracticals.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18CASJ1VAi8l5LjlSFOV697xPmlqLNwnj

### Prac 1 spam ham filter
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

mydata = pd.read_csv("/content/spam_ham_dataset (1).csv")
mydata

"""if result col is not in numeric"""

mydata["result"] = mydata["label"].apply(lambda x : 1 if x=="spam" else 0)

mydata

x_train,x_test,y_train,y_test = train_test_split(mydata["text"],mydata["result"])

y_train[0]

cv = CountVectorizer(max_features=10000)
count_x_train = cv.fit_transform(x_train)

count_x_train

count_x_test = cv.fit_transform(x_test).toarray()

count_x_test.shape

arr_count_x_train = count_x_train.toarray()
arr_count_x_train
arr_count_x_train.shape

import tensorflow as tf

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

model = Sequential()

model.add(Dense(64,input_shape = (count_x_train.shape[1],),activation="relu"))
model.add(Dense(32,activation="relu"))
model.add(Dense(1,activation="sigmoid"))

model.compile(optimizer ="SGD", loss = "binary_crossentropy" , metrics = ['accuracy'])

#for practical 4 using nesteorv
#model.compile(optimizer =SGD(learning_rate=0.01,nesterov = True), loss = "binary_crossentropy" , metrics = ['accuracy'])

model.fit(arr_count_x_train,y_train,epochs = 10)

example = ['''Subject: enron methanol ; meter # : 988291\r\nthis is a follow up to the note i gave you on monday , 4 / 3 / 00 { preliminary\r\nflow data provided by daren } .\r\nplease override pop ' s daily volume { presently zero } to reflect daily\r\nactivity you can obtain from gas control .\r\nthis change is needed asap for economics purposes
''']
example1 = cv.fit(x_train)
example2 = cv.transform(example1)
exampleArr = example2.toarray()
prediction = model.predict(exampleArr)
print(prediction)
if(prediction[0] > 0.5):
    print("spam")
else:
    print("ham")

"""###Practical 2 : Object detection"""

!pip install ultralytics

!yolo predict model=yolov8l.pt source = "/content/1.jpg"

"""###Practical 3 : Separate sounds using spleeter"""

!pip install spleeter

tf.__version__

from spleeter.separator import Separator

separator = Separator("spleeter:2stems")

separator.separate_to_file("/content/audio_example.mp3","/content/separateAudio")

"""###NLP Application"""

!pip install SpeechRecognition

import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile("/content/WhatsApp Ptt 2023-10-21 at 20.16.21.wav") as source:
  audio = r.listen(source)

  try:
    audio_text = r.recognize_google(audio)
    print(audio_text)
  except:
    print("try again")

"""###ESN"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class ESN:
    def __init__(self,neurons):
      self.input_weights = np.random.randn(neurons,1)
      self.neurons_weights = np.random.randn(neurons,neurons)
      self.output_weights = None

    def train(self,x,y):
      x_reservior = np.tanh(self.input_weights*x + self.neurons_weights*x)
      self.output_weights = np.linalg.lstsq(x_reservior,y)[0]

    def predict(self,x):
       x_reservior = np.tanh(self.input_weights*x + self.neurons_weights*x)
       y_pred = self.output_weights * x_reservior
       return y_pred

#make inputs x and y
x = np.random.randn(10,1)
y = np.random.randn(10,1)


esn = ESN(10)

esn.train(x,y)

g = nx.Graph()
g.add_nodes_from(range(10,1))

#as esn is matrix if i -> j is not 0 then add edge in graph from i to j
for i in range(10):
  for j in range(10):
    if(esn.neurons_weights[i,j] != 0):
      g.add_edge(i,j)

nx.draw(g,with_labels = True)
plt.show()

x

y

y_pred = esn.predict(x)
y_pred

plt.plot(x,y , label = "Actual")
plt.plot(x,y_pred,label = "Predicted")
plt.legend()
plt.show()

"""###ICA"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA

#to preserve randomness
# np.random.seed(0)

#create 2000 samples from 0 to 8
time = np.linspace(0,8,2000)

#signal 1
s1 = np.sin(2*time)

s2 = np.cos(2*time)

# add noise
s3 = np.random.rand(2000)

S = np.c_[s1,s2,s3]
A = np.array([[1,1,1],[0.5,2,1],[1,0.5,2]])

X = np.dot(S,A) #observed signal

ica = FastICA(n_components=3)
recovered = ica.fit_transform(X)

plt.subplot(3,1,1)
plt.plot(S)

plt.subplot(3,1,2)
plt.plot(X)

plt.subplot(3,1,3)
plt.plot(recovered)

plt.tight_layout()
plt.show()

"""###CIFAR"""

import numpy as np
import pandas as pd

import tensorflow as tf
from tensorflow import keras

from keras import models,layers,optimizers,datasets

(train_images,train_labels),(test_images,test_labels) = datasets.cifar10.load_data()

train_images , test_images = train_images/255.0 , test_images/255.0

model = models.Sequential()

model.add(layers.Conv2D(32,(3,3),input_shape=(32, 32, 3),activation='relu'))
model.add(layers.MaxPool2D((2,2)))

model.add(layers.Conv2D(64,(3,3),activation='relu'))
model.add(layers.MaxPool2D((2,2)))

model.add(layers.Conv2D(64,(3,3),activation='relu'))
model.add(layers.Flatten())

model.add(layers.Dense(64,activation='relu'))
model.add(layers.Dense(10,activation = 'sigmoid'))

model.compile(optimizer='SGD',loss = 'categorical_crossentropy',metrics=['accuracy'])

model.fit(train_images,train_labels,epochs=10)

!pip install gitpython

from git import Repo

Repo.clone_from("https://github.com/VishalShinde16/google-keep-clone.git","/content/sample_data/demo")