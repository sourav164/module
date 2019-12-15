from __future__ import print_function
import numpy as np
import argparse, cv2, os, glob

# take the video as input
all_video = glob.glob("*.mp4")

for video in all_video:
	# read the video and extract info about it
	cap = cv2.VideoCapture(video)

	# make the folder to save file
	output = os.path.join("output", video[:-4])
	if not os.path.exists(output):
		os.makedirs(output)

	# get total number of frames
	totalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	x = np.linspace(0,totalFrames-10,30).tolist()


	print (x)
	for myFrameNumber in x:
		myFrameNumber = int(myFrameNumber)
		cap.set(cv2.CAP_PROP_POS_FRAMES,myFrameNumber)
		while True:
			ret, frame = cap.read()
			out_name = os.path.join(output, (str(file[:-9])+"_"+str(myFrameNumber)+".png"))
			out_name2 = os.path.join(output, (str(file[:-9])+"_"+str(myFrameNumber)+".jpg"))
			cv2.imwrite(out_name, frame)
			cv2.imwrite(out_name2, frame)
			break
