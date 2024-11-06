#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

#camera = cv2.VideoCapture(0, cv2.CAP_V4L2)

# default trackbar value
trackbar_value = 127

def update_exposure(new):
    global trackbar_value
    trackbar_value = new
    #camera.set(cv2.CAP_PROP_EXPOSURE, new)

def main():
    # Working with image files stored in the same folder as .py file
    file = "sample01.tiff"

    # Load the image from the given location
    img = cv2.imread(file)

    # Load the image from the given location in greyscale
    img_greyscale = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    # Create a named window and name it "Output"
    cv2.namedWindow("Output")
    # Attach a trackbar to a window named "Output"
    cv2.createTrackbar("Threshold", "Output", int(trackbar_value), 500, update_exposure)


    while True: 
        # Thresholding the grayscaled image 
        ret, thresh = cv2.threshold(img_greyscale, trackbar_value, 255, cv2.THRESH_BINARY)
    
        # Display the images
        cv2.imshow("Original", img)
        cv2.imshow("Output", thresh)

        # Quit the program when "q" is pressed
        if (cv2.waitKey(1) & 0xFF) == ord("q"):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
