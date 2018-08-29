import pandas as pd 
import csv

input_file="Gene_Goterm_matrix.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
Gene_Goterm_matrix = dataset.iloc[1:,0:].values
# print Gene_Goterm_matrix

input_file="Multifactored_Similarity_Matrix.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
Multi_Similarity = dataset.iloc[0:,0:].values
# print Multi_Similarity.shape


"""  #############ALL LIST PRESENT HERE##############"""
Gene_row_index_lexicon=dict()
Goterm_col_index_lexicon=dict()
Considered_Gene_list=[]
Considered_Goterm_list=[]
# Goterm_corresponding_index=dict()
"""###################################################"""
def Intialize_the_lexicon_and_list(Gene_row_index_lexicon,Goterm_col_index_lexicon,Considered_Gene_list,Considered_Goterm_list):
	input_file="Gene_Goterm_matrix.txt"
	dataset = pd.read_csv(input_file,sep=",",header=None)
	Gene_row_list = dataset.iloc[0:,0].values
	for i in range(0,len(Gene_row_list)):
		Gene_row_index_lexicon[Gene_row_list[i]]=i
	Goterm_col_list=dataset.iloc[0,0:]
	for i in range(0,len(Goterm_col_list)):
		Goterm_col_index_lexicon[Goterm_col_list[i]]=i
	for i in range(1,len(Gene_row_list)):
		Considered_Gene_list.append(Gene_row_list[i])
	for i in range(0,len(Goterm_col_list)):
		Considered_Goterm_list.append(Goterm_col_list[i])
	return Gene_row_index_lexicon,Goterm_col_index_lexicon,Considered_Gene_list,Considered_Goterm_list

Gene_row_index_lexicon,Goterm_col_index_lexicon,Considered_Gene_list,Considered_Goterm_list=Intialize_the_lexicon_and_list(Gene_row_index_lexicon,Goterm_col_index_lexicon,Considered_Gene_list,Considered_Goterm_list)


def find_overlap_for_Genes(Gene1_list_s,Gene2_list_s):
	count=0
	Gene1_list=[]
	Gene2_list=[]
	for i in range(0,len(Gene1_list_s)):
		Gene1_list.append(int(Gene1_list_s[i]))
		Gene2_list.append(int(Gene2_list_s[i]))
	for i in range(0,len(Gene1_list)):
		if (Gene1_list[i]==Gene2_list[i]==1):
			count=count+1
	sum1=sum(Gene1_list)
	sum2=sum(Gene2_list)
	if sum1<=sum2:
		return count/float(sum1)
	else:
		return count/float(sum2)


def Multifactored_average(Gene1_list_s,Gene2_list_s,Multi_Similarity):
	Gene1_list=[]
	Gene2_list=[]
	for i in range(0,len(Gene1_list_s)):
		Gene1_list.append(int(Gene1_list_s[i]))
		Gene2_list.append(int(Gene2_list_s[i]))
	index_gene1=[]
	index_gene2=[]
	sum_=0
	for i in range(0,len(Gene1_list)):
		if Gene1_list[i] == 1:
			index_gene1.append(i+1)
	for i in range(0,len(Gene2_list)):
		if Gene2_list[i]== 1 :
			index_gene2.append(i+1)
	for ele1 in index_gene1:
		for ele2 in index_gene2:
			sum_=sum_+ round(float(Multi_Similarity[ele1,ele2]),5)
	denom=len(index_gene1)*len(index_gene2)
	if denom==0:
		return 0
	else:
		return sum_/float(denom)


row_c,col_c=Gene_Goterm_matrix.shape
for i in range(0,1):
	for j in range(0,1):
		gene1=Gene_Goterm_matrix[i,0]
		gene2=Gene_Goterm_matrix[j,0]
		gene_list1=Gene_Goterm_matrix[i,1:]
		gene_list2=Gene_Goterm_matrix[j,1:]
		sum1=0
		sum1=find_overlap_for_Genes(gene_list1,gene_list2)
		sum2=0
		sum2=Multifactored_average(gene_list1,gene_list2,Multi_Similarity)
		sum_=(sum1+sum2)/2

def Create_Multifactored_Similarity_Matrix(Gene_Goterm_matrix,Multi_Similarity,Considered_Gene_list):
	output_file='Multifactored_TermOverlap_Matrix.txt'
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=',')
		col1=[]
		row_c,col_c=Gene_Goterm_matrix.shape
		col1.append("GENES: ")
		for i in range(0,len(Considered_Gene_list)):
			col1.append(Considered_Gene_list[i])
		print len(col1)
		spamwriter.writerow(col1)
		for i in range(0,row_c):
			gene1=Gene_Goterm_matrix[i,0]
			col1=[]
			col1.append(gene1)
			for j in range(0,row_c):
				gene_list1=Gene_Goterm_matrix[i,1:]
				gene_list2=Gene_Goterm_matrix[j,1:]
				sum1=0
				sum1=find_overlap_for_Genes(gene_list1,gene_list2)
				sum2=0
				sum2=Multifactored_average(gene_list1,gene_list2,Multi_Similarity)
				sum_=(sum1+sum2)/2
				col1.append(sum_)
			print len(col1)
			spamwriter.writerow(col1)
		

Create_Multifactored_Similarity_Matrix(Gene_Goterm_matrix,Multi_Similarity,Considered_Gene_list)






