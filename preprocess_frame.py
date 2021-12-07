"""

import cv2
import numpy as np


def resize_frame(frame):
    frame = frame[28:,5:-4]
    frame = np.average(frame,axis = 2)
    frame = cv2.resize(frame,(84,84),interpolation = cv2.INTER_NEAREST)
    frame = np.array(frame,dtype = np.uint8)
    return frame
"""
#en esta parte del código lo que se hace en recortar la imagen y usar el cv2 para detectar los puntos convirtiendolos a enteros.
import cv2
import numpy as np


def resize_frame(frame):
    frame = frame[30:-12,5:-4]
    frame = np.average(frame,axis = 2)
    frame = cv2.resize(frame,(84,84),interpolation = cv2.INTER_NEAREST)
    frame = np.array(frame,dtype = np.uint8)
    return frame