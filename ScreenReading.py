
import numpy as np
from PIL import ImageGrab, Image
import cv2
import time
from mss import mss

# capture_screenshot() applies the mss functions which I found to be faster than ImageGrab.grab() on my machine.
# The current FPS from mss is ~ 24 FPS. Grab the package from: https://github.com/BoboTiG/python-mss

def capture_screenshot():

    with mss() as sct:
        
        monitor = {"top": 50, "left": 10, "width": 800, "height": 640}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        sct_img = sct.grab(monitor)

        # Convert to PIL/Pillow Image
        return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

# screen_record() uses the functionality from capture_screenshot() to get a real-time record of the screen.

def screen_record(): 
    while True:
        screen =  capture_screenshot()
        cv2.imshow('window', cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB))
        if(cv2.waitKey(25) & 0xFF == ord('q')):
            cv2.destroyAllWindows()
            break      

screen_record()
