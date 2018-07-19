# -*- coding: utf-8 -*-

from keras.preprocessing.image import ImageDataGenerator, image

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearnest'
)

img = image.load_img("../data/train/J01_2018.06.13 13_25_43.jpg")
x = image.img_to_array(img)
print(x.shape)
x = x.reshape((1,) + x.shape)
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='train', save_prefix='J01', save_format='jpeg'):
    i += 1
    if i > 20:
        break  # otherwise the generator would loop indefinitely

