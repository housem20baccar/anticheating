import json as js


def check_value_exist(test_dict, value):
	do_exist = False
	for table in test_dict["table"]:
		for key, val in table.items():
			if val == value:
				do_exist = True
	return do_exist


def json_upload(results):
	with open("json_files_data/data.json", "r+") as f:
		dict = js.load(f)
	res = js.loads(results.pandas().xyxy[0].to_json(orient="records"))
	for s in range(len(res)):
		if res[s]["name"] == "dining table":
			pos = {"xmin": res[s]["xmin"], "ymin": res[s]["ymin"], "xmax": res[s]["xmax"], "ymax": res[s]["ymax"]}
			print(pos)
			ser = pos["xmax"] + pos["ymax"] + pos["xmin"] + pos["ymin"]
			if check_value_exist(dict, ser):
				continue
			else:
				dicti = {
					"table_row": "",
					"table_number": 0,
					"table_serial": pos["xmax"] + pos["ymax"] + pos["xmin"] + pos["ymin"],
					"xmax": pos["xmax"],
					"ymax": pos["ymax"],
					"xmin": pos["xmin"],
					"ymin": pos["ymin"]
				}
				dict["table"].append(dicti)
				with open("json_files_data/data.json", "r+") as f:
					f.seek(0)
					js.dump(dict, f, indent=2)
				print(dict)
