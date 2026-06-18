import cv2
import mediapipe as mp
import math

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)

led_on = False         
pinch_cooldown = False  #to stop toggling continuosly
cooldown_frames = 0     

print("Pinch your Thumb and Index Finger tips tightly together to toggle state to ON or OFF.")
print("Press 'q' to exit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgbframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgbframe)

    #to cause half second delyas in toggling so as to provide smooth toggling
    if pinch_cooldown:
        cooldown_frames += 1
        if cooldown_frames > 15: 
            pinch_cooldown= False
            cooldown_frames= 0

    if result.multi_hand_landmarks:
        for hand_lms in result.multi_hand_landmarks:
            # Index 4 is Thumb Tip | Index 8 is Index Finger Tip
            thumb= hand_lms.landmark[4]
            index= hand_lms.landmark[8]

            tx,ty= int(thumb.x * w), int(thumb.y * h)
            ix,iy= int(index.x * w), int(index.y * h)

            cv2.circle(frame, (tx, ty), 8, (255, 255, 0), cv2.FILLED) 
            cv2.circle(frame, (ix, iy), 8, (255, 255, 0), cv2.FILLED)

            distance= math.sqrt((tx - ix)**2 +(ty - iy)**2)

            # A distance below 40 pixels is condition for toggling
            if distance < 40:
                if not pinch_cooldown:
                    led_on = not led_on 
                    pinch_cooldown = True 

    
    if led_on:
        led = (0, 255, 0) 
        text = "SYSTEM STATUS: ON"
    else:
        led = (0, 0, 255) 
        text = "SYSTEM STATUS: OFF"

    cv2.circle(frame, (100, 100), 30, led, cv2.FILLED)
    cv2.circle(frame, (100, 100), 32, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.putText(frame, text,(160, 110),cv2.FONT_HERSHEY_SIMPLEX,1,led,2,cv2.LINE_AA)
    
    cv2.imshow("Interface", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()