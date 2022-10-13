import json as js
from simple_facerec import SimpleFacerec


def check_id(frame):
	sfr = SimpleFacerec()
	sfr.load_encoding_images("students")
	face_location, face_name = sfr.detect_known_faces(frame)
	if face_name == -1:
		print("student dosen't exist")
	else:
		print("The original list is : " + str(face_name))
		return face_name[0]


def check_place(img, results):
	res = js.loads(results.pandas().xyxy[0].to_json(orient="records"))
	for s in range(len(res)):
		if res[s]["name"] == "person":
			pos = {"xmin": res[s]["xmin"], "ymin": res[s]["ymin"], "xmax": res[s]["xmax"], "ymax": res[s]["ymax"]}
			top = int(res[s]["ymin"])
			right = int(res[s]["xmin"])
			height = int(res[s]["ymax"])
			width = int(res[s]["xmax"])
			crop = img[top:height, right:width]
			#id = check_id(crop)
			#id = int(id)
			#print(id)
			with open("json_files_data/students.json", "r+") as f:
				studen = js.load(f)
			for s in studen["students"]:
				if id == s["student_id"]:
					with open("json_files_data/class.json", "r+") as n:
						clas = js.load(n)
						with open("json_files_data/orderddata.json", "r+") as m:
							order = js.load(m)
							for a in clas["place"]:
								if a["student_id"] == id:
									for i, table in enumerate(order["table"]):
										for j, row in enumerate(table):
										# row['table_row'] == a["table_row"] and row['table_number'] == a["table_number"]:
											if (width - row["xmax"]) + (right - row["xmin"]) + (height - row["ymax"]) + (
												top - row["ymin"]) < 2:
											# return id+"student sitting in his rightful place"
												print("student sitting in his place:" + str(id))
											else:
												print(s["student_id"])
												print("student is not sitting in his place")
											#return s["student_id"]+"student is not sitting in his place"
