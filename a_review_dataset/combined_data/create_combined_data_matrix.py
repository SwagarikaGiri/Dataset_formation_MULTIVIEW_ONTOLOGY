import csv
import pandas as pd
import readchar
genes_unique=[]
go_term_unique=[]
mapped_gene_in_sequence=[]
common_in_all=[]
lexicon_gene_goterm=dict()
''' here we are finding which are the uniques genes '''
def unique_genes(gene_list):
	split_gene=[]
	gene_list.rstrip("\r")
	split_gene=gene_list.split(",")
	for i in range(0,len(split_gene)):
		if split_gene[i].lstrip() not in genes_unique:
			genes_unique.append(split_gene[i].lstrip())
'''here we will take into account which are the unique gene term'''	
def unique_go_term(go_id):
	if go_id not in go_term_unique:
		go_term_unique.append(go_id)

"""here we have taken into account  the unique gene and go term and stored them """
def create_dict_gene_goterm(go_id,gene_list):
	split_gene=[]
	gene_list.lstrip("\r")
	split_gene=gene_list.split(",")
	for i in range(0,len(split_gene)):
		if(go_id,split_gene[i]) not in lexicon_gene_goterm:
			lexicon_gene_goterm[go_id,split_gene[i].lstrip(" ")]=1
		else:
			lexicon_gene_goterm[go_id,split_gene[i].lstrip(" ")]=lexicon_gene_goterm[go_id,split_gene[i].lstrip(" ")]+1
def create_mapped_gene_in_sequence():
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
			mapped_gene_in_sequence.append(csv_list1[i,0])

	
""" creating the matrix """
def create_matrix():
	count=0
	output_file='matrix_combined_all_gene.txt'
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=',')
		col1=[]
		col1.append("gene_name")
		for i in range(0,len(go_term_unique)):
			col1.append(go_term_unique[i])
		print len(col1)
		spamwriter.writerow(col1)
		for i in range(0,len(mapped_gene_in_sequence)):
			col1=[]
			col1.append(mapped_gene_in_sequence[i])
			for j in range(0,len(go_term_unique)):
				if(str(go_term_unique[j]),str(mapped_gene_in_sequence[i]))  in lexicon_gene_goterm:
					count=count+1
					col1.append(1)
				else:
					col1.append(0)
			print len(col1)
			spamwriter.writerow(col1)
	print count
with open("combined_gene_goterm.txt") as file:
	content=file.readlines()
	for li in content:
		split=li.split(":")
		unique_go_term(split[0].rstrip("\n"))
		unique_genes(split[1].rstrip("\n\r"))
		create_dict_gene_goterm(split[0].rstrip("\n"),split[1].rstrip("\n\r"))
# print len(genes_unique)
# print len(go_term_unique)
# genes_unique.remove('none')
# print len(genes_unique)
create_mapped_gene_in_sequence()
output_file='gene_common_in_all_sequential.txt'
with open(output_file,'w') as outputcsv_file:
	spamwriter = csv.writer(outputcsv_file,delimiter=' ')
	for i in range(0,len(mapped_gene_in_sequence)):
		col1=[]
		col1.append(mapped_gene_in_sequence[i])
		spamwriter.writerow(col1)
# create_matrix()


# count=0
# count_1=0
# for key,value in lexicon_gene_goterm.iteritems():
# 	count=count+1
# 	if value>1:
# 		count_1=count_1+1
# 	print str(count)+"::"+str(key)+"::"+str(value)
# print count_1
