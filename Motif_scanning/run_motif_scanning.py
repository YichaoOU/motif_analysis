
from joblib import Parallel, delayed
import os
import sys 

motif_list_file=sys.argv[1]
motif_pwm_file=sys.argv[2]
genome_fa_file=sys.argv[3]
def run_fimo(motif_id):
	command = "fimo --max-stored-scores 9999999999 --no-qvalue --motif " + motif_id  + " --text "+motif_pwm_file+"  "+genome_fa_file+" > " + motif_id+".fimo"
	print command
	os.system(command)

my_motifs = []
with open(motif_list_file) as ds:
	for line in ds:
		line = line.strip()
		if len(line) == 0:
			continue
		my_motifs.append(line)
		

Parallel(n_jobs=8)(delayed(run_fimo)(x) for x in my_motifs)
