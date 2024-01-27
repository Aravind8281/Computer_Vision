import cv2

# Load an image
image = cv2.imread(r'C:\Users\91638\Documents\CV\venv\Scripts\Object detection\human.jpg', cv2.IMREAD_GRAYSCALE)
sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(image, None)
output_image = cv2.drawKeypoints(image, keypoints, None)
cv2.imshow('Keypoints', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
Definition:
Spatial Pyramid Matching is a technique used in computer vision for image recognition. It involves dividing an image into sub-regions and representing each sub-region with histograms of local features. These histograms are then combined in a hierarchical manner to capture both local and global information.

Real-world Explanation:
Imagine you want to recognize objects in an image. SPM breaks down the image into various regions, analyzes each region's features, and then combines these features to understand both the detailed and overall characteristics of the image.

Working:

Divide the Image:

The image is divided into different levels of sub-regions, forming a pyramid structure.
Extract Local Features:

Local features, such as SIFT or HOG descriptors, are computed for each sub-region.
Histogram Representation:

Histograms are created for each sub-region based on the local features.
Combine Hierarchically:

Histograms from different levels of the pyramid are combined hierarchically to create a comprehensive representation of the entire image.
Use Case:
Object recognition in images where the location and arrangement of features are crucial. SPM is often used in scenes with varying object scales and positions.

Influence on Computer Vision (CV):
SPM enhances the performance of computer vision systems by incorporating both local and global information. It allows models to capture spatial relationships between features, making it robust to changes in object position and scale
"""
