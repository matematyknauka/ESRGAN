import cv2
import torch
import numpy as np

def tensor(path):
    # Wczytuje obraz i zwraca tensor w formacie dla ESRGAN.
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    img = img*1.0/255
    img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
    img_LR = img.unsqueeze(0)
    return img_LR