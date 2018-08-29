import csv
import pandas as pd
gene_list_all=[]
gene_list_process=[]
gene_list_function=[]
gene_list_component=[]
lexicon_gene_count=dict()
def all_gene_list(gene_list_all):
	gene_list_all=[]
	input_file='yeast_name.txt'
	dataset = pd.read_csv(input_file,sep=" ",header=None)
	csv_list = dataset.iloc[0:,0:].values
	row,col = csv_list.shape
	for i in range(0,row):
		gene_list_all.append(csv_list[i,0])
	return gene_list_all

def process_gene_list(gene_list_process):
	gene_list_process=[]
	input_file='process_mapped_genes.txt'
	dataset = pd.read_csv(input_file,sep=" ",header=None)
	csv_list = dataset.iloc[0:,0:].values
	row,col = csv_list.shape
	for i in range(0,row):
		gene_list_process.append(csv_list[i,0])
	return gene_list_process

def function_gene_list(gene_list_function):
	gene_list_function=[]
	input_file='function_mapped_genes.txt'
	dataset = pd.read_csv(input_file,sep=" ",header=None)
	csv_list = dataset.iloc[0:,0:].values
	row,col = csv_list.shape
	for i in range(0,row):
		gene_list_function.append(csv_list[i,0])
	return gene_list_function

def component_gene_list(gene_list_component):
	gene_list_component=[]
	input_file='component_mapped_genes.txt'
	dataset = pd.read_csv(input_file,sep=" ",header=None)
	csv_list = dataset.iloc[0:,0:].values
	row,col = csv_list.shape
	for i in range(0,row):
		gene_list_component.append(csv_list[i,0])
	return gene_list_component
def initialize_dictionary():
	for i in range(0,len(gene_list_all)):
		if gene_list_all[i] not in lexicon_gene_count:
			lexicon_gene_count[gene_list_all[i]]=0
		else:
			lexicon_gene_count[gene_list_all[i]]=lexicon_gene_count[gene_list_all[i]]+1
	for i in range(0,len(gene_list_process)):
		if gene_list_process[i] not in lexicon_gene_count:
			lexicon_gene_count[gene_list_process[i]]=0
		else:
			lexicon_gene_count[gene_list_process[i]]=lexicon_gene_count[gene_list_process[i]]+1
	for i in range(0,len(gene_list_function)):
		if gene_list_function[i] not in lexicon_gene_count:
			lexicon_gene_count[gene_list_function[i]]=0
		else:
			lexicon_gene_count[gene_list_function[i]]=lexicon_gene_count[gene_list_function[i]]+1
	for i in range(0,len(gene_list_component)):
		if gene_list_component[i] not in lexicon_gene_count:
			lexicon_gene_count[gene_list_component[i]]=0
		else:
			lexicon_gene_count[gene_list_component[i]]=lexicon_gene_count[gene_list_component[i]]+1

def seperate_mapped_in_all():
	output_file='gene_common_in_all3.txt'
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=' ')
		for key,val in lexicon_gene_count.iteritems():
			col1=[]
			if val==3:
				col1.append(key)
				spamwriter.writerow(col1)

		

gene_list_all=all_gene_list(gene_list_all)
print len(gene_list_all)
gene_list_process=process_gene_list(gene_list_process)
print len(gene_list_process)
gene_list_function=function_gene_list(gene_list_function)
print len(gene_list_function)
gene_list_component=component_gene_list(gene_list_component)
print len(gene_list_component)
initialize_dictionary()
count=0
count_1=0
for key,val in lexicon_gene_count.iteritems():
	count=count+1
	if val==3:
		count_1=count_1+1
	print str(count)+":: "+str(key)+": "+str(val)
print count_1
seperate_mapped_in_all()

