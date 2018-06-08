# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 15:06:46 2018

@author: n34873
"""


import cv2

vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval: 
    cv2.imshow("img", frame)
    rval, frame = vc.read()
      
    key = cv2.waitKey(20) 
    if key == 27: # exit on ESC
        break

cv2.destroyAllWindows()        
#cv2.destroyWindow("preview")
