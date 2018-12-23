
import numpy as np
from PIL import ImageGrab, Image
import cv2
import time
from mss import mss
from EdgeDetection import detect_edges
from constants import path_vertices
from RegionOfInterestDetection import Detect_roi
from LineDetection import detect_lines
from GameControlAI import decide_movement

def process_screen(screen):
        original_screen = screen
        processed_screen = detect_edges(screen)
        gaussain_processed = cv2.GaussianBlur(processed_screen, (5,5), 0)
        roi_processed = Detect_roi(gaussain_processed, [path_vertices])
        processed, original, slope1, slope2 = detect_lines(original_screen, roi_processed)
        return processed, original, slope1, slope2

# capture_screenshot() applies the mss functions which I found to be faster than ImageGrab.grab() on my machine.
# The current FPS from mss is ~ 24 FPS. Grab the package from: https://github.com/BoboTiG/python-mss



def capture_screenshot():

    with mss() as sct:
        
        monitor = {"top": 50, "left": 0, "width": 800, "height": 600}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        sct_img = sct.grab(monitor)

        # Convert to PIL/Pillow Image
        return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

# screen_record() uses the functionality from capture_screenshot() to get a real-time record of the screen.

def screen_record(): 
    while True:
        start = time.time()
        screen =  capture_screenshot()
        screen = np.array(screen) # Quite an important line. This was causing the whole logic to fall off.
        new_screen, original_screen, slope1, slope2 = process_screen(screen)
        #cv2.imshow('game', np.array(new_screen))
        #cv2.imshow('game2', cv2.cvtColor(np.array(original_screen), cv2.COLOR_BGR2RGB))
        decide_movement(slope1, slope2)
        end = time.time()
        print(end - start)
        if(cv2.waitKey(25) & 0xFF == ord('q')):
            cv2.destroyAllWindows()
            break  
        

screen_record()