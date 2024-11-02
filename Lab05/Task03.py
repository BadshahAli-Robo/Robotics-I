#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
trackbar_value = 127

def update_exposure(new):
    global trackbar_value
    trackbar_value = new

def main():
    # Working with image files stored in the same folder as .py file
    file = "sample01.tiff"
    # Load the image from the given location
    img = cv2.imread(file)
    # Load the image from the given location in greyscale
    img_greyscale = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    
    #to set up SimpleBlobDetector parameters
    blobparams = cv2.SimpleBlobDetector_Params()
    
    # filtering blobs by area
    blobparams.filterByArea = True
    blobparams.minArea = 1000
    blobparams.maxArea = 100000
    
    blobparams.filterByCircularity = False
    #blobparams.minCircularity = 1
    
    # and doesn't matter if its one side is much longer than the other
    blobparams.filterByInertia = False
    # and doesn't matter whether it's concave and/or has holes inside
    blobparams.filterByConvexity = False
    # and we don't want to detect every single small speck in the proximity
    blobparams.minDistBetweenBlobs = 100
    
    #to create a detector with blobparams as an input
    detector = cv2.SimpleBlobDetector_create(blobparams)
    
    # Create a named window and name it "Output"
    cv2.namedWindow("Threshold")
    # Attach a trackbar to a window named "Output"
    cv2.createTrackbar("Threshold", "Threshold", int(trackbar_value), 255, update_exposure)

    while True: 
        # Thresholding the grayscaled image 
        _, thresh = cv2.threshold(img_greyscale, trackbar_value, 255, cv2.THRESH_BINARY)
        
        keypoints = detector.detect(thresh)
        output_img = cv2.drawKeypoints(img, keypoints, None, (0, 255, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        
        for idx, keypoint in enumerate(keypoints):
            x, y = int(keypoint.pt[0]), int(keypoint.pt[1])
            cv2.putText(output_img, f"{idx}: ({x}, {y})", (x+15, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
            
        # Display the images
        cv2.imshow("Original", output_img)
        cv2.imshow("Threshold", thresh)

        # Quit the program when "q" is pressed
        if (cv2.waitKey(1) & 0xFF) == ord("q"):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


