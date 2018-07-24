# -*- coding: utf-8 -*-

import os
import random
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
                    shutil.copyfile(os.path.join(abs_path, fi), "../data/test/normal/" + os.path.basename(fi))
                else:
                    shutil.copyfile(os.path.join(abs_path, fi), "../data/test/flaw/" + os.path.basename(fi))


def get_train_valication_imgs(dir, des_train_dir, des_valication_dir):
    """
    获取训练集 80%, 验证集 20%
    """
    fileName = []
    abs_path = os.path.abspath(dir)
    fileNames = os.listdir(dir)
    print(os.pardir)
    for f in fileNames:
        if not os.path.isdir(os.path.join(abs_path, f)):
            fileName.append(f)
    # shuffle
    random.shuffle(fileName)
    # sample
    valication = random.sample(fileName, int(len(fileName) * 0.2))
    train = list(set(fileName).difference(set(valication)))
    print("ori size", len(fileName))
    print("train size", len(train))
    print("valication size", len(valication))

    for f1 in train:
        shutil.copy(os.path.join(dir, f1), os.path.join(des_train_dir, f1))

    for f1 in valication:
        shutil.copy(os.path.join(dir, f1), os.path.join(des_valication_dir, f1))


if __name__ == "__main__":
    # get_imgs(r"F:\天池比赛项目\雪浪制造AI挑战赛\data\xuelang_round1_train_part1_20180628")
    # get_imgs(r"F:\天池比赛项目\雪浪制造AI挑战赛\data\xuelang_round1_train_part2_20180705")
    # get_imgs(r"F:\天池比赛项目\雪浪制造AI挑战赛\data\xuelang_round1_train_part3_20180709")
    get_train_valication_imgs("../data/test/flaw", "../data/train/flaw", "../data/valication/flaw")
    get_train_valication_imgs("../data/test/normal", "../data/train/normal", "../data/valication/normal")