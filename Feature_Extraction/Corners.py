import cv2 as cv
image_path = r"C:\Users\91638\Documents\CV\venv\Scripts\Feature Extraction\cat.jpg"
image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
if image is None:
    print(f"Error: Unable to read the image at {image_path}")
    exit()
corners = cv.goodFeaturesToTrack(image, maxCorners=100, qualityLevel=0.01, minDistance=10)
if corners is not None:
    corners = corners.astype(int)
    for c in corners:
        x, y = c.ravel()
        cv.circle(image, (x, y), 3, 255, -1)
    cv.imshow('Corners', image)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("No corners were found.")


"""Definition:
Corners are points in an image where the intensity gradients change abruptly in multiple directions. Keypoints are specific locations in an image identified as distinctive and suitable for matching.

Real-world Explanation:
Imagine a corner of a book cover. The meeting point of the edges represents a corner, and a unique pattern of edges forms a keypoint.

Working:
Corners are detected by looking for significant changes in intensity in different directions. Keypoints are identified based on local extrema in feature space.

Use Case:
Image stitching applications use keypoints to match corresponding points in different images for creating a panorama.

Influence on CV:
Corners and keypoints serve as anchor points for matching and registration tasks, contributing to the robustness of computer vision algorithms."""
