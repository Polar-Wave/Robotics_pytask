import cv2
import numpy as np
import mediapipe as mp
import os

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands = 1, min_detection_confidence = 0.85, min_tracking_confidence = 0.85)

drawclr = (0,0,255)
brthick = 5
px,py = 0,0

board = np.ones((720,1280,3), dtype=np.uint8)*255

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

while cap.isOpened():
    success, frame=cap.read()
    if not success:
        break
    frame = cv2.flip(frame,1)

    frame = cv2.cvtcolor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(frame)
    
    drawing= False

    if result.multi_hand_landmarks:
        for hand_lms in result.multi_hand_landmarks:
            h,w,_ = frame.shape
            landmarks=[]
            for lm in hand_lms.landmark:
                cx,cy = int(lm.x*w), int(lm.y*h)
                landmarks.append((cx,cy))

            if landmarks:
                x1, y1 = landmarks[8]
                x2, y2 = landmarks[12]

                fingers = []
                fingers.append(1 if landmarks[8][1]<landmarks[6][1] else 0)
                fingers.append(1 if landmarks[12][1]<landmarks[10[1]] else 0)

                if fingers[0]==1 and fingers[1]==1:
                   px,py=0,0
                   cv2.circle(frame,(x1,y1),15,(255,0,0),cv2.FILLED)

                elif fingers[0]==1 and fingers[1]==0:
                   cv2.circle(frame,(x1,y1),10, drawclr ,cv2.FILLED)
                   
                   if px==0 and py==0:
                       px,py = x1,y1

                   cv2.line(board,(px,py),(x1,y1),drawclr,brthick)
                   cv2.line(frame,(px,py),(x1,y1),drawclr,brthick)
                   px,py =x1,y1
 
    img_gray=cv2.cvtColor(board, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, img_inv)
    frame = cv2.bitwise_or(frame, board)

    cv2.imshow("Virtual Drawing Board (Camera View)",frame)
    cv2.imshow("Canvas Output File Preview",board)

    key = cv2.waitkey(1) & 0xFF
  
    if key ==ord('s'):
       filename = "my_drawing.png"
       cv2.imwrite(filename,board)
       print(f"Drawing saved to project folder as '{filename}'")

    elif key == ord('c'):
       board = np.ones((720,1280,3), dtype=np.uint8)*255
       print("canvas cleared")

    elif key == ord('q'):
       break

cap.release()
cv2.destroyAllWindows()