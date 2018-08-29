import csv
import pandas as pd
go_list_process=[]
go_list_function=[]
go_list_component=[]
lexicon_go_count=dict()
def update_list(input_file,go_term_list):
	go_term_list=[]
	dataset = pd.read_csv(input_file,sep=" ",header=None)
	csv_list = dataset.iloc[0:,0:].values
	row,col = csv_list.shape
	for i in range(0,row):
		go_term_list.append(csv_list[i,0])
	return go_term_list
def create_lexicon(go_list_process,go_list_function,go_list_component):
	for i in range(0,len(go_list_process)):
		if go_list_process[i] not in lexicon_go_count:
			lexicon_go_count[go_list_process[i]]=1
		else:
			lexicon_go_count[go_list_process[i]]=lexicon_go_count[go_list_process[i]]+1
	for i in range(0,len(go_list_function)):
		if go_list_function[i] not in lexicon_go_count:
			lexicon_go_count[go_list_function[i]]=1
		else:
			lexicon_go_count[go_list_function[i]]=lexicon_go_count[go_list_function[i]]+1
	for i in range(0,len(go_list_component)):
		if go_list_component[i] not in lexicon_go_count:
			lexicon_go_count[go_list_component[i]]=1
		else:
			lexicon_go_count[go_list_component[i]]=lexicon_go_count[go_list_component[i]]+1


go_list_process=update_list('process_unique_goterm.txt',go_list_process)
print len(go_list_process)
go_list_function=update_list('function_unique_goterm.txt',go_list_function)
print len(go_list_function)
go_list_component=update_list('component_unique_goterm.txt',go_list_component)
print len(go_list_component)
create_lexicon(go_list_process,go_list_function,go_list_component)
print type(lexicon_go_count)
count=0
count_1=0
for key,value in lexicon_go_count.iteritems():
	count=count+1
	if value>1:
		count_1=count_1+1
	print str(count)+"::"+str(key)+":"+str(value)
print count_1

