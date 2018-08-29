import pandas as pd
import csv


input_file="Go_term info_remove_obsolete.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
csv_list = dataset.iloc[0:,0:].values
row,col = csv_list.shape
Root_nodes=['GO:0008150','GO:0044699','GO:0000004','GO:0007582','GO:0003674','GO:0005554','GO:0005575','GO:0008372']
"""################     LIST   ####################"""
go_term_index_lexicon=dict()
Go_term_Depth_lexicon=dict()
considered_goterm_list=[]


"""################     LIST   ####################"""
input_file="Go_term info_remove_obsolete.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
go_term_info = dataset.iloc[0:,0:].values
row_g,col_g = go_term_info.shape
for i in range(0,row_g):
	term=go_term_info[i,0]
	depth=go_term_info[i,1]
	Go_term_Depth_lexicon[term]=depth

input_file="Goterm_list_without_obs.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
considered_goterm = dataset.iloc[0:,0:].values
row_c,col_c = considered_goterm.shape
for i in range(0,row_c):
	considered_goterm_list.append(considered_goterm[i,0])



def find_go_term_index():
	for i in range(0,row):
		go_term_index_lexicon[csv_list[i,0]]=i
find_go_term_index()

def return_parent_list(string_):
	list_=string_.split(" ")
	parent_list=[]
	for i in range(0,len(list_)-1):
		parent_list.append(list_[i])
	return parent_list

def unique_parent_list(list_):
	unique_list=[]
	for ele in list_:
		if ele not in unique_list:
			unique_list.append(ele)
	return unique_list

def find_all_parent_list(go_term):
	parent_list=[]
	index = int(go_term_index_lexicon[go_term])
	list_=csv_list[index,4]
	if go_term not in Root_nodes:
		parent_list=return_parent_list(list_)
		for ele in parent_list:
			new_list=[]
			new_list=find_all_parent_list(ele)
			parent_list=parent_list+new_list
		return parent_list
	else:
		parent_list=[]
		return parent_list
def find_all_unique_parent_list(go_term):
	parent_list=[]
	parent_list=find_all_parent_list(go_term)
	parent_list=unique_parent_list(parent_list)
	return parent_list
def list_into_str(list_):
	str_=""
	for i in range(0,len(list_)):
		str_=str_+list_[i]+" "
	return str_

def Write_all_parent_list():
	output_file='Go_term_all_parents_info.txt'
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=',')
		col1=[]
		col1.append("Go term ID")
		col1.append("No of parents")
		col1.append("All parents list ")
		spamwriter.writerow(col1)
		for i in range(0,row):
			col1=[]
			parent_list=[]
			parent_list=find_all_parent_list(csv_list[i,0])
			parent_list=unique_parent_list(parent_list)
			parent_string=list_into_str(parent_list)
			col1.append(csv_list[i,0])
			col1.append(str(len(parent_list)))
			col1.append(parent_string)
			spamwriter.writerow(col1)
# Write_all_parent_list()
def find_common_parents(go_term1, go_term2):
	parent_list1=[]
	parent_list2=[]
	common_parents=[]
	parent_list1=find_all_unique_parent_list(go_term1)
	parent_list2=find_all_unique_parent_list(go_term2)
	for i in range(0,len(parent_list1)):
		if parent_list1[i] in parent_list2:
			common_parents.append(parent_list1[i])
	return common_parents

def parent_maximum_depth(common_parents_list):
	max_depth=0
	LCA=None
	for i in range(0,len(common_parents_list)):
		new_depth=Go_term_Depth_lexicon[common_parents_list[i]]
		if new_depth>=max_depth:
			max_depth=new_depth
			LCA=common_parents_list[i]
	return LCA


def LCA_for_goterm_pair(go_term1, go_term2):
	common_parents=find_common_parents(go_term1, go_term2)
	if len(common_parents)==0:
		return "NoParent"
	elif len(common_parents)>0:
		LCA_parent=parent_maximum_depth(common_parents)
		return LCA_parent
# print Go_term_Depth_lexicon
 
def write_file_depth_matrix():
	output_file='LCA_and_Depth_Info_unique.txt'
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=',')
		col1=[]
		col1.append("Goterm1")
		col1.append("Goterm2")
		col1.append("LCA")
		col1.append("LCA Depth")
		spamwriter.writerow(col1)
		for i in range(0,len(considered_goterm_list)):
			for j in range(0,len(considered_goterm_list)):
				if (i<=j):
					col1=[]
					goterm1=considered_goterm_list[i]
					goterm2=considered_goterm_list[j]
					LCA=LCA_for_goterm_pair(goterm1,goterm2)
					if LCA != "NoParent":
						depth=Go_term_Depth_lexicon[LCA]
					else:
						depth=0
					col1.append(goterm1)
					col1.append(goterm2)
					col1.append(LCA)
					col1.append(depth)
					spamwriter.writerow(col1)
write_file_depth_matrix()


