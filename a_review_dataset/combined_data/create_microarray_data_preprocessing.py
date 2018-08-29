import csv
import pandas as pd
common_in_all=[]
index_gene_in_sequence=[]
def extract_index_of_common_gene():
	input_file="gene_common_in_all3.txt"
	dataset = pd.read_csv(input_file,sep=" ",header=None)
	csv_list = dataset.iloc[0:,0:].values
	row,col = csv_list.shape
	input_file1="yeast_name.txt"
	dataset1 = pd.read_csv(input_file1,sep=" ",header=None)
	csv_list1 = dataset1.iloc[0:,0:].values
	row1,col1 = csv_list1.shape
	for i in range(0,row):
		common_in_all.append(csv_list[i,0])
	for i in range(0,row1):
		if csv_list1[i,0] in common_in_all:
			index_gene_in_sequence.append(i)
def remove_space(list_):
	new_list=[]
	last_index=len(list_)-1
	for i in range(0,len(list_)):
		if i != last_index:
			if list_[i]!="":
				new_list.append(list_[i])
		elif i==last_index:
			val=list_[i].rstrip("\n")
			new_list.append(val)
	# print new_list
	# print len(new_list)
	return new_list


def create_new_microarray():
	index=-1
	count=0
	output_file='1842_microarray_updated.txt'
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=' ')
		with open('yeast_dataset.txt') as file_name:
			content = file_name.readlines()
			for line in content:
				index=index+1
				split_line=line.split(" ")
				split_line=remove_space(split_line)
				if index in index_gene_in_sequence:
					spamwriter.writerow(split_line)
	# print count
	# print index
extract_index_of_common_gene()
create_new_microarray()
# print len(common_in_all)
# print index_gene_in_sequence
