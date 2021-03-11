import cv2

detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_extractor(img):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cropped_face=img[y:y+h, x:x+w]
        return cropped_face

cam = cv2.VideoCapture(0)
face_id=input('enter your id=')
count=0

while(True):
    ret, frame = cam.read()
    if face_extractor(frame) is not None:
         count+=1
         face=cv2.resize(face_extractor(frame),(200,200))
         face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

         file_name_path='C:/Users/lenovo/Desktop/project/DataSet/Person.'+face_id+'.'+str(count)+'.jpg'
         cv2.imwrite(file_name_path,face)

         cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
         cv2.imshow('Face Cropper',face)
    else:
        print("Please move in front of the WebCam....!!!")

    #wait for 100 miliseconds 
    #if cv2.waitKey(100) & 0xFF == ord('q'):
    if cv2.waitKey(300)==13 or count==10:
        break
print('Data has been collected.....')
cam.release()
cv2.destroyAllWindows()
