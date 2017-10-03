
# coding: utf-8

# In[ ]:




# In[ ]:

import os
import cv2
import numpy as np
from tqdm import tqdm
import argparse


#function to create and save training data and resize it to 100*100 pixels
def create_train_data():
    i = 0
    
    training_output = []
    training_input = []
    for img in tqdm(os.listdir(TRAININ_DIR)):
        path = os.path.join(TRAININ_DIR,img)
        img = cv2.imread(path)
        try:
            img = cv2.resize(img, (100,100))
            training_input.append([np.array(img)])
        except Exception:
            pass
        #saves only first 100000 imagres
        if i == 100000:
            break
        
    i = 0 

    # creating training output
    for img in tqdm(os.listdir(TRAINOUT_DIR)):
        path = os.path.join(TRAINOUT_DIR,img)
        img1 = cv2.imread(path)
        try:
            img1 = cv2.resize(img1, (100,100))
            training_output.append([np.array(img1)])
        except Excepion:
            pass
        i = i + 1
        if i == 100000:
            break
        
    
    
   
    np.save('training_input_cropped.npy', training_input)
    np.save('training_output_cropped.npy', training_output)
    
    return training_input, training_output

if __name__ == '__main__':
    
    
    # training directories
    TRAININ_DIR = 'crop_sketches'
    TRAINOUT_DIR = 'crop'
    create_train_data()


