import cv2
import numpy as np

image = cv2.imread('channel.jpg')

if image is None:
    print("ERROR, couldnt find image")
else:
    print("File succesfully read")

    b,g,r= cv2.split(image)

    blank= np.zeros_like(b)

    tleft_b= cv2.merge([b,blank,blank])
    tright_g= cv2.merge([blank,g,blank])
    bleft_r= cv2.merge([blank,blank,r])
    bright= cv2.merge([b,blank,r])

    top = np.hstack((tleft_b,tright_g))
    bottom = np.hstack((bleft_r,bright))
    final= np.vstack((top,bottom))

    cv2.imwrite('all_channels.png',final)

    cv2.imshow("all channels",final)

    cv2.waitKey(0)
    cv2.destroyAllWindows