#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

# Colour detection limits
lB = 125
lG = 125
lR = 125
hB = 255
hG = 255
hR = 255

def main():
    # Open the camera
    camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
    
    while True:
        # Read the image from the camera
        ret, frame = camera.read()

        # You will need this later
        # frame = cv2.cvtColor(frame, ENTER_CORRECT_FLAG_HERE)

        # Colour detection limits
        lower_limits = np.array([lB, lG, lR])
        upper_limits = np.array([hB, hG, hR])

        # Our operations on the frame come here
        thresholded = cv2.inRange(frame, lower_limits, upper_limits)

        cv2.imshow("Original", frame)

        # Display the resulting frame
        cv2.imshow("Thresholded", thresholded)

        # Quit the program when "q" is pressed
        if (cv2.waitKey(1) & 0xFF) == ord("q"):
            break

    # When everything done, release the camera
    print("Closing program")
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
