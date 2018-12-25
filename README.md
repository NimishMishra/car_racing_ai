# car_racing_ai

[I am quite satisfied with the results. However, this model still needs a good deal of training data. I think applying RL to this scenario would be more interesting. This repo shall be reopened once I learn to apply RL on simple cases.]

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

7. GameControlAI.py - a simple algorithm to move the car about

However, the above logic is quite simple. We shall not be able to train on complex games.
Better to use a neural network instead.

1. RecordUserInput.py - a file that records the user input

2. NNTrainingData.py - a script to train the data for a neural network

3. BalanceData.py - script to remove most of 'forwards' so that the network doesn't overfit

4. tensorflow_alexnet.py - Tensorflow's implementation of a nice neural network

5. train_model. py - script to enable training of the model

6. Test_model.py - script to enable testing of the model
