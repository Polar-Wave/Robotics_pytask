import cv2
import time

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

prevframetime = 0
newframetime = 0

img_counter = 0

cap.set(cv2.CAP_PROP_FPS, 30)

print("Press 's' to save a screenshot")
print("press 'q' to quit application")

while cap.isOpened():
    success, frame=cap.read()
    if not success:
        print("ERROR webcam feed not available")
        break
    
    #1 divided by time taken by each frame to get fps
    newframetime = time.time()
    timediff = newframetime - prevframetime
    fps=1/timediff if timediff>0 else 0
    prevframetime = newframetime

    fpstext = f"FPS:{int(fps)}"
    # to show fps as text on the feed
    cv2.putText(frame,fpstext,(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2,cv2.LINE_AA)

    cv2.imshow("webcam live feed", frame)
    
    #cap fps around 30
    key = cv2.waitKey(33) & 0xFF

    if key == ord('s'):
        img_name= f"img_{img_counter}.png"
        cv2.imwrite(img_name, frame)
        print(f"image saved as '{img_name}'")
        img_counter +=1

    elif key == ord('q'):
        print("shutting down feed")
        break

cap.release()
cv2.destroyAllWindows()