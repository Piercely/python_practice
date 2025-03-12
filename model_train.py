import os
import random
import string
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from tqdm import tqdm
from model.unet_model import UNet
from model_dataset import ISBI_Loader

# 设置 matplotlib 使用的字体
import matplotlib as mpl
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

def generate_random_suffix(length=2):
    return ''.join(random.choices(string.digits, k=length))

def calculate_iou(pred, label, threshold=0.5):
    pred = torch.sigmoid(pred) > threshold
    pred = pred.byte()  # 将pred转换为布尔类型张量
    label = label.byte()  # 将label转换为布尔类型张量
    intersection = (pred & label).float().sum((1, 2, 3))
    union = (pred | label).float().sum((1, 2, 3))
    iou = (intersection + 1e-6) / (union + 1e-6)
    return iou.mean().item()

def save_plot(data, title, xlabel, ylabel, filename):
    """保存图像"""
    plt.figure()
    plt.plot(data, label=title)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    random_suffix = generate_random_suffix()
    save_path = os.path.join('tryimg', f'{filename}_{random_suffix}.png')
    plt.savefig(save_path)
    plt.show()
    return save_path

def train_net(net, device, img_dir, label_dir, epochs=10, batch_size=4, lr=0.00001, optimizer_type='RMSprop'):
    dataset = ISBI_Loader(img_dir, label_dir)  # 创建数据集对象，会自动调用数据增强函数
    train_loader = torch.utils.data.DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)
    criterion = nn.BCEWithLogitsLoss()

    if optimizer_type == 'RMSprop':
        optimizer = optim.RMSprop(net.parameters(), lr=lr, weight_decay=1e-8, momentum=0.9)
    elif optimizer_type == 'Adam':
        optimizer = optim.Adam(net.parameters(), lr=lr, weight_decay=1e-8)
    elif optimizer_type == 'SGD':
        optimizer = optim.SGD(net.parameters(), lr=lr, momentum=0.9, weight_decay=1e-8)
    else:
        raise ValueError(f"不支持的优化器类型: {optimizer_type}")

    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min', patience=2)

    best_iou = 0.0
    best_loss = float('inf')
    train_losses = []
    train_accuracies = []
    train_ious = []

    for epoch in range(epochs):
        net.train()
        epoch_loss = 0
        correct = 0
        total = 0
        epoch_iou = 0

        with tqdm(total=len(train_loader), desc=f'Epoch {epoch + 1}/{epochs}', unit='batch') as pbar_epoch:
            for image, label in train_loader:
                optimizer.zero_grad()
                image = image.to(device=device, dtype=torch.float32)
                label = label.to(device=device, dtype=torch.float32)
                pred = net(image)
                loss = criterion(pred, label)
                loss.backward()
                optimizer.step()

                epoch_loss += loss.item()
                preds = torch.sigmoid(pred) > 0.5
                correct += (preds == label).sum().item()
                total += label.numel()

                batch_iou = calculate_iou(pred, label)
                epoch_iou += batch_iou

                pbar_epoch.set_postfix(loss=loss.item(), IoU=batch_iou)
                pbar_epoch.update(1)

            avg_epoch_loss = epoch_loss / len(train_loader)
            avg_epoch_iou = epoch_iou / len(train_loader)
            train_losses.append(avg_epoch_loss)
            train_accuracies.append(correct / total)
            train_ious.append(avg_epoch_iou)

            scheduler.step(avg_epoch_loss)

            if avg_epoch_loss < best_loss:
                best_loss = avg_epoch_loss
                best_loss_model_path = os.path.join('model', 'best_loss_model.pth')
                torch.save(net.state_dict(), best_loss_model_path)

            if avg_epoch_iou > best_iou:
                best_iou = avg_epoch_iou
                best_iou_model_path = os.path.join('model', 'best_iou_model.pth')
                torch.save(net.state_dict(), best_iou_model_path)

    loss_img_path = save_plot(train_losses, '损失变化', 'Epoch', '损失', 'train_loss')
    iou_img_path = save_plot(train_ious, 'mIoU变化', 'Epoch', 'mIoU', 'train_iou')

    print(f"训练完成. 最佳损失: {best_loss:.4f}")
    print(f"最佳mIoU: {best_iou:.4f}")
    print(f"训练损失图保存: {loss_img_path}")
    print(f"训练IoU图保存: {iou_img_path}")
    print(f"最佳损失模型保存路径: {best_loss_model_path}")
    print(f"最佳mIoU模型保存路径: {best_iou_model_path}")

    return best_loss_model_path, best_iou_model_path

if __name__ == "__main__":
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    net = UNet(n_channels=1, n_classes=1)
    net.to(device=device)

    img_dir = r"C:\Users\L1887\Desktop\b5\train\img"
    label_dir = r"C:\Users\L1887\Desktop\b5\train\label"
    os.makedirs('tryimg', exist_ok=True)
    os.makedirs('model', exist_ok=True)

    # 训练模型，当前使用RMSprop优化器，控制epochs
    train_net(net, device, img_dir, label_dir, epochs=100, batch_size=3, lr=0.00001, optimizer_type='RMSprop')
    # 切换优化器
    # train_net(net, device, img_dir, label_dir, epochs=20, batch_size=2, lr=0.00001, optimizer_type='Adam')
    # train_net(net, device, img_dir, label_dir, epochs=20, batch_size=2, lr=0.00001, optimizer_type='SGD')
