





def parse_aln(file):
	my_dict = {}
	for line in open(file).readlines()[1:]:
		line = line.strip().split()
		if not len(line) == 2:
			continue
		gene = line[0]
		seq = line[1]
		if not my_dict.has_key(gene):
			my_dict[gene] = ""
		my_dict[gene] += seq

	return my_dict

def min_diff(a,b):
	min_diffs = 999
	for i in a:
		for j in b:
			diff = abs(i-j)
			if diff < min_diffs:
				min_diffs = diff
	return min_diffs
def parse_fimo(file):
	my_dict = {}
	for line in open(file).readlines()[1:]:
		line = line.strip().split()
		motif = line[0]
		gene = line[1].split("@")[0]
		start = int(line[2])
		if not my_dict.has_key(motif):
			my_dict[motif] = {}
		if not my_dict[motif].has_key(gene):
			my_dict[motif][gene] = []
		my_dict[motif][gene].append(start)
	return my_dict
	
def adjust_pos(seq,pos):
	adjust_pos = pos
	count_original_pos = 0
	for i in range(len(seq)):
		if seq[i] == "-":
			adjust_pos += 1
		else:
			count_original_pos += 1
		if count_original_pos == pos:
			return adjust_pos

import glob
gene_list = [] 
for item in glob.glob("Bm*.aln"):
	item = item.split(".")[0]
	gene_list.append(item)
import sys
B_fimo = sys.argv[1]
C_fimo = "elegans.fimo"
O_fimo = "OVOC.fimo"

B_fimo_pos = parse_fimo(B_fimo)
C_fimo_pos = parse_fimo(C_fimo)
O_fimo_pos = parse_fimo(O_fimo)
motif_cons = {}		
dis_cut = 1	
for motif in B_fimo_pos:
	motif_cons[motif]={}
	motif_cons[motif]["cons"] = []
	motif_cons[motif]["amg"] = []
	if not C_fimo_pos.has_key(motif):
		continue
	if not O_fimo_pos.has_key(motif):
		continue
	for gene in B_fimo_pos[motif]:
		if gene in gene_list:
			aln = parse_aln(gene+".orthologs.aln")
			
			orthologs = aln.keys()
			B_pos_array = B_fimo_pos[motif][gene]
			B_adj_pos_array = []
			C_adj_pos_array = []
			O_adj_pos_array = []
			for B_pos in B_pos_array:
				B_adj_pos = adjust_pos(aln[gene],B_pos)
				B_adj_pos_array.append(B_adj_pos)
			orthologs.remove(gene)
			ortholog1 = orthologs[0]
			ortholog2 = orthologs[1]
			# print 
			if C_fimo_pos[motif].has_key(orthologs[0]):
				ortholog1 = orthologs[0]
			if C_fimo_pos[motif].has_key(orthologs[1]):
				ortholog1 = orthologs[1]
			if O_fimo_pos[motif].has_key(orthologs[0]):
				ortholog2 = orthologs[0]
			if O_fimo_pos[motif].has_key(orthologs[1]):
				ortholog2 = orthologs[1]
			
			if C_fimo_pos[motif].has_key(ortholog1):
				motif_cons[motif]["amg"].append("C_elegans,"+ortholog1)
				C_pos_array = C_fimo_pos[motif][ortholog1]
				for C_pos in C_pos_array:
					C_adj_pos = adjust_pos(aln[ortholog1],C_pos)
					C_adj_pos_array.append(C_adj_pos)
				motif_cons[motif]["amg"].append("Brugia: " + ",".join(map(lambda x:str(x),B_adj_pos_array)) + "; C.elegans: " + ",".join(map(lambda x:str(x),C_adj_pos_array)))
			if O_fimo_pos[motif].has_key(ortholog2):
				motif_cons[motif]["amg"].append("OVOC,"+ortholog2)
				O_pos_array = O_fimo_pos[motif][ortholog2]
				for O_pos in O_pos_array:
					O_adj_pos = adjust_pos(aln[ortholog2],O_pos)
					O_adj_pos_array.append(O_adj_pos)
				motif_cons[motif]["amg"].append("Brugia: " + ",".join(map(lambda x:str(x),B_adj_pos_array)) + "; OVOC: " + ",".join(map(lambda x:str(x),O_adj_pos_array)))
			if min_diff(B_adj_pos_array,C_adj_pos_array) < dis_cut:
				motif_cons[motif]["cons"].append("Brugia " + gene +" : " + ",".join(map(lambda x:str(x),B_adj_pos_array)) + "@" + ",".join(map(lambda x:str(x),B_pos_array)) + "; C.elegans "+ortholog1+" : " + ",".join(map(lambda x:str(x),C_adj_pos_array)))
			if min_diff(B_adj_pos_array,O_adj_pos_array) < dis_cut:
				motif_cons[motif]["cons"].append("Brugia "+gene+" : " + ",".join(map(lambda x:str(x),B_adj_pos_array)) + "@" + ",".join(map(lambda x:str(x),B_pos_array)) + "; OVOC " +ortholog2 + " : " + ",".join(map(lambda x:str(x),O_adj_pos_array)))

out = open("motif_conservation_analysis.tsv","wb")				
for motif in motif_cons:
	if not len(motif_cons[motif]["cons"]) == 0:
		out_line = [motif] + ["conserved"] + motif_cons[motif]["cons"]
		print >>out,"\t".join(out_line)
	else:
		if not len(motif_cons[motif]["amg"]) == 0:
			out_line = [motif] + ["ambigous"] + motif_cons[motif]["amg"]
			print >>out,"\t".join(out_line)