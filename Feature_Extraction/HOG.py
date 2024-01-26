import cv2
import numpy
imagepath=r"C:\Users\91638\Documents\CV\venv\Scripts\Feature Extraction\cat.jpg"
image=cv2.imread(imagepath,cv2.IMREAD_GRAYSCALE)
if image is None:
    print("No image found")
hog=cv2.HOGDescriptor()
features =hog.compute(image)
print(features)

"""
Definition:
HOG is a feature descriptor that represents the distribution of gradient orientations in an image.

Real-world Explanation:
In an image, the HOG descriptor captures the information about the direction of edges, emphasizing the structure and shape of objects.

Working:
HOG computes histograms of gradient orientations in local image regions and concatenates them to create a feature vector.

Use Case:
Object detection, particularly in pedestrian detection, uses HOG as a feature descriptor.

Influence on CV:
HOG is effective for capturing object shape and structure, making it a valuable tool in object recognition and detection.

"""
