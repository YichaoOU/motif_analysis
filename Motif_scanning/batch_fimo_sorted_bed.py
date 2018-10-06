import os
import glob
files = glob.glob("*.fimo")
def run_command(f):
	print f
	command = "python transform_fimo_to_bedtools.py "+f+" > "+f+".bed"
	os.system(command)
	command = "sort -k1,1 -k2,2n "+f+".bed"+" > "+f+".bed"+".sorted"
	os.system(command)
from joblib import Parallel, delayed
Parallel(n_jobs=16)(delayed(run_command)(x) for x in files)

os.system("rm *.bed")
os.system("mkdir sorted_bed_files")
os.system("mv *.sorted sorted_bed_files")


