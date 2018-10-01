#!/usr/bin/env python

"""Description"""

__author__ = "Yichao Li"
__license__ = "MIT"

import sys
# import pickle



def parse_bed_file(file,promoter_length):
	my_dict = {}
	flag = True
	with open(file) as f:
		for line in f:
			if flag:
				flag = False
				continue
			line = line.strip().split()
			seq_id = line[0]
			chr = line[1]
			gene_start = int(line[2])
			gene_end = int(line[3])
			strand = line[4]
			if strand == "1":
				end = gene_start - 1
				start = end - promoter_length
				if start < 0:
					continue
				my_dict[seq_id] = [chr,str(start),str(end),seq_id+"@pos_strand",'.','+']
			if strand == "-1":
				end = gene_end + promoter_length
				start = gene_end
				if start < 0:
					continue
				my_dict[seq_id] = [chr,str(start),str(end),seq_id+"@neg_strand",'.','-']
	return my_dict


if __name__=="__main__":
	tsv_file = sys.argv[1]
	out_file = sys.argv[2]
	promoter_length = sys.argv[3]
	
	
	all_bed = parse_bed_file(tsv_file,int(promoter_length))
	out = open(out_file,'wb')
	for i in all_bed:
		print >>out,"\t".join(all_bed[i])
	out.close()

