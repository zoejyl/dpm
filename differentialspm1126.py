import re
import numpy as np
from scipy import stats
import os.path
import statistics as stat

def regexformat(pat,gap):
	pat_len = len(pat)
	rg = ""
	if gap ==0:
		rg = pat
	else:
		for i in range(pat_len-1):
			rg += pat[i]+"[a-z]{0,"+str(gap)+"}"
		rg += pat[-1]
	return rg

def iSupport(pat,gap,seq_list):
	pat_len = len(pat)
	rg = ""
	if gap ==0:
		rg = pat
	else:
		for i in range(pat_len-1):
			rg += pat[i]+"[a-z]{0,"+str(gap)+"}"
		rg += pat[-1]
	reg = re.compile(rg)

	ifre = []
	for seq in seq_list:
		result = reg.findall(seq)
		frequency = len(result)
		ifre.append(frequency)
	return ifre





if __name__ == '__main__':
	# low -left
	# high -right
	gap = 0
	leftseqlist = []
	filename = os.path.join( os.getcwd(), '..', 'seq_list_lowper1126.txt' )
	with open(filename) as f1:
		for line in f1:
			leftseqlist.append(line.strip("\n"))

	rightseqlist = []
	filename2 = os.path.join( os.getcwd(), '..', 'seq_list_highper1126.txt' )
	with open(filename2) as f2:
		for line in f2:
			rightseqlist.append(line.strip("\n"))
	operations = {'1':['a',1], '2':['b',2], '3':['c',3], '4': ['d',4], '5': ['e',5], '6': ['f',6], '7': ['g',7], '8': ['h',8], '9': ['i',9], '10': ['j',10], '11': ['k',11], "12": ['l',12], "13": ['m',13], '14': ['n',14], '15': ['o',15], '16': ['p',16], '17': ['q',17],'18':['r',18],'19':['s',19],'20':['t',20],'21':['u',21]}

	leftfrepatlist = []
	filename3 = os.path.join( os.getcwd(), '..', 'fre_pattern_lowper1126.txt' )
	with open(filename3) as f3:
		for line in f3:
			temp = line.split("#SUP")[0].strip()
			temp2 = temp.split(" -1")
			final = ''
			for i in range(len(temp2)-1):
				final+=temp2[i].strip()
			leftfrepatlist.append(final)

	rightfrepatlist = []
	filename4 = os.path.join( os.getcwd(), '..', 'fre_pattern_highper1126.txt' )
	with open(filename4) as f4:
		for line in f4:
			temp = line.split("#SUP")[0].strip()
			temp2 = temp.split(" -1")
			final = ''
			for i in range(len(temp2)-1):
				final+=temp2[i].strip()
			rightfrepatlist.append(final)
	bothleft = {}
	bothright = {}
	left = {}
	right = {}
	for pat in leftfrepatlist + rightfrepatlist:
		iSupportleft = np.array(iSupport(pat,gap,leftseqlist))
		iSupportright = np.array(iSupport(pat,gap,rightseqlist))
		if stats.ttest_ind(iSupportright,iSupportleft,equal_var = False)[1] <= 0.05:
			if pat in leftfrepatlist and pat in rightfrepatlist:
				if np.mean(iSupportleft) > np.mean(iSupportright):
					bothleft[pat] = np.mean(iSupportleft) - np.mean(iSupportright)
				else:
					bothright[pat] = np.mean(iSupportleft) - np.mean(iSupportright)
			elif pat in leftfrepatlist:
				left[pat] = np.mean(iSupportleft) - np.mean(iSupportright)
			else:
				right[pat] = np.mean(iSupportleft) - np.mean(iSupportright)
	left_sort = sorted(left.items(), key=lambda x: x[1], reverse = True) 
	right_sort = sorted(right.items(), key=lambda x: x[1]) 
	operations_dict = {'1':'textbook', '2':'in class problem', '3':'solution', '4':'note', '5':'test_paper', '6':'step problem','7':'instruction','8':'research','9':'self evaluation'}
	fre_dict_left = []
	for pat in left:
		issup = iSupport(pat,gap,leftseqlist)
		fre_dict_left.append((pat,stat.mean(issup)))
	fre_dict_right = []
	for pat in right:
		issup = iSupport(pat,gap,rightseqlist)
		fre_dict_right.append((pat,stat.mean(issup)))
	print(fre_dict_left)
	print(fre_dict_right)
	print("left ", len(fre_dict_left))
	for item in fre_dict_left:
		seq = item[0]
		temp = ''
		for i in range(len(seq)):
			temp+= operations_dict[seq[i]] + '->'
		print(temp)
		print(item[1])
	print("right ", len(fre_dict_right))
	for item in fre_dict_right:
		seq = item[0]
		temp = ''
		for i in range(len(seq)):
			temp+= operations_dict[seq[i]] + '->'
		print(temp)
		print(item[1])



	# print("right sorted ",len(right_sort))
	# for item in right_sort:
	# 	seq = item[0]
	# 	temp = ''
	# 	for i in range(len(seq)):
	# 		temp+= operations_dict[seq[i]] + '->'
	# 	print(temp)
	# 	print(item[1])







