# -*- coding: utf-8 -*-

import os


def get_nor_imgs(dir):
    """
    :param dir: 文件夹的路径
    :return: 获取正常无瑕疵的图片
    """
    if os._exists(dir):
        for f in os.listdir(dir):
            print(f)

def get_flaw_imgs(dir):
    """
    :param dir: 文件夹路径
    :return: 获取有瑕疵的图片
    """

if __name__ == "__main__":
    get_nor_imgs(r"../models")
