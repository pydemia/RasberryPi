#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 22:40:11 2017

@author: Young Ju Kim
"""

import time, pygame, matplotlib, math
import scipy as sp
from pygame.locals import KEYDOWN
import numpy as np
from PIL import Image, ImageDraw, ImageFont
#from scipy.misc import imread
import picamera
from picamera.array import PiRGBArray
import cv2


RESOLUTION = (480, 320)
# Import the face detection haar file
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_eye.xml')


camera = picamera.PiCamera()
camera.resolution = RESOLUTION
video = PiRGBArray(camera, size=RESOLUTION)

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Test")

try:
    for frameBuf in camera.capture_continuous(video, format ="rgb", use_video_port=True):
        frame = np.rot90(frameBuf.array, 3)
        video.truncate(0)
        surface = pygame.surfarray.make_surface(frame)
        screen.fill([0,0,0])
        screen.blit(surface, (0,0))
        pygame.display.update()

        image = np.rot90(frameBuf.array, 2)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(gray, 2, 5)

        if (len(faces) > 0): 
            faceFound = True
        else:
            faceFound = False

        if faceFound:
            print('Face Found!')
            for idx,(x,y,w,h) in enumerate(faces):
                img = np.array(image, dtype=np.uint8)
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h,x:x+w]
                roi_color = img[y:y+h,x:x+w]
                eyes=eye_cascade.detectMultiScale(roi_gray, 2,5)
                for eidx,(ex,ey,ew,eh) in enumerate(eyes):
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_s:
                    camera.capture('/home/pi/workspaces/camera/a.png', format='png')
                elif event.key == pygame.K_q:
                    raise KeyboardInterrupt
            elif event.type == pygame.QUIT:
                raise KeyboardInterrupt
           
except KeyboardInterrupt as SystemExit:
    pygame.quit()
    camera.close()
    video.close() 
