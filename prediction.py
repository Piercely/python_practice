import os
import torch
import cv2
import numpy as np
from tqdm import tqdm
from model.unet_model import UNet


def predict_images(model_path, test_dir, output_dir, device):
    # Load the model
    print("Loading model...")
    net = UNet(n_channels=1, n_classes=1)
    net.to(device=device)
    net.load_state_dict(torch.load(model_path, map_location=device))
    net.eval()
    print("Model loaded.")

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Get the list of image files
    img_names = os.listdir(test_dir)
    image_ids = [image_name.split(".")[0] for image_name in img_names]

    # Predict and save the results
    print("Predicting images...")
    for image_id in tqdm(image_ids, desc="Predicting"):
        image_path = os.path.join(test_dir, image_id + ".jpg")
        img = cv2.imread(image_path)
        if img is None:
            print(f"Image {image_path} not found or unable to read.")
            continue

        origin_shape = img.shape
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = cv2.resize(img, (512, 512))
        img = img.reshape(1, 1, img.shape[0], img.shape[1])
        img_tensor = torch.from_numpy(img)
        img_tensor = img_tensor.to(device=device, dtype=torch.float32)

        with torch.no_grad():
            pred = net(img_tensor)

        pred = np.array(pred.data.cpu()[0])[0]
        pred[pred >= 0.5] = 255
        pred[pred < 0.5] = 0
        pred = cv2.resize(pred, (origin_shape[1], origin_shape[0]), interpolation=cv2.INTER_NEAREST)
        cv2.imwrite(os.path.join(output_dir, image_id + "_bin.png"), pred)

    print("Prediction completed.")


if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model_path = os.path.join('model', 'best_iou_model.pth')
    test_dir = r"C:/Users/L1887/Desktop/yz"
    output_dir = r"C:/Users/L1887/Desktop/yz"
    predict_images(model_path, test_dir, output_dir, device)
