import json as js
def organize_data():
	with open("json_files_data/data.json", "r+") as f:
		dict = js.load(f)
		sorted_dict = sorted(dict["table"], key=lambda t: t["xmax"] and t["ymax"])
		l = {"table": []}
		l["table"].append(sorted_dict)
		with open("json_files_data/orderddata.json", "r+") as m:
			a = 750
			b = 2150
			c = 4000
			#d = 200 add  d
			for i, table in enumerate(l["table"]):
				for j, row in enumerate(table):
					if a == min([a, b, c], key=lambda x: abs(x - row["xmax"])):
						l["table"][i][j]['table_row'] = "A"
					if b == min([a, b, c], key=lambda x: abs(x - row["xmax"])):
						l["table"][i][j]['table_row'] = "B"
					if c == min([a, b, c], key=lambda x: abs(x - row["xmax"])):
						l["table"][i][j]['table_row'] = "C"
					#if d == min([a, b, c, d], key=lambda x: abs(x - row["xmax"])):
					#	l["table"][i][j]['table_row'] = "D"
			f = 0
			fr = 0
			frt = 0
			frty = 0
			for i, table in enumerate(l["table"]):
				for j, row in enumerate(table):
					if row["table_row"] == "A":
						f = f + 1
						row['table_number'] = f
					if row["table_row"] == "B":
						fr = fr + 1
						row['table_number'] = fr
					if row["table_row"] == "C":
						frt = frt + 1
						row['table_number'] = frt
					if row["table_row"] == "D":
						frty = frty + 1
						row['table_number'] = frty
			js.dump(l, m, indent=2)