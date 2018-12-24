# Logic is to take the screenshot, feed it into the model trained, and predict what to do.

import numpy as np
import cv2
import time
from PIL import ImageGrab, Image
from InputController import PressKey, ReleaseKey
from constants import W,A,S,D
from tensorflow_alexnet import alexnet
from RecordUserInput import key_check
from mss import mss

import random

WIDTH = 160
HEIGHT = 120
LR = 1e-03
EPOCHS = 10
t_time = 0.9
MODEL_NAME = 'car_racing_ai'

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)
def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def left():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(A)

def right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(D)

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
            prediction = model.predict([screen.reshape(160,120,1)])[0]
            print(prediction)
        turn_thresh = 0.25
        fwd_thresh = 0.50
        if prediction[1] > fwd_thresh:
            straight()
        elif prediction[0] > turn_thresh and prediction[0] > prediction[2]:
            left()
        elif prediction[2] > turn_thresh and prediction[2] > prediction[0]:
            right()
        else:
            straight()

        keys = key_check()
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
print('Lets begin')
screen_record()