import cv2

cap= cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

kernel = 5

print("'W' to increase blur and 'S' to decrease blur")

while cap.isOpened():
    success, frame=cap.read()
    if not success:
        print("ERROR webcam feed not available")
        break

    flip= cv2.flip(frame,1)

    gray= cv2.cvtColor(flip,cv2.COLOR_BGR2GRAY)

    blur= cv2.GaussianBlur(gray,(kernel,kernel),0)

    edges = cv2.Canny(blur,10,100)

    text= f"Kernel Size: {kernel}x{kernel}"
    cv2.putText(edges,text,(20,50),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),2,cv2.LINE_AA)

    cv2.imshow("original",flip)
    cv2.imshow("Interactive Canny Edges",edges)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('w'):
        kernel+=2

    elif key == ord('s'):
        if kernel>1:
            kernel-=2

    elif key == ord('q'):
        break