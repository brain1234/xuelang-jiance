# -*- coding: utf-8 -*-

from keras.preprocessing.image import ImageDataGenerator,image


datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    # rescale=1./255,
    horizontal_flip=True,
    fill_mode="nearest"
)

img = image.load_img(r"E:\hzj\code\xuelang-jiance\data\train\flaw\J01_2018.06.13 13_17_04.jpg")
x = image.img_to_array(img, data_format="channels_first")
print(x.shape)





