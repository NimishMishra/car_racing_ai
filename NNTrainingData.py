# We have developed a simple model that detect edges and drives using that. Now to more
# advanced techniques viz. neural networks.

# We shall be sending data manually to the neural network. We only need the screen image.

import numpy as np
from PIL import ImageGrab, Image
import cv2
import time
from mss import mss
from RecordUserInput import key_check
import os

def key_output(keys):
    output = [0, 0, 0]
    if 'A' in keys:
        output[0] = 1

    if 'D' in keys:
        output[2] = 1
    if 'W' in keys:
        output[1] = 1
    return output


file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    training_data = []

# capture_screenshot() applies the mss functions which I found to be faster than ImageGrab.grab() on my machine.
# The current FPS from mss is ~ 24 FPS. Grab the package from: https://github.com/BoboTiG/python-mss

def capture_screenshot():

    with mss() as sct:
        
        monitor = {"top": 50, "left": 0, "width": 800, "height": 600}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        sct_img = sct.grab(monitor)

        # Convert to PIL/Pillow Image
        return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')


def screen_record():
    paused = False
    while True:

        if not paused:
            screen = capture_screenshot()
            screen = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (160, 120))
            keys = key_check()
            output = key_output(keys)
            training_data.append([screen,output])

            if len(training_data) % 5000 == 0:
                print(len(training_data))
                np.save(file_name,training_data)
                break
        keys = key_check()
        print (output)
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)

time.sleep(2)
screen_record()