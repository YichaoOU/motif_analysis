from Bio import SeqIO as io
from Bio.Seq import Seq
def read_fasta(file):
	
	seq_hash = {}
	f=open(file,"rU")
	record = io.parse(f,"fasta")
	
	
	for r in record:
		# print r.id
		temp = str(r.id)
		temp = temp.split("@")[0]
		seq_hash[temp]=str(r.seq).upper()
	return seq_hash 


from random import sample

import sys
my_gene = map(lambda x:x.strip(),open(sys.argv[1]).readlines())
all_promoters = read_fasta(sys.argv[2])
label = sys.argv[1].split("/")[-1]
foreground = open(label+".foreground.fa","wb")
background = open(label+".background.fa","wb")
all_genes = set(all_promoters.keys())
pool = list(all_genes.difference(set(my_gene)))
current_sample = sample(pool,3*len(my_gene))
fore_count = 0
for g in my_gene:
	if all_promoters.has_key(g):
		fore_count += 1
		print >>foreground,">" + g
		print >>foreground,all_promoters[g]
	else:
		print g

for g in current_sample:
	if all_promoters.has_key(g):
		print >>background,">" + g
		print >>background,all_promoters[g]








