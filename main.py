import sched
import time
import torch
import numpy as np
import cv2
from check_place import check_place
from json_upload import json_upload
from organize_data import organize_data
from phone_detect import phone_detection


def detect():
	model = torch.hub.load('ultralytics/yolov5', 'yolov5x6')
	#mode = torch.hub.load('ultralytics/yolov5', 'custom', path='weight_pt/best.pt',device="cpu")
	#mode.conf=0.60
	
	frame=cv2.imread("test_pics/pic1.jpg")
	#res= mode(frame)
	results = model(frame)
	print(results.pandas().xyxy[0])
	print(results.pandas().xyxy[0].to_json(orient="records"))
	#cv2.imshow('YOLO',np.squeeze(results.render()))
	cv2.imwrite("img.jpg",np.squeeze(results.render()))
	json_upload(results)
	organize_data()
	check_place(frame, results)
	phone_detection(results)
	#gaze_detection(results)
	re = np.squeeze(results.render())
	return re
"""
	model = torch.hub.load('ultralytics/yolov5', 'yolov5x6')
	cap = cv2.VideoCapture(0)
	while cap.isOpened():
		ret, frame = cap.read()
		# persons and phone and tables
		results = model(frame)
		cv2.imshow('YOLO', np.squeeze(results.render()))
		print(results.pandas().xyxy[0].to_json(orient="records"))
		json_upload(results)
		organize_data()
		check_place(frame, results)
		phone_detection(results)
		#gaze_detection(results)
		re = np.squeeze(results.render())
		#return re
		if cv2.waitKey(10) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
	"""
detect()


