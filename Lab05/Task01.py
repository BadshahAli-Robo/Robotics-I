#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import time

def main():
    # Open the camera
    camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
    
    prev_time = time.time()
    fps = 0
    
    while True:
        # Read the image from the camera
        ret, frame = camera.read()
        
        #calculate fps
        curr_time = time.time()
        #as fps is calculated the reciprocal of time difference between frames
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time
        
        #to write the calculated fps on frame
        cv2.putText(frame, f"FPS: {fps:.2f}", (5, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)

        # Write some text onto the frame
        cv2.putText(frame, "Hello Ali Badshah", (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Show this image on a window named "Original"
        cv2.imshow("Original", frame)

        # Quit the program when "q" is pressed
        if (cv2.waitKey(1) & 0xFF) == ord("q"):
            break

    # When everything is done, release the camera
    print("Closing program")
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

