import numpy as np
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
arg=vars(ap.parse_args())

image=cv2.imread(arg["image"])
cv2.imshow("Original",image)

mask=np.zeros(image.shape[:2], dtype="uint8")
(cX,cY)=(image.shape[1]//2,image.shape[0]//2)
cv2.rectangle(mask,(cX-75,cY-75),(cX+75,cY+75),255,-1)
cv2.imshow("Mask",mask)

masked=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("Masked",masked)
cv2.waitKey(0)

mask=np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask,(cX,cY),100,255,-1)
masked=cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("mask",mask)
cv2.imshow("masked",masked)
cv2.waitKey(0)
