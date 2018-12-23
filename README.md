# car_racing_ai

This repo is about training a car to win a racing video game.

Special packages used:

1. OpenCV
2. mss (https://github.com/BoboTiG/python-mss)
3. Python Imaging Library
4. Quartz (pip install pyobjc-framework-Quartz)

Scripts:

1. ScreenReading.py - to capture the screen in real-time that can be 
                      used for training purposes

2. EdgeDetection.py - uses Canny edge detection algorithm to detect
                      edges in the captured screen  

3. InputController.py -  script to automate keyboard inputs to the game

4. RegionOfInterestDetection.py - Detects the region to be processed based on the path vertices described

5. constants.py - Defines the constants to be used elsewhere

6. LineDetection.py - detects and draws lines on edges
