# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
from scipy.misc import imread, imresize

class Vgg16:
    """
    首次使用tensorflow创建vgg16网络结构
    2018/07/16
    """
    def __init__(self, ims, weights = None, sess = None):
        self.ims = ims

    # 创建卷积层
    def convlayers(self):
        self.params = []



