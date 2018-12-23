import numpy as np

# This array defines the vertices of the shape we want our image to have.
# Every pixel outside this shape will be darkened. I suggest not to mess with the order of the coordinates given below, unless it is completely understood
# what exactly is the shape of the Region of interest desired.

# tl;dr OpenCV draws the shape exactly as the order of vertices that you have given.
path_vertices = np.array([[0, 600],
            [0, 272],
            [240, 172],
            [560, 172],
            [800, 272],
            [800, 600],
            [600, 352],
            [200 , 352],
            [0, 600]
            ])


# Parameters that control which lines are drawn in the ROI processed image. You may need to tweak them until you get good edge detection
minLineLength = 350
maxLineGap = 10


# The controls to be used in the game
W = 0x0D
A = 0x00
S = 0x01
D = 0x02