# -*- coding: utf-8 -*-

import os
import shutil


def get_imgs(dir):
    """
    获取目录下的所有文件
    :param dir: 文件夹的路径
    """
    abs_path = os.path.abspath(dir)
    filenames = os.listdir(dir)
    for i in filenames:
        fi = os.path.join(abs_path, i)
        if os.path.isdir(fi):
            get_imgs(fi)
        else:
            print(os.path.join(abs_path, fi))
            if os.path.splitext(fi)[1] != ".xml":
                if os.path.dirname(fi).endswith("正常"):
                    shutil.copyfile(os.path.join(abs_path, fi), "../data/train/normal/" + os.path.basename(fi))
                else:
                    shutil.copyfile(os.path.join(abs_path, fi), "../data/train/flaw/" + os.path.basename(fi))


if __name__ == "__main__":
    get_imgs(r"E:\hzj\天池比赛\雪浪制造AI挑战赛—视觉计算辅助良品检测\原始数据\xuelang_round1_train_part3_20180709")
