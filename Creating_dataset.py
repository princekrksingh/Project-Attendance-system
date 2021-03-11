# Importing the library cv2
import cv2
# Now we have to  ask for Id as a Input of a Users
face_id=input('Please Enter The Id Of User:=\t')
# Now we have to use a file haarcascade_frontalface_default.xml for Cascade
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Now we have to Open the Web cam for Cpturing the data scaleFactor
video_capture=cv2.VideoCapture(0,cv2.CAP_DSHOW)
#Now we will define a count to count the Number of frame with 0
count=0
while True:
    #Capturing frame-by-frame
    ret,frame=video_capture.read()
    #Concerting the frames into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255,0), 3)
        count += 1
        #Now saving The Frames
        cv2.imwrite("dataset/User." + str(face_id) +'.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    elif count>=100:
        print("Successfully Captured")
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
