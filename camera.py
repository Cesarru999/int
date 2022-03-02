import cv2
import sys
import random
faceCascade = cv2.CascadeClassifier('C:/Users/Verona/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not video_capture.isOpened():
    raise IOError("Cannot open webcam")

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    n=0
    for (x, y, w, h) in faces:
        n += 1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 2)
        cv2.putText(frame, f"Face {n}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
		0.55, (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.putText(frame, f"Total people: {n}", (1,25), cv2.FONT_HERSHEY_SIMPLEX,
		0.50, (255, 80, 0), 2)
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()