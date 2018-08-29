import pandas as pd
import csv
import igraph
from igraph import *
import numpy as np
import math

input_file="Go_term info_remove_obsolete.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
parent_info = dataset.iloc[0:,0:].values
information_content= dataset.iloc[0:,0:].values
row_p,col_p = parent_info.shape
max_ic=0
min_weight=0
for i in range(0,row_p):
	val=parent_info[i,3]
	if val>max_ic:
		max_ic=val
# print max_ic

min_weight=1.0/max_ic
# print min_weight





""" so that index of the go term can be easily assessible """
go_term_index_lexicon=dict()
considered_goterm_list=[]
goterm_pair_and_LCA=dict()
new_child_parent_lexicon=dict()
Shen_similarity_lexicon=dict()


"""########################################################"""
input_file="LCA_and_Depth_Info_unique.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
Goterm_pair_LCA = dataset.iloc[0:,0:].values
row_lca,col_lca = Goterm_pair_LCA.shape
# print row_lca
# print col_lca
for i in range(0,row_lca):
	goterm1=Goterm_pair_LCA[i,0]
	goterm2=Goterm_pair_LCA[i,1]
	lca=Goterm_pair_LCA[i,2]
	if lca!="NoParent":
		if (goterm1,goterm2) not in goterm_pair_and_LCA:
			goterm_pair_and_LCA[goterm1,goterm2]=lca


input_file="Goterm_list_without_obs.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
considered_goterm = dataset.iloc[0:,0:].values
row_c,col_c = considered_goterm.shape
for i in range(0,row_c):
	considered_goterm_list.append(considered_goterm[i,0])

input_file="LCA_and_Depth_Info_unique.txt"
dataset = pd.read_csv(input_file,sep=",",header=None)
Goterm_pair_LCA = dataset.iloc[0:,0:].values
row_lca,col_lca = Goterm_pair_LCA.shape


""" here from the go term we will find the index and then from index we need to find the information content of the go term"""
def find_IC(parent_info,go_term):
	pass

def find_go_term_index(parent_info,go_term_index_lexicon):
	row_p,col_p = parent_info.shape
	for i in range(0,row_p):
		go_term_index_lexicon[parent_info[i,0]]=i
	return go_term_index_lexicon

go_term_index_lexicon=find_go_term_index(parent_info,go_term_index_lexicon)

Root_nodes=['GO:0008150','GO:0044699','GO:0000004','GO:0007582','GO:0003674','GO:0005554','GO:0005575','GO:0008372']



def return_parent_list(string_):
	list_=string_.split(" ")
	parent_list=[]
	for i in range(0,len(list_)-1):
		parent_list.append(list_[i])
	return parent_list

def unique_list(list_of_list,new_child_parent_lexicon):
	for ele in list_of_list:
		key1=ele[0]
		key2=ele[1]
		if  (key1,key2) not in new_child_parent_lexicon:
			new_child_parent_lexicon[key1,key2]=1
	return new_child_parent_lexicon
	
def child_parent_list(go_term,parent_info_list):
	# print go_term
	if go_term in Root_nodes:
		return []
	index=go_term_index_lexicon[go_term]
	string_=parent_info_list[index,4]
	parent_list=return_parent_list(string_)
	list_of_list=[]
	if len(parent_list)==0:
		list_=[]
		list_of_list.append(list_)
		return list_of_list
	else:
		for i in range(0,len(parent_list)):
			list_=[]
			list_=[str(go_term),str(parent_list[i])]
			list_of_list.append(list_)
		for i in range(0,len(parent_list)):
			# print parent_list[i]
			new_list_of_list=child_parent_list(str(parent_list[i]),parent_info_list)
			for i in range(0,len(new_list_of_list)):
				list_of_list.append(new_list_of_list[i])
		return list_of_list
		

	return list_of_list
def create_lexicon_of_child_parent_for_go_term(go_term,new_child_parent_lexicon):
	new_child_parent_lexicon.clear()
	list_of_list=child_parent_list(go_term,parent_info)
	new_child_parent_lexicon= unique_list(list_of_list,new_child_parent_lexicon)
	return new_child_parent_lexicon

def get_num_vertex_list(new_child_parent_lexicon):
	list_=[]
	for key,value in new_child_parent_lexicon.iteritems():
		goterm1=key[0]
		goterm2=key[1]
		if goterm1 not in list_:
			list_.append(goterm1)
		if goterm2 not in list_:
			list_.append(goterm2)
	return len(list_),list_
def weight_of_parent(parent):
	index=go_term_index_lexicon[parent]
	weight = float(information_content[index,3])
	if weight==0.0:
		return 0.001
	else:
		return (1.0/weight)

def create_graph_and_apply_shortest_path(new_child_parent_lexicon,source_,destination):
	dist=0
	g = Graph(directed=True)
	num,vertices=get_num_vertex_list(new_child_parent_lexicon)
	g.add_vertices(num)
	g.vs["name"]=vertices
	g.es["weight"]=1
	for key,value in new_child_parent_lexicon.iteritems():
		child=key[0]
		parent=key[1]
		g[child,parent]=weight_of_parent(parent)
	weight=g.es["weight"]
	# print weight
	val=g.shortest_paths_dijkstra(source=source_, target=destination, weights=weight, mode=OUT)
	dist=val[0][0]
	return dist


def Shen_measure(go_term1,go_term2,lca,new_child_parent_lexicon):
	total_dist=0
	new_child_parent_lexicon.clear()
	new_child_parent_lexicon=create_lexicon_of_child_parent_for_go_term(go_term1,new_child_parent_lexicon)
	dist_goterm1_lca=create_graph_and_apply_shortest_path(new_child_parent_lexicon,go_term1,lca)
	index1=go_term_index_lexicon[go_term1]
	try:
		ic_of_goterm1=(1.0/float(information_content[index1,3]))
	except:
		ic_of_goterm1=0.001

	new_child_parent_lexicon.clear()
	new_child_parent_lexicon=create_lexicon_of_child_parent_for_go_term(go_term2,new_child_parent_lexicon)
	dist_goterm2_lca=create_graph_and_apply_shortest_path(new_child_parent_lexicon,go_term2,lca)
	index2=go_term_index_lexicon[go_term2]
	try:
		ic_of_goterm2=(1.0/float(information_content[index2,3]))
	except:
		ic_of_goterm2=0.001

	
	index_lca=go_term_index_lexicon[lca]
	try:
		ic_of_lca=(1.0/float(information_content[index_lca,3]))
	except:
		ic_of_lca=0.001
	total_dist=ic_of_goterm1+dist_goterm1_lca+ic_of_goterm2+dist_goterm2_lca-ic_of_lca
	return total_dist


def calculate_shen_similarity_between_goterms(go_term1,go_term2,LCA,new_child_parent_lexicon):
	if go_term1==go_term2:
		return 1
	else:
		new_child_parent_lexicon.clear()
		dist=Shen_measure(go_term1,go_term2,LCA,new_child_parent_lexicon)
		in_array=[dist]
		dist_list = (np.arctan(in_array)*2)/math.pi
		shen_dist = round(dist_list[0],5)
		shen_sim = 1.0-shen_dist
		return shen_sim

def write_file_Shen_similarity(Shen_similarity_lexicon):
	output_file='Shen_similarity_matrix.txt'
	with open(output_file,'w') as outputcsv_file:
		spamwriter = csv.writer(outputcsv_file,delimiter=',')
		col1=[]
		col1.append("Go term ")
		for i in range(0,len(considered_goterm_list)):
			goterm=considered_goterm_list[i]
			col1.append(goterm)
		spamwriter.writerow(col1)
		for i in range(0,len(considered_goterm_list)):
			col1=[]
			col1.append(considered_goterm_list[i])
			for j in range(0,len(considered_goterm_list)):
				goterm1=considered_goterm_list[i]
				goterm2=considered_goterm_list[j]
				if (goterm1,goterm2) not in Shen_similarity_lexicon:
					col1.append(0)
				elif (goterm1,goterm2) in Shen_similarity_lexicon:
					val=Shen_similarity_lexicon[goterm1,goterm2]
					col1.append(val)
			spamwriter.writerow(col1)




for key,value in goterm_pair_and_LCA.iteritems():
	go_term1=key[0]
	go_term2=key[1]
	LCA=value
	shen_sim=0
	shen_sim=calculate_shen_similarity_between_goterms(go_term1,go_term2,LCA,new_child_parent_lexicon)
	# print shen_sim
	if (go_term1,go_term2) not in Shen_similarity_lexicon:
		Shen_similarity_lexicon[go_term1,go_term2]=shen_sim
# print Shen_similarity_lexicon
write_file_Shen_similarity(Shen_similarity_lexicon)








