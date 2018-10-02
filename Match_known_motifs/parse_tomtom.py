def parse_tomtom(file,T):
	motif_list = {}
	for line in open(file).readlines()[1:]:
		line = line.strip().split()
		motif = line[0]
		motif1 = line[0] 
		motif2 = line[1]
		# print line
		p_value = float(line[3])
		if motif1 == motif2:
			continue
		if p_value > float(T):
			continue
		if not motif_list.has_key(motif):
			motif_list[motif]=[motif2+":"+str(p_value)]
		else:
			motif_list[motif].append(motif2+":"+str(p_value))
	return motif_list
import sys

my_list = parse_tomtom(sys.argv[1],sys.argv[3])
my_out = open(sys.argv[2],"wb")
for m in my_list:
	print >>my_out,m,",".join(my_list[m])
my_out.close()
