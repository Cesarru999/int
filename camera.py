#for this project, use a phone, conect pc and phne to the same network, install ip webcam android, start app and start server, copy the ip, and change the code.
import cv2 
import numpy as np
url = 'http://192.168.0.101:8080/video'
cap = cv2.VideoCapture(url)
while(True):
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('frame',frame)
    q = cv2.waitKey(1)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        cv2.destroyAllWindows()