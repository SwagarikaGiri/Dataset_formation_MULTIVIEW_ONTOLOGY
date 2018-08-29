import csv
import pandas as pd

goterm_pair_and_LCA=dict()
input_file="LCA_and_Depth_Info_unique.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
Goterm_pair_LCA = dataset.iloc[0:,0:].values
row_lca,col_lca = Goterm_pair_LCA.shape
print row_lca
print col_lca
for i in range(0,row_lca):
	goterm1=Goterm_pair_LCA[i,0]
	goterm2=Goterm_pair_LCA[i,1]
	lca=Goterm_pair_LCA[i,2]
	if lca!="NoParent":
		if (goterm1,goterm2) not in goterm_pair_and_LCA:
			goterm_pair_and_LCA[goterm1,goterm2]=lca


for key, value in goterm_pair_and_LCA.iteritems():
	print key 
	print value