# -*- coding: utf-8 -*-

import os


def get_nor_imgs(dir):
    """
    :param dir: 文件夹的路径
    :return: 获取正常无瑕疵的图片
    """
    abs_path = os.path.abspath(dir)
    filenames = os.listdir(dir)
    print(abs_path)
    filenames = [os.path.join(abs_path, i) for i in filenames]
    print(filenames)
    for file in filenames:
        if os.path.isfile(file):
            print("是个文件，不是目录")


def get_flaw_imgs(dir):
    """
    :param dir: 文件夹路径
    :return: 获取有瑕疵的图片
    """


if __name__ == "__main__":
    get_nor_imgs(r"../models")
