from InputController import PressKey, ReleaseKey
from constants import W, S, A, D


def straight():
    PressKey(W)
    ReleaseKey(S)
    ReleaseKey(A)

def right():
    PressKey(D)
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(D)

def left():
    PressKey(A)
    ReleaseKey(W)
    ReleaseKey(D)
    ReleaseKey(A)

def decide_movement(slope1, slope2):
    # If we are between the two lanes
    if (slope1 < 0 and slope2 < 0):
        right()
    
    elif(slope1 > 0 and slope2 > 0):
        left()

    else:
        straight()