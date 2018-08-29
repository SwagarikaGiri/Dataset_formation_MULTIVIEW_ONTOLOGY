import pandas as pd
import csv
import numpy as np
import math
"""All Lexicon and List  present here """

Go_Term_Col_Index=dict()
Go_Term_Row_Index=dict()

"""Shen Similarity matrix"""
input_file="Shen_similarity_matrix.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
Shen_similarity=dataset.iloc[0:,0:].values

""" Lins similarity matrix """
input_file="Lins_similarity_matrix.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
Lins_similarity = dataset.iloc[0:,0:].values

""" Depth Based Information"""
input_file="Depth_Based_Matrix.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
Depth_similarity = dataset.iloc[0:,0:].values

""" Column and Row indices stored in dictionary"""
col=Shen_similarity[0,0:]
row=Shen_similarity[0:,0]
for i in range(0,len(row)):
	Go_Term_Row_Index[row[i]]=i
for i in range(0,len(col)):
	Go_Term_Col_Index[col[i]]=i

"""############ Considered Goterm ################################"""
input_file="Goterm_list.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
Goterm_list = dataset.iloc[0:,0].values
"""###################################################################"""

def apply_arc_tan(sum):
	in_array=[sum]
	sum_list = (np.arctan(in_array)*2)/math.pi
	return sum_list[0]

# print apply_arc_tan(10)
output_file='Multifactored_Similarity_Matrix.txt'
with open(output_file,'w') as outputcsv_file:
	spamwriter = csv.writer(outputcsv_file,delimiter=',')
	col1=[]
	col1.append("Go term ")
	for i in range(0,len(Goterm_list)):
		goterm=Goterm_list[i]
		col1.append(goterm)
	spamwriter.writerow(col1)
	for i in range(0,len(Goterm_list)):
		col1=[]
		goterm1=Goterm_list[i]
		index_row=Go_Term_Row_Index[goterm1]
		col1.append(goterm1)
		for j in range(0,len(Goterm_list)):
			goterm2=Goterm_list[j]
			index_col=Go_Term_Col_Index[goterm2]
			Shen_sim=0
			Depth_sim=0
			Lins_sim=0
			Shen_sim = float(Shen_similarity[index_row,index_col])
			Depth_sim = float(Depth_similarity[index_row,index_col])
			Lins_sim = float(Lins_similarity[index_row,index_col])
			similarity=Shen_sim+Depth_sim+Lins_sim
			val=apply_arc_tan(similarity)
			col1.append(val)
		print col1
		print len(col1)
		spamwriter.writerow(col1)









