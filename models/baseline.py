# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D
from keras.layers import Activation, Flatten, Dropout, Dense
from keras.preprocessing import image


model = Sequential()
model.add(Conv2D((32, (3, 3)), input_shape=(3, 124, 124)))
model.add(Activation('relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', metrics=['accuracy'], optimizer='adam')

batch_size = 16


train_datagen = image.ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    horizontal_flip=True
    )

# 读取训练数据以及shuffle过程
train_generator = train_datagen.flow_from_directory(
        '../data/train',  # this is the target directory
        target_size=(124, 124),  # all images will be resized to 150x150
        batch_size=batch_size,
        shuffle=True,
        class_mode='binary')




