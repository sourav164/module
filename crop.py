import cv2, numpy, os, glob
import numpy as np

os.chdir(r"D:\training_data\17-18\output")
all_images = glob.glob("*g")


def crop_roi(original_frame):
    frame = original_frame.copy()

    # pts - location of the 4 corners of the roi
    # 15-16
    # pts = np.array([[0, 1440],[0, 1020],[1050, 0], [1400,0],[2560,1140], [2560, 1440]])

    #17-18
    pts = np.array([[0, 1440],[0, 715],[680, 0], [1750,0],[2560,870], [2560, 1440]])

    # 19-20
    # pts = np.array([[0, 1440],[0,780],[790, 0], [1750,0],[2560,850], [2560, 1440]])

    #23-24
    # pts = np.array([[0, 1450], [0, 1087], [977, 80], [1925, 67], [2560, 800], [2560, 1440]])
    # (x,y,w,h) = cv2.boundingRect(pts)

    pts = pts - pts.min(axis=0)
    mask = np.zeros(original_frame.shape, np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)
    result = cv2.bitwise_and(original_frame, mask)
    return result

for img in all_images:
    
    original_frame = cv2.imread(img)
    frame = crop_roi(original_frame)
    
    name = os.path.join("c", img)
    cv2.imwrite( name, frame )
