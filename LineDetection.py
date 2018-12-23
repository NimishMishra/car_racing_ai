import numpy as np
import cv2

# drawLines() aids to draw the lines depicted by the coordinates stored in the 
# array of arrays- lines.

def drawLines(image, lines):
    try:
        for line in lines:
            coordinate = line[0]
            cv2.line(image, (coordinate[0], coordinate[1]), \
            (coordinate[2], coordinate[3]), color = [255, 255, 255], thickness = 5)
    except:
        pass



# Implementing Hough Transform. Find more imformation about Progressive Probabilistic
# Hough Transform in the OpenCV documentation
def detect_lines(image):
    minLineLength = 30
    maxLineGap = 15
    lines = cv2.HoughLinesP(image, 1, np.pi/180, 180, minLineLength, maxLineGap)
    drawLines( image,lines)