# Import the library
import cv2
import numpy as np
# Creating a LBPHFaceRecognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
# Taking Path of Our Trained Model and Reading the File
recognizer.read('C://Users//Sunil Yadav//OneDrive//Desktop//Python Projects//Git Hub//trainningData.yml')
#Giving the Path of haarcascade_frontalface_default
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

# Opening tHe Web_cam
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
while True:
    ret, img =cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    # Drawing The rectangle
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        if (confidence < 57):
            if(id==1):
                id='Sunil Yadav'
                confidence = "  {0}%".format(round(100 - confidence))
            elif(id==2):
                id='Prince Kumar'
                confidence = "  {0}%".format(round(100 - confidence))

            elif(id==3):
                id='Rahul'
                confidence = "  {0}%".format(round(100 - confidence))

        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(
                    img,
                    str(id),
                    (x+5,y-5),
                    font,
                    1,
                    (255,255,255),
                    2
                   )
        cv2.putText(
                    img,
                    str(confidence),
                    (x+5,y+h-5),
                    font,
                    1,
                    (255,255,0),
                    1
                   )

    cv2.imshow('camera',img)
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
