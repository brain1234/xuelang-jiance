# -*- coding: utf-8 -*-

import os
from keras.utils import plot_model
from keras.applications.resnet50 import ResNet50
from keras.applications.vgg19 import VGG19
from keras.applications.inception_v3 import InceptionV3
from keras.layers import Dense,Flatten,GlobalAveragePooling2D
from keras.models import Model,load_model
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator


class PowerFineTuningModel:
    # 数据准备
    def DataGen(self, ):
        print()