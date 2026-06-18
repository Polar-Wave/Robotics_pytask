import cv2
import numpy as np

image = cv2.imread('noiseimg.jpg')

if image is None:
    print("ERROR, couldnt find image")
else:
    print("File succesfully read")

    height,width,channels =image.shape
    pixels=height*width

    print(f"Dimensions: {width}x{height} pixels")
    print(f"Pixel Count: {pixels:,} pixels")

    gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    denoised = cv2.fastNlMeansDenoisingColored(image, None, h=10, hColor=10,templateWindowSize=7, searchWindowSize=21)

    cv2.imwrite('cleaned.png', denoised)
    print("\nDenoised copies saved to your folder.")

    cv2.imshow("Original Noisy Image", image)
    cv2.imshow("Denoised", denoised)
    
    print("\nPress any key inside the image windows to exit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()