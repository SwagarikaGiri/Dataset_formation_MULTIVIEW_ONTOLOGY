import pandas as pd 
import csv
list_166=[]
list_162=[]
obsolute=[]
obsolute_index=[]

input_file="Gene_Goterm_Matrix.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
matrix=dataset.iloc[0:,0:].values
list_goterm166=dataset.iloc[0,1:].values
for i in range(0,len(list_goterm166)):
	list_166.append(list_goterm166[i])

input_file="Goterm_list.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
list_goterm162=dataset.iloc[0:,0:].values
row_c,col_c=list_goterm162.shape
for i in range(0,row_c):
	list_162.append(list_goterm162[i,0])

for i in range(0,len(list_166)):
	if list_166[i] not in list_162:
		obsolute.append(list_166[i])
		obsolute_index.append(i+1)
# print matrix[1,0:]
print obsolute_index

row_m,col_m =matrix.shape
print row_m
print col_m
output_file='Gene_Goterm_matrix_updated162.txt'
with open(output_file,'w') as outputcsv_file:
	spamwriter = csv.writer(outputcsv_file,delimiter=',')
	for i in range(0,row_m):
		col1=[]
		for j in range(0,col_m):
			if j not in obsolute_index:
				col1.append(matrix[i,j])
		print len(col1)
		spamwriter.writerow(col1)



