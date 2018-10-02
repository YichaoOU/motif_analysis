import sys		

import os


def parse_orthologs(file):
	for line in open(file).readlines():
		line = line.strip().split(",")
		T = line[0]
		L = line[3]
		do_MSA_2_seqs(T,L)

from Bio import SeqIO as io
from Bio.Seq import Seq
def read_fasta(file):
	
	seq_hash = {}
	f=open(file,"rU")
	record = io.parse(f,"fasta")
	
	for r in record:
		seq_hash[str(r.id).split("|")[0]]=str(r.seq)
	return seq_hash		

T_seq = read_fasta(sys.argv[2])
L_seq = read_fasta(sys.argv[3])
def do_MSA_2_seqs(id1,id2):
	try:
		seq1 = T_seq[id1]
		seq2 = L_seq[id2]
	except:
		print id1,id2,"can't be accessed, something wrong"
		return 1
	out = open(id1+".orthologs.fa","wb")
	print >>out,">"+id1
	print >>out,seq1
	print >>out,">"+id2
	print >>out,seq2
	out.close()
	command = "clustalw2 -gapopen=10 -gapext=0.1 -infile=" + id1+".orthologs.fa"
	os.system(command)
	os.system("rm "+id1+".orthologs.fa")
	os.system("rm "+id1+".orthologs.dnd")
	
parse_orthologs(sys.argv[1])



