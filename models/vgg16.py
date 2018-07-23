# -*- coding: utf-8 -*-

from keras.preprocessing.image import ImageDataGenerator, image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
import numpy as np

model = VGG16(weights='imagenet', include_top=False)
img_path = '../data/train/flaw/J01_2018.06.13 13_17_04.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
feature = model.predict(x)
print(feature)