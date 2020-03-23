# this file convert annotation from csv file to text file
# original format YOLO created by labelimg 
# annotation to csv using converter used for tensorflow/model; collected from 
# https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10
# output file 
# Row format: image_file_path box1 box2 ... boxN;
# Box format: x_min,y_min,x_max,y_max,class_id (no space)

import pandas as pd
import itertools
import os
df = pd.read_csv("csv file location")

# input: list of lists [[box 1], [box 2], [box 3], ...... , [box N]]
# output: string = "x_min1,y_min1,x_max1,y_max1,class_id x_min2,y_min2,x_max2,y_max2,class_id" 
def ready_write(list_boxes):
    full_string = ""
    for i in range(len(list_boxes)):
        if i>4 and (i%5==0):
            full_string = full_string+" "+str(list_boxes[i])
        elif i==0:
            full_string = full_string+str(list_boxes[i])
        else: 
            full_string = full_string+","+str(list_boxes[i])
    return full_string

# lst : dictionary with all imagename as key and empty value
# append boxes locations as list of list in the dictionary
lst = { i:[]  for i in  df.filename.unique().tolist()}
for index, row in df.iterrows():
    lst[row['filename']].append([row['xmin'],row['ymin'],row['xmax'],row['ymax'],1])
    
# open and write a file in the following formate "image/filename full_string version of boxes"    
for i in lst:
    name ="images/"+i+","+ready_write( list(itertools.chain.from_iterable(lst[i])))
    file1 = open((i[:-4]+".txt"),"w") 
    file1.write(name) 
    file1.close()
