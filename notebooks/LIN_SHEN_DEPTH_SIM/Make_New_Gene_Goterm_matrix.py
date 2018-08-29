import pandas as pd 
import csv
import numpy as np
import math


def make_new_gene_goterm_matrix():
	input_file="Gene_goterm_matrix.txt"
	dataset = pd.read_csv(input_file,sep=",",header=None)
	go_term_166=[]
	Gene_Goterm = dataset.iloc[0:,0:].values
	goterm_row = dataset.iloc[1:,0].values
	goterm_col = dataset.iloc[0,0:].values
	for i in range(1,len(goterm_col)):
		go_term_166.append(goterm_col[i])
	print len(go_term_166)
	go_term_list_id=[]
	go_term_list_term=[]
	input_file="Goterm_list.txt"
	dataset = pd.read_csv(input_file,sep=",",header=None)
	Considered_goterm = dataset.iloc[0:,0:].values
	row_g,col_g=Considered_goterm.shape
	""" there are some useless list and dict here """
	for i in range(0,row_g):
		val=Considered_goterm[i,0]
		val_list=val.split(":")
		go_term_list_id.append(int(val_list[1]))
		go_term_list_term.append(val)
	col_index=dict()
	for i in range(0,len(goterm_col)):
		col_index[goterm_col[i]]=i
	output_file='Gene_Goterm_matrix_updated162.txt'
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=',')
		col1=[]
		col1.append("Go term ")
		for i in range(0,len(go_term_list_term)):
			goterm=go_term_list_term[i]
			col1.append(goterm)
		spamwriter.writerow(col1)
		for i in range(0,len(goterm_row)):
			col1=[]
			gene=goterm_row[i]
			col1.append(gene)
			for j in range(0,len(go_term_list_term)):
				go_term_id=go_term_list_id[j]
				# if go_term_id in go_term
			# spamwriter.writerow(col1)



make_new_gene_goterm_matrix()

