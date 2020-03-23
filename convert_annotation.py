#!/usr/bin/env python
# coding: utf-8

# In[104]:


import pandas as pd
import itertools
import os
os.chdir(r"D:\Box Sync\new_anotation\data")
df = pd.read_csv(r"D:\Box Sync\new_anotation\data\test_labels.csv")


# In[141]:


def ready_write(a):
    name = ""
    for i in range(len(a)):
        if i>4 and (i%5==0):
            name = name+" "+str(a[i])
        elif i==0:
            name = name+str(a[i])
        else: 
            name = name+","+str(a[i])
    return name


# In[150]:


lst = { i:[]  for i in  df.filename.unique().tolist()}
for index, row in df.iterrows():
    lst[row['filename']].append([row['xmin'],row['ymin'],row['xmax'],row['ymax'],1])
for i in lst:
    name ="images/"+i+","+ready_write( list(itertools.chain.from_iterable(lst[i])))
    file1 = open((i[:-4]+".txt"),"w") 
    file1.write(name) 
    file1.close()


# In[149]:




