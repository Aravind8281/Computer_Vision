import cv2
image_path = r"C:\Users\91638\Documents\CV\venv\Scripts\Feature Extraction\cat.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(image, None)
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None)
cv2.imshow("Image with SIFT Keypoints", image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
Definition:
SIFT is a feature extraction algorithm that identifies keypoints and computes descriptors invariant to scale and rotation.

Real-world Explanation:
SIFT keypoints are distinctive points in an image, and the descriptors encode information about the local image region around each keypoint.

Working:
SIFT detects keypoints in different scales and orientations, and the descriptors are based on the gradient information in the keypoint's neighborhood.

Use Case:
Image stitching, object recognition, and 3D reconstruction use SIFT for robust feature matching.

Influence on CV:
SIFT provides robustness to changes in scale, rotation, and illumination, making it suitable for various computer vision tasks.
"""
