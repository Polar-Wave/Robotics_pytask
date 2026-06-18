import cv2

# Operation 1: Loading the image
frame = cv2.imread("channel.jpg")

# Operation 2: Converting color space
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Operation 3: Drawing a bounding box
cv2.rectangle(gray_frame, (10, 10), (100, 100), (0, 255, 0), 3)

# Operation 4: Displaying the result
cv2.imshow("view", gray_frame)
cv2.waitKey(1) 

'''option A is incorrect as it loads image in BGR format
   option B is correct, the rectangle is in grayscale
   option C is correct, after 1 milisfcond the window closes instantly
   option D is incorrent as these values are the the top left point and bottom right point of rectangle'''