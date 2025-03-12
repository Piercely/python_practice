import torch
import cv2
import os
import glob
import numpy as np
from torch.utils.data import Dataset
import random


class ISBI_Loader(Dataset):
    def __init__(self, img_dir, label_dir, img_size=(512, 512)):
        self.img_dir = img_dir  # 图像目录路径
        self.label_dir = label_dir  # 标签目录路径
        self.img_size = img_size  # 图像尺寸
        self.imgs_path = glob.glob(os.path.join(img_dir, '*.jpg'))  # 获取所有图像文件路径列表

    def augment(self, image, label):
        # 数据增强函数，随机进行水平翻转、垂直翻转、旋转、平移、缩放和透视变换
        if random.random() > 0.5:
            image = cv2.flip(image, 1)
            label = cv2.flip(label, 1)

        if random.random() > 0.5:
            image = cv2.flip(image, 0)
            label = cv2.flip(label, 0)

        if random.random() > 0.5:
            angle = random.uniform(-10, 10)
            M = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle, 1)
            image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
            label = cv2.warpAffine(label, M, (label.shape[1], label.shape[0]))

        if random.random() > 0.5:
            tx = random.uniform(-10, 10)
            ty = random.uniform(-10, 10)
            M = np.float32([[1, 0, tx], [0, 1, ty]])
            image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
            label = cv2.warpAffine(label, M, (image.shape[1], image.shape[0]))

        if random.random() > 0.5:
            scale = random.uniform(0.9, 1.1)
            image = cv2.resize(image, None, fx=scale, fy=scale)
            label = cv2.resize(label, None, fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)

        if random.random() > 0.5:
            h, w = image.shape[:2]
            src_points = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
            dst_points = src_points + np.random.uniform(-20, 20, size=src_points.shape).astype(np.float32)
            M = cv2.getPerspectiveTransform(src_points, dst_points)
            image = cv2.warpPerspective(image, M, (w, h))
            label = cv2.warpPerspective(label, M, (w, h))

        # 添加亮度和对比度调整
        if random.random() > 0.5:
            alpha = random.uniform(0.7, 1.3)
            beta = random.uniform(-30, 30)
            image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

        # 添加色彩空间变换
        if random.random() > 0.5:
            if random.random() > 0.5:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            else:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 添加噪声添加
        if random.random() > 0.5:
            noise = np.zeros(image.shape, np.int16)
            cv2.randn(noise, 0, 20)
            image = cv2.add(image, noise, dtype=cv2.CV_8UC3)

        # 添加随机剪裁和填充
        if random.random() > 0.5:
            x, y = random.randint(0, 50), random.randint(0, 50)
            h, w = image.shape[:2]
            image = image[y:h - y, x:w - x]
            label = label[y:h - y, x:w - x]

        # 添加随机遮挡
        if random.random() > 0.5:
            mask = np.zeros(image.shape[:2], dtype=np.uint8)
            cv2.rectangle(mask, (random.randint(0, 50), random.randint(0, 50)),
                          (random.randint(150, 200), random.randint(150, 200)), (255), -1)
            image[mask == 255] = 0
            label[mask == 255] = 0

        return image, label

    def __getitem__(self, index):
        image_path = self.imgs_path[index]  # 获取当前索引的图像文件路径
        label_path = os.path.join(self.label_dir,
                                  os.path.basename(image_path).replace('.jpg', '_bin.png'))  # 构建对应的标签文件路径

        # 添加文件存在性检查
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"图像文件不存在：{image_path}")
        if not os.path.exists(label_path):
            raise FileNotFoundError(f"标签文件不存在：{label_path}")

        image = cv2.imread(image_path)  # 读取图像
        label = cv2.imread(label_path, cv2.IMREAD_GRAYSCALE)  # 读取标签，以灰度模式加载

        # 添加文件读取失败的处理
        if image is None:
            raise FileNotFoundError(f"无法读取图像文件：{image_path}")
        if label is None:
            raise FileNotFoundError(f"无法读取标签文件：{label_path}")

        # 确保图像和标签的大小一致，并进行数据增强
        image, label = self.augment(image, label)
        image = cv2.resize(image, self.img_size)
        label = cv2.resize(label, self.img_size, interpolation=cv2.INTER_NEAREST)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转换图像为灰度
        label = (label > 0).astype(float)  # 将标签转换为二值化格式，用于语义分割任务

        image = image.reshape(1, image.shape[0], image.shape[1])  # 添加通道维度
        label = label.reshape(1, label.shape[0], label.shape[1])

        return image, label

    def __len__(self):
        return len(self.imgs_path)  # 返回数据集大小，即图像数量
