import time
#import numpy as np
import cv2

#cv2.imread() to read an image - image should be in a working directory or a full path of the image 
#paramter:1st is image file, 2nd is the way image should be read 
img = cv2.imread('test.png',0)
#cv2.imshow() to display image in window 
cv2.imshow('image',img)
#keyboard binding function - if 0 is passed, then it waits indefinitely until keyboard press
k = cv2.waitKey(0)
if k == 27:
	#destroy all windows after any key is pressed 
	cv2.destroyAllWindows()
elif k == ord('s'): #wait for 's' key to save image then exit
	#save image and destroy all windows
	cv2.imwrite('NewImageTesting.png',img)
	cv2.destroyAllWindows()
else:
	time.sleep(5)

