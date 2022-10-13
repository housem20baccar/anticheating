import dlib
import cv2
def midpoint(p1, p2):
	return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)
def gaze_detection(result,img):
	res = result.pandas().xyxy[0].to_json(orient="records")
	for s in range(len(res)):
		if res[s]["name"] == "person":
			pos = {"xmin": res[s]["xmin"], "ymin": res[s]["ymin"], "xmax": res[s]["xmax"], "ymax": res[s]["ymax"]}
			top = int(res[s]["ymin"])
			right = int(res[s]["xmin"])
			height = int(res[s]["ymax"])
			width = int(res[s]["xmax"])
			crop = img[top:height, right:width]
			detector = dlib.get_frontal_face_detector()
			predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
			gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
			face = detector(gray)
			landmarks = predictor(gray, face)
			left_point = (landmarks.part(36).x, landmarks.part(36).y)
			right_point = (landmarks.part(39).x, landmarks.part(39).y)
			center_top = midpoint(landmarks.part(37), landmarks.part(38))
			center_bottom = midpoint(landmarks.part(41), landmarks.part(40))