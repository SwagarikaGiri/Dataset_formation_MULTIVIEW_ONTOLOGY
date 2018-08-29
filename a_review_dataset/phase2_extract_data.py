import csv
import pandas as pd
import readchar
genes_unique=[]
go_term_unique=[]
lexicon_gene_goterm=dict()
mapped_gene_in_sequence=[]
un_mapped_gene_in_sequence=[]
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
""" we need to store the gene sequence according to input list for further decrease in problem as only 2263 out of 2884 genes were mapped"""
def correct_gene_sequence():
	input_file='yeast_name.txt'
	dataset = pd.read_csv(input_file,sep=" ",header=None)
	csv_list = dataset.iloc[0:,0:].values
	row,col = csv_list.shape
	for i in range(0,row):
		if csv_list[i,0] in genes_unique:
			mapped_gene_in_sequence.append(csv_list[i,0])
		else:
			un_mapped_gene_in_sequence.append(csv_list[i,0])
	
def create_matrix():
	count=0
	output_file='matrix_component_gene_go_term.txt'
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
""" we need to strore mapped genes and mapped go terms """
def store_result_seq():
	output_file='component_mapped_genes.txt'
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=' ')
		for i in range(0,len(mapped_gene_in_sequence)):
			col1=[]
			col1.append(mapped_gene_in_sequence[i])
			spamwriter.writerow(col1)
	output_file='component_unmapped_genes.txt'
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=' ')
		for i in range(0,len(un_mapped_gene_in_sequence)):
			col1=[]
			col1.append(un_mapped_gene_in_sequence[i])
			spamwriter.writerow(col1)
	output_file='component_unique_goterm.txt'
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=' ')
		for i in range(0,len(go_term_unique)):
			col1=[]
			col1.append(go_term_unique[i])
			spamwriter.writerow(col1)
	

with open("component_gene_go_term.txt") as file:
	content=file.readlines()
	for li in content:
		split=li.split(":")
		unique_go_term(split[0].rstrip("\n"))
		unique_genes(split[1].rstrip("\n\r"))
		create_dict_gene_goterm(split[0].rstrip("\n"),split[1].rstrip("\n\r"))
print len(genes_unique)
print len(go_term_unique)
genes_unique.remove('none')
print len(genes_unique)
correct_gene_sequence()
print len(mapped_gene_in_sequence)
print len(un_mapped_gene_in_sequence)
create_matrix()
store_result_seq()

# for i in range(0,len(go_term_unique)):
# 	print go_term_unique[i]
# # 	print i
# count=0
# for key,value in lexicon_gene_goterm.iteritems():
# 	if key[0]=='none':
# 		print yes
	

