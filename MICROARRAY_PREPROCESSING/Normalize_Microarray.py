import csv 
import pandas as pd 
from sklearn import preprocessing
import numpy as np 
import math
"""******************* all list over here *******"""
Considered_gene_list=[]
"""**********************************************"""
input_file="1842_microarray_updated.txt"
dataset = pd.read_csv(input_file,sep=" ",header=None)
Microarray= dataset.iloc[0:,0:].values
Microarray_Scaled = preprocessing.scale(Microarray)


input_file="Gene_list.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
Gene_list= dataset.iloc[0:,0:].values
row_g,col_g=Gene_list.shape
for i in range(0,row_g):
	Considered_gene_list.append(Gene_list[i,0])


def write_with_gene_name(Microarray,Considered_gene_list):
	output_file='Unlabeled_Microarray_zero_mean_unit_var.txt'
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=',')
		for i in range(0,len(Considered_gene_list)):
			col1=[]
			# col1.append(Considered_gene_list[i])
			list_=Microarray[i]
			for j in range(0,len(list_)):
				col1.append(list_[j])
			print len(col1)
			spamwriter.writerow(col1)

def calculate_eucledian_dist(list1,list2):
	sum_=0
	for i in range(0,len(list1)):
		sum_=sum_+(float(list1[i])-float(list2[i]))*(float(list1[i])-float(list2[i]))
	eucle_dist=math.sqrt(sum_)
	return eucle_dist


def eucledian_dist_without_gene_name(Microarray):
	row_c,col_c=Microarray.shape
	output_file='Microarray_Distance_Matrix.txt'
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=' ')
		for i in range(0,row_c):
			col1=[]
			for j in range(0,row_c):
				dist=0
				list1=[]
				list2=[]
				list1=Microarray[i]
				list2=Microarray[j]
				dist=calculate_eucledian_dist(list1,list2)
				col1.append(dist)
			spamwriter.writerow(col1)
				
def eucledian_dist_with_gene_name(Microarray,Considered_gene_list):
	row_c,col_c=Microarray.shape
	output_file='Microarray_Distance_Matrix_with_Header.txt'
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=',')
		col1=[]
		col1.append("Genes")
		for i in range(0,len(Considered_gene_list)):
			col1.append(Considered_gene_list[i])
		print len(col1)
		spamwriter.writerow(col1)
		for i in range(0,row_c):
			col1=[]
			col1.append(Considered_gene_list[i])
			for j in range(0,row_c):
				dist=0
				list1=[]
				list2=[]
				list1=Microarray[i]
				list2=Microarray[j]
				dist=calculate_eucledian_dist(list1,list2)
				col1.append(dist)
			print len(col1)
			spamwriter.writerow(col1)
# write_with_gene_name(Microarray_Scaled,Considered_gene_list)
eucledian_dist_with_gene_name(Microarray_Scaled,Considered_gene_list)
