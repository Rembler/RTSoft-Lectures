import numpy as np
import cv2 as cv
import time

movie = cv.VideoCapture("video_name.mp4")

while movie.isOpened():
	ret, frame = movie.read()

	if not ret:
		print("Can not get a frame. Perhaps stream has ended.")
		break
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	ret,thresh = cv.threshold(gray,127,255,0)
	contours,hierarchy = cv.findContours(thresh, 1, 2)

	for cnt in contours:
		x,y,w,h = cv.boundingRect(cnt)
		if y != 0 and w > 10 and h > 10:
			cv.rectangle(frame,(x,y),(x+w,y+h),(0,255.0),2)

	cv.imshow('frame', frame)
	time.sleep(0.01)
	if cv.waitKey(1) == ord('q'):
		break

movie.release()
cv.destroyAllWindows()
