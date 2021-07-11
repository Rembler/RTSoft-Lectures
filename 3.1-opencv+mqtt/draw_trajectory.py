import numpy as np
import cv2 as cv
import time
import paho.mqtt.client as mqtt
import json

client =mqtt.Client("somename")
client.connect("localhost")

movie = cv.VideoCapture("LastTestVideo.mp4")

lst = []
avg_lst = []

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
		if y != 0 and w > 20 and h > 20:
			M = cv.moments(cnt)
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])
			point = [cx, cy]
			lst.append(point)
			if len(lst) > 1:
				avg_x = sum([lst[i][0] for i in range(max(-1,len(lst) - 40 - 1), len(lst) - 1)]) // min(len(lst), 40)
				avg_y = sum([lst[i][1] for i in range(max(-1,len(lst) - 40 - 1), len(lst) - 1)]) // min(len(lst), 40)
				point = [avg_x, avg_y]
				avg_lst.append(point)
			else:
				avg_lst.append(point)

			if len(lst) % 10 == 0:
				data = {"Real:": 
								{"x": lst[len(lst) - 1][0],
								 "y": lst[len(lst) - 1][1]},
						"Filtered":
								{"x": avg_lst[len(avg_lst) - 1][0],
								 "y": avg_lst[len(avg_lst) - 1][1]}}
				to_send = json.dumps(data)
				client.publish("video/data", to_send)

		if len(lst) > 2:
			i = 0
			while i < len(lst) - 1:
				cv.line(frame, (lst[i][0],lst[i][1]), (lst[i+1][0],lst[i+1][1]), (255,0,0), 5)
				cv.line(frame, (avg_lst[i][0],avg_lst[i][1]), (avg_lst[i+1][0],avg_lst[i+1][1]), (0,255,0), 5)
				i += 1

	cv.imshow('frame', frame)
	time.sleep(0.07)
	if cv.waitKey(1) == ord('q'):
		break

movie.release()

cv.destroyAllWindows()
