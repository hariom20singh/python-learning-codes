import os
import cv2
import numpy as np
import mediapipe as mp

image_path = 'images'
images = os.listdir(image_path)

image_index= 0
bg_image = cv2.imread(image_path+'/'+images[image_index])
