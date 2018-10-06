# chr1        10      20      a1      1       +
# chr1        50      60      a2      2       -
# chr1        80      90      a3      3       -
# -bash-4.2$ for i in human_*bed;do python transform_ucsc_bed_to_bedtools.py $i > anno_feature.$i;done
# sort -k1,1 -k2,2n factorbook-UA5.fimo.bed > factorbook-UA5.fimo.bed.sorted
# -bash-4.2$ for i in *.fimo; do python ../transform_fimo_to_bedtools.py $i > $i.bed ; sort -k1,1 -k2,2n $i.bed > $i.bed.sorted;done
# -bash-4.2$ for i in *.fimo; do echo $i ;python ../transform_fimo_to_bedtools.py $i > $i.bed ; sort -k1,1 -k2,2n $i.bed > $i.bed.sorted;done


import sys
flag = True
# print sys.argv[1]
with open(sys.argv[1]) as f:
	for line in f:
		if flag:
			flag = False
			continue
		line = line.strip().split()
		chr = line[1]
		start = line[2]
		end = line[3]
		name = "."
		score = line[5]
		strand = line[4]
		print "\t".join([chr,start,end,name,score,strand])
		