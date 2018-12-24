import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

# Load the training data. Ensure directory path is correct. 
# For safety, keep the training data in the same directory as the code file
train_data = np.load('training_data_1.npy')

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts = []
rights = []
forwards = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1,0,0] or choice == [1, 1, 0]:
        lefts.append([img,choice])
    elif choice == [0,1,0]:
        forwards.append([img,choice])
    elif choice == [0,0,1] or choice == [0, 1, 1]:
        rights.append([img,choice])
    else:
        print('no matches')

# Making sure all are of the same length
forwards = forwards[:len(lefts)][:len(rights)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]

final_data = forwards + lefts + rights
shuffle(final_data)

np.save('finally_balanced_training_data.npy', final_data)
print(len(lefts))
print(len(rights))
print(len(forwards))