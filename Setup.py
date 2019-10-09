#This is where we setup our model
import numpy as np 
import mnist 
import keras

train_images = mnist.train_images()
train_labels = mnist.train_labels()

#To test it's loading properly
print(train_images.shape) # (60000, 28, 28)
print(train_labels.shape) # (60000,)