import cv2
image_path=r"C:\Users\91638\Documents\CV\venv\Scripts\Image Segmentation\cat.jpg"
image=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
_,thresholded=cv2.threshold(image,128,255,cv2.THRESH_BINARY)
print(thresholded)

"""
Definition: 

Thresholding is a simple segmentation technique where pixels in an image are classified as foreground or background based on a specified threshold value.

Real-world Explanation:

Imagine converting a grayscale image into a binary image where pixels above a certain intensity level are considered part of an object, and others are considered background.

Working: 

Pixels with intensity values above the threshold are set to one class, and pixels below are set to another.

Use Case: 

It is often used for basic object separation when the foreground and background have clear intensity differences.

Influence on CV: 

Thresholding is fundamental for creating binary masks, which are crucial in various computer vision applications.
"""
