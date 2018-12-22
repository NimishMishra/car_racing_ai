import numpy as np
import cv2


# detect_edges() applies Canny edge detection algorithm to the captured image. The required thresholds have been calculated 
# using the median of the initial image
def detect_edges(colored_image):
    greyed_image = cv2.cvtColor(np.array(colored_image), cv2.COLOR_BGR2GRAY)
    v = np.median(greyed_image)
    sigma = 0.33
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    processed_image = cv2.Canny(greyed_image, threshold1 = lower, threshold2 = upper)
    return processed_image



