#import the libraries
import cv2 as cv
import numpy as np

#read the image
img = cv.imread("D://MSc Project//Experiment Videos//Retinol//Red_test.png")

# Split the image into its BGR channels
b, g, r = cv.split(img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Reduce the intensity of the red channel
#reduced_r = cv.subtract(r, 250)  # You can adjust the subtraction value
#reduced_g = cv.subtract(g, 150)  # You can adjust the subtraction value

# Combine the modified channels to form the new image
#new_img = cv.merge((cv.subtract(b, 50), reduced_g, reduced_r))

#create resizable windows for displaying the images
cv.namedWindow("original", cv.WINDOW_NORMAL)
cv.namedWindow("new_img", cv.WINDOW_NORMAL)

#display the images
cv.imshow("original", img)
cv.imshow("new_img", gray)

if cv.waitKey(0):
    cv.destroyAllWindows()
