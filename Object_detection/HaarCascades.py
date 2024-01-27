import cv2
face=cv2.CascadeClassifier(r'C:\Users\91638\Documents\CV\venv\Scripts\Object detection\haarcascade_frontalface_default.xml')
img=cv2.imread(r"C:\Users\91638\Documents\CV\venv\Scripts\Object detection\human.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('faces',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
Haar cascades are a machine learning object detection method used to identify objects in images or video. They use a set of Haar-like features and a cascade classifier to detect objects of interest.
"""
