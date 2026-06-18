import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)

while cap.isOpened():
    success, frame=cap.read()
    if not success:
        print("ERROR webcam feed not available")
        break

    flipped = cv2.flip(frame,1)

    height, width,_ = frame.shape
    widthh= int(width/2)
    heighth= int(height/2)

    downscale= cv2.resize(flipped,(widthh,heighth), interpolation=cv2.INTER_LINEAR)

    gray = cv2.cvtColor(downscale, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Requested flipped gray Feed(q to close)",gray)

    quarter= cv2.resize(frame,(widthh,heighth),interpolation=cv2.INTER_LINEAR)

    tleft= quarter.copy()

    tright= cv2.flip(quarter,0)

    bleft= cv2.cvtColor(quarter, cv2.COLOR_BGR2HSV)

    b,g,r =cv2.split(quarter)
    blank= np.zeros_like(r)
    bright= cv2.merge([blank,blank,r])

    top= np.hstack((tleft,tright))
    bottom= np.hstack((bleft,bright))
    final= np.vstack((top,bottom))

    cv2.imshow("4 Window View(q to close)",final)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()