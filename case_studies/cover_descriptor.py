import numpy as np
import cv2

class CoverDescriptor:
    def __init__(self,useSIFT= False):
        self.useSIFT= useSIFT

    def describe(self,image):
        descriptor=cv2.BRIST_create()

        if self.useSIFT:
            descriptor=cv2.xfeatures2d.SIFT_create()

        (kps, decs)=descriptor.detectAndCompute(image,None)
        kps=np.float32([kp.pt for kp in kps])

        return (kps,descs)
