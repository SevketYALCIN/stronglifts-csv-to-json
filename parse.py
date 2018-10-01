import csv
import json

with open('./data/input/spreadsheet-stronglifts.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	next(csv_reader)
	line_count = 0
	workout_dic = {'Squat': [], 'Deadlift': [],
								 'Bench Press': [], 'Barbell Row': [], 'Overhead Press': []}
	for row in csv_reader:
		workout_dic[row[4]].append({'x': row[0], 'y': row[5]})
		workout_dic[row[12]].append({'x': row[0], 'y': row[13]})
		workout_dic[row[20]].append({'x': row[0], 'y': row[21]})

with open('./data/output/squat.json', 'w') as outfile:
  json.dump(workout_dic['Squat'], outfile)

with open('./data/output/bench.json', 'w') as outfile:
  json.dump(workout_dic['Bench Press'], outfile)

with open('./data/output/deadlift.json', 'w') as outfile:
  json.dump(workout_dic['Deadlift'], outfile)

with open('./data/output/row.json', 'w') as outfile:
  json.dump(workout_dic['Barbell Row'], outfile)

with open('./data/output/overhead.json', 'w') as outfile:
  json.dump(workout_dic['Overhead Press'], outfile)