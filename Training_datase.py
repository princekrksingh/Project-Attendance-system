# Importing the required library
import os
import cv2
import numpy as np
from PIL import Image


recognizer = cv2.face.LBPHFaceRecognizer_create()
# Giving Path of Data dataset
path='C://Users//Sunil Yadav//OneDrive//Desktop//Python Projects//Git Hub//dataset'
# Function
def getImagesWithID(path):
	imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
	faces=[]
	IDs=[]
	for imagePath in imagePaths:
		faceImg=Image.open(imagePath).convert('L');
		faceNp=np.array(faceImg,'uint8')
		ID=int(os.path.split(imagePath)[-1].split('.')[1])
		faces.append(faceNp)
		print( ID)
		IDs.append(ID)
		cv2.imshow("training",faceNp)
		cv2.waitKey(10)
	return IDs,faces

Ids,faces=getImagesWithID(path)
recognizer.train(faces,np.array(Ids))
# Path of Saving the Training File
recognizer.save('C://Users//Sunil Yadav//Desktop//Git Hub//trainningData.yml')
print("Successfully Trained The DataSet")
# Destroying the windows
cv2.destroyAllWindows()
