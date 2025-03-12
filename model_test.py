import os
from tqdm import tqdm
from model_metrics import compute_mIoU, show_results
import numpy as np
import torch
import cv2
from model.unet_model import UNet


def cal_miou(test_dir="E:/dataset_B/test/img",
             pred_dir="./results",
             gt_dir="E:/dataset_B/test/label"):
    miou_mode = 0
    num_classes = 2
    name_classes = ["background", "lane line"]

    if not os.path.exists(pred_dir):
        os.makedirs(pred_dir)

    if miou_mode in [0, 1]:
        print("加载模型中...")
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        net = UNet(n_channels=1, n_classes=1)
        net.to(device=device)
        net.load_state_dict(torch.load('model/best_iou_model(85).pth', map_location=device))
        net.eval()
        print("模型加载完成。")

        img_names = os.listdir(test_dir)
        image_ids = [image_name.split(".")[0] for image_name in img_names]

        print("正在获取预测结果...")
        for image_id in tqdm(image_ids):
            image_path = os.path.join(test_dir, image_id + ".jpg")
            img = cv2.imread(image_path)
            origin_shape = img.shape
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            img = cv2.resize(img, (512, 512))
            img = img.reshape(1, 1, img.shape[0], img.shape[1])
            img_tensor = torch.from_numpy(img).to(device=device, dtype=torch.float32)
            pred = net(img_tensor)
            pred = np.array(pred.data.cpu()[0])[0]
            pred[pred >= 0.5] = 255
            pred[pred < 0.5] = 0
            pred = cv2.resize(pred, (origin_shape[1], origin_shape[0]), interpolation=cv2.INTER_NEAREST)
            cv2.imwrite(os.path.join(pred_dir, image_id + ".png"), pred)
        print("预测结果获取完成。")

    if miou_mode in [0, 2]:
        print("正在计算mIoU...")
        hist, IoUs, PA_Recall, Precision = compute_mIoU(gt_dir, pred_dir, image_ids, num_classes, name_classes)
        print("mIoU计算完成。")
        miou_out_path = os.path.join(pred_dir, "dataset_A")
        if not os.path.exists(miou_out_path):
            os.makedirs(miou_out_path)
        show_results(miou_out_path, hist, IoUs, PA_Recall, Precision, name_classes)


if __name__ == '__main__':
    cal_miou()
