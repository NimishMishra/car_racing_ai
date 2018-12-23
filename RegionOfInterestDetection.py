import numpy as np
import cv2



# This funtion aids to cut off extra noise from the input environment.
# Params:
#   image: the image that must be operated upon
#   vertices: defining the region in the image that is of interest

def Detect_roi(image, vertices):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(image, mask)
    return masked
