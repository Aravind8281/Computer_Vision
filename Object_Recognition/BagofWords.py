import cv2
import numpy as np
from sklearn.cluster import KMeans
image = cv2.imread(r'C:\Users\91638\Documents\CV\venv\Scripts\Object detection\human.jpg', cv2.IMREAD_GRAYSCALE)
sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(image, None)# Feature Extraction
kmeans = KMeans(n_clusters=50)# Build vocabulary
kmeans.fit(descriptors)
histogram = np.histogram(kmeans.labels_, bins=np.arange(51))[0]# Histogram representation
print(histogram)


"""
Definition:
Bag of Visual Words is an image representation model inspired by text retrieval models. It treats an image as an unordered set of local features, discarding spatial information, and creates a "vocabulary" of visual words to represent the image.

Real-world Explanation:
Consider an image as a collection of visual words. These words represent distinctive features, and the arrangement of these features doesn't matter, similar to how words in a bag don't have a specific order.

Working:

Feature Extraction:

Extract local features (e.g., SIFT) from the image.
Build Vocabulary:

Cluster the features to create a visual vocabulary (k-means clustering).
Histogram Representation:

Represent the image as a histogram of visual words, counting the occurrences of each word.
Use Case:
Object recognition and scene categorization where spatial relationships between features are less important than the presence of distinctive visual elements.

Influence on CV:
BoVW simplifies image representation and allows for efficient comparison between images. It's computationally less expensive compared to methods considering spatial information.

Code (Python - O
"""
