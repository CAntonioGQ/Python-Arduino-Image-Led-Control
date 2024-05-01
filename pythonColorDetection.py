import cv2
import numpy as np
import serial

ser = serial.Serial('COM3', 9600)  # Puerto
cap = cv2.VideoCapture(0)

redBajo1 = np.array([0, 80, 20], np.uint8)
redAlto1 = np.array([10, 255, 255], np.uint8)
redBajo2 = np.array([170, 100, 20], np.uint8)
redAlto2 = np.array([180, 255, 255], np.uint8)
redBajo3 = np.array([160, 100, 20], np.uint8)
redAlto3 = np.array([179, 255, 255], np.uint8)

greenBajo1 = np.array([40, 100, 20], np.uint8)
greenAlto1 = np.array([80, 255, 255], np.uint8)
greenBajo2 = np.array([80, 100, 20], np.uint8)
greenAlto2 = np.array([100, 255, 255], np.uint8)
greenBajo3 = np.array([50, 100, 20], np.uint8)
greenAlto3 = np.array([70, 255, 255], np.uint8)

while True:
    ret, frame = cap.read()
    if ret == True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
        maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
        maskRed3 = cv2.inRange(frameHSV, redBajo3, redAlto3)
        maskRed = cv2.add(cv2.add(maskRed1, maskRed2), maskRed3)
        maskRedvis = cv2.bitwise_and(frame, frame, mask=maskRed)
        
        maskGreen1 = cv2.inRange(frameHSV, greenBajo1, greenAlto1)
        maskGreen2 = cv2.inRange(frameHSV, greenBajo2, greenAlto2)
        maskGreen3 = cv2.inRange(frameHSV, greenBajo3, greenAlto3)
        maskGreen = cv2.add(cv2.add(maskGreen1, maskGreen2), maskGreen3)
        maskGreenvis = cv2.bitwise_and(frame, frame, mask=maskGreen)
        
        if np.sum(maskRed) > 0:
            ser.write(b'R')
        elif np.sum(maskGreen) > 0:
            ser.write(b'G')
        else:
            ser.write(b'N')
        
        # cv2.imshow("frame", frame)
        cv2.imshow("maskRedvis", maskRedvis)
        cv2.imshow("maskGreenvis", maskGreenvis)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
ser.close()