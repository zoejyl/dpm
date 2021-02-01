import csv
import pandas
from datetime import datetime
from operator import itemgetter
from collections import defaultdict
import itertools
import copy
if __name__ == '__main__':
	path1 = os.path.join(os.getcwd(), '..', '1125jh_g1_math_score.xlsx' )
	excel_data_df = pandas.read_excel(path1, sheet_name='math-score', usecols=['course_student_id', 'quiz'])
	sid = excel_data_df['course_student_id'].tolist()
	excel_dict = excel_data_df.to_dict(orient = 'records')
	high_pref = []
	low_pref = []
	for item in excel_dict:
		if item['quiz'] <= 43.5:
			low_pref.append(item['course_student_id'])
		else:
			high_pref.append(item['course_student_id'])
	content_dict = {}
	with open('content_list3.csv','r') as f:
		csv_reader = csv.reader(f)
		for row in csv_reader:
			if int(row[1]) != 0:
				temp = int(row[1])
				if int(row[1]) == 6: 
					temp = 2
				content_dict[row[0].strip()] = temp
	data_df = pandas.read_csv('1121data_open_sequence.csv') 
	data_dict = data_df.to_dict(orient = 'records')
	log = {}
	for item in data_dict:
		name = item["ssokid"]
		if not name in high_pref:#preformance
			continue
		timestamp = item["operationdate"]
		date = timestamp[:10]
		date_format = datetime.strptime(date,"%Y-%m-%d")
		contentname = item['contentsname'].strip()
		if not contentname in content_dict:
			continue
		content = content_dict[contentname]
		if not name in log:#new user
			log[name] = [content]
		else:
			log[name].append(content)
	dataset = []
	for name in log:
		dataset.append(log[name])
	user_num = 0
	for key in log:
		user_num += 1
	print("number of user: ",user_num)
	with open('processed_data_highper1126.txt', 'w') as f:
		for s in dataset:
			result = ""
			for c in s:
				result+= str(c)+" "+"-1 "
			result+= "-2\n"
			f.write(result)
	with open('seq_list_highper1126.txt','w') as f:
		for s in dataset:
			result = ""
			for c in s:
				result+= str(c)
			result+="\n"
			f.write(result)


