# Edge Detection:

Definition:
Edge detection involves identifying boundaries within an image where there is a significant change in intensity. Edges often represent important features.

Real-world Explanation:
Think of it as outlining the contours in a picture, highlighting the transitions from one object to another.

Working:
Edge detection algorithms locate areas with high intensity gradients, where rapid changes in pixel values occur. Common methods include the Sobel operator or Canny edge detector.

Importance in Computer Vision:
Edges provide crucial information about the structure and boundaries of objects in an image. They serve as a foundation for object recognition and segmentation.

Use Case:
Example - Canny Edge Detection: Widely used for detecting edges in images, the Canny edge detector helps identify important features and is often a preprocessing step in object recognition

import cv2
import numpy
image = cv2.imread(r"C:\Users\91638\Pictures\Downloads\wallhaven-0jzjxw.jpg")
if image is None:
    print("Error")
    exit()

edge=cv2.Canny(image,50,150);
cv2.imshow("",edge)

cv2.waitKey(0)
