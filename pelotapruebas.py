import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#cap = cv2.VideoCapture("C:/Users/vicen/Downloads/WIN_20231208_15_16_32_Pro.mp4")
#cap = cv2.VideoCapture("C:/Users/vicen/Downloads/WIN_20231208_15_17_00_Pro.mp4")

majinBooClassif = cv2.CascadeClassifier('C:/Users/vicen/Documents/Git/haar/cascade1hora.xml')

while True:
	
	ret,frame = cap.read()
	frame=cv2.resize(frame,(480,480))
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	toy = majinBooClassif.detectMultiScale(gray,
	scaleFactor = 5,
	minNeighbors = 90,minSize=(70,78))

	for (x,y,w,h) in toy:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		cx=int((x+(x+w))/2)
		cy=int((y+(y+h))/2)
		cv2.circle(frame, (cx, cy), radius=5, color=(0, 255, 0), thickness=1)
		cv2.putText(frame,'BALÓN',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

	cv2.imshow('frame',frame)
	
	if cv2.waitKey(1) == 27:
		break
cap.release()
cv2.destroyAllWindows()