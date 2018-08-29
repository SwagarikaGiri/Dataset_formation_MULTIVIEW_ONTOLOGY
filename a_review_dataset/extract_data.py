import csv


output_file='component_gene_go_term.txt'
with open(output_file,'w') as outputcsv_file:
	spamwriter = csv.writer(outputcsv_file,delimiter=':')
	fname='component.txt'
	col1=[]
	col1.append("go_id")
	col1.append("genes")
	spamwriter.writerow(col1)
	with open(fname) as f:
		content = f.readlines()
		count=0
		for line in content:
			count=count+1
			if((count%6==2)or(count%6==5)):
				split_line=line.split(":")
				if(count%6==2):
					col1=[]
					col1.append(split_line[1].rstrip("\n"))
				if (count%6==5):
					col1.append(split_line[1].rstrip("\n"))
					print col1
					spamwriter.writerow(col1)

				
				

	