import pandas as pd 
import csv
obselete_goterm_list=[]
input_file="Go_term_obsolete.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
obsolete_list = dataset.iloc[0:,0:].values
row,col = obsolete_list.shape
# print row
# print obsolete_list
for i in range(0,row):
	obselete_goterm_list.append(obsolete_list[i,0])
# print obselete_goterm_list
	
Goterm_list=[]
input_file="Goterm_list.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
considered_csv_list = dataset.iloc[0:,0:].values
row,col = considered_csv_list.shape
for i in range(0,row):
	go_term = considered_csv_list[i,0]
	if go_term  in obselete_goterm_list:
		Goterm_list.append(go_term)
print Goterm_list
print len(Goterm_list)


