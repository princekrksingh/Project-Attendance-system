import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(img,"Cat",(x,y-10),font,0.55,(0,255,0),1)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf>50):
            if(Id==1):
                Id="Rahul"
            elif(Id==2):
                Id="Sai Pallavi"
            elif(Id==3):
                Id="College crush"
        else:
            Id="Unknown"
        cv2.putText(Person,str(Id), (x,y+h),font,0.55,(0,255,0),1)
    cv2.imshow('im',Person) 
    if cv2.waitKey(10)==13:
        break
cam.release()
cv2.destroyAllWindows()
