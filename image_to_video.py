import cv2
import numpy as np
import glob

img_array = []
for filename in glob.glob('/home/alervice/Desktop/output_videos/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('/home/alervice/Desktop/project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()