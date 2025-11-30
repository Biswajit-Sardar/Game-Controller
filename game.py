import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Controller,Key


#hand detector with a detection confidence 
detector = HandDetector(detectionCon=0.3 , maxHands=1)  

#keyboard controller
keyboard= Controller()



cap=cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,720)
while True:
    _, img=cap.read()  # Read the frame from the camera and store it in img , ( _,) means we are ignoring the first return value
    img = cv2.flip(img, 1)
    hand,img= detector.findHands(img) # Detect hands in the image

    if hand:
        finger=detector.fingersUp(hand[0])  # Get the status of each finger (up or down)
        print(finger)

