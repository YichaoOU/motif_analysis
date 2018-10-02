import os
def parse_list(file):
	temp = {}
	for line in open(file).readlines():
		temp[line.strip()] = ""
	return temp

def parse_bed_file(file):
	my_dict = {}
	flag = True
	with open(file) as f:
		for line in f:
			if flag:
				flag = False
				continue
			line = line.strip().split()
			seq_id = line[0]
			gene_id = line[5]
			my_dict[gene_id] = seq_id

	return my_dict	
	
def parse_orthologs(file,fore_list,Brugia_seq_id_gene_id):
	for line in open(file).readlines()[1:]:
		line = line.strip().split(",")
		brugia_id = line[0]
		elegans_id = line[6]
		OVOC_id = line[13]
		brugia_seq_id = Brugia_seq_id_gene_id[brugia_id]
		if not fore_list.has_key(brugia_seq_id):
			continue
		do_MSA_3_seqs(brugia_seq_id,elegans_id,OVOC_id)

from Bio import SeqIO as io
from Bio.Seq import Seq
def read_fasta(file):
	
	seq_hash = {}
	f=open(file,"rU")
	record = io.parse(f,"fasta")
	
	for r in record:
		seq_hash[str(r.id).split("@")[0]]=str(r.seq)
	return seq_hash		

B_seq = read_fasta("/users/PHS0293/ohu0404/project/Brugia/genome/Brugia_promoters.1000.fa")
C_seq = read_fasta("/users/PHS0293/ohu0404/project/Brugia/conservation/elegans_promoters.1000.fa")
O_seq = read_fasta("/users/PHS0293/ohu0404/project/Brugia/conservation/OVOC_promoters.1000.fa")
def do_MSA_3_seqs(id1,id2,id3):
	seq1 = B_seq[id1]
	seq2 = C_seq[id2]
	seq3 = O_seq[id3]
	out = open(id1+".orthologs.fa","wb")
	print >>out,">"+id1
	print >>out,seq1
	print >>out,">"+id2
	print >>out,seq2
	print >>out,">"+id3
	print >>out,seq3
	out.close()
	command = "clustalw2 -gapopen=10 -gapext=0.1 -infile=" + id1+".orthologs.fa"
	os.system(command)
	
		
label = "L3_L3D9"
fore_list = parse_list("/users/PHS0293/ohu0404/project/Brugia/FC4/L3_L3D9/fore.list")
Brugia_seq_id_gene_id = parse_bed_file("/users/PHS0293/ohu0404/project/Brugia/genome/Brugia_sequence_name.bed")

parse_orthologs("orthologs.csv",fore_list,Brugia_seq_id_gene_id)



