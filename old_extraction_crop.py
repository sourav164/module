import cv2, os, numpy, glob
import numpy as np

# get the name of the all images
all_images = []
for root, dirs, files in os.walk(r"C:\Users\SR\all_images"):
    for f in files:
        if f.endswith("jpg"):
            all_images.append(f)

all_images = list(set(all_images))

def crop_roi(original_frame):
    frame = original_frame.copy()
    # for 17-18
    pts = np.array([[0, 1440],[0, 715],[680, 0], [1750,0],[2560,870], [2560, 1440]])
    pts = pts - pts.min(axis=0)
    mask = np.zeros(original_frame.shape, np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)
    result = cv2.bitwise_and(original_frame, mask)
    return result


os.chdir(r"C:\All_videos")
videos = glob.glob("*mp4")

for v in videos:
    cap = cv2.VideoCapture(v)
    vid_name = v[:-4]
    print (vid_name)
    num = [int(img[20:-4]) for img in all_images if  img.startswith(vid_name)]
    for myFrameNumber in num:
        cap.set(cv2.CAP_PROP_POS_FRAMES,myFrameNumber)
        while True:
            ret, frame = cap.read()
            out_name = os.path.join("output", (str(vid_name)+"_"+str(myFrameNumber)+".png"))
            out_name2 = out_name.replace("png", "jpg")

            cropped = crop_roi (frame)
            crooped_name1 = out_name.replace("output", "c")
            crooped_name2 = out_name2.replace("output", "c")

            cv2.imwrite(out_name, frame)
            cv2.imwrite(out_name2, frame)
            cv2.imwrite(crooped_name1, cropped)
            cv2.imwrite(crooped_name2, cropped)
            break
