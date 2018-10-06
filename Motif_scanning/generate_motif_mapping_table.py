
import os
import glob
from joblib import Parallel, delayed
import pandas as pd
import sys 

output = open(sys.argv[1]+".bed","wb")

sorted_files_pattern = sys.argv[2]

output_table = sys.argv[3]

def reformat(x):
	chr,pos = x.split(":")
	start,end = pos.split("-")
	return [chr,start,end,x]

def run_command(f):
	print f
	command = "bedtools intersect -a "+sys.argv[1]+".bed.sorted"+" -b "+f+" -F 1 -c -sorted > " + f.split("/")[-1] + ".count"
	os.system(command)

def read_df(f):
	columns = ['chr','start','stop','name'] + [f.split(".fimo")[0]]
	df = pd.read_csv(f,sep="\t",header=None,names = columns,usecols = columns[3:])
	df = df.set_index(df.columns[:-1].tolist())
	# print df.head()
	return df
	
# list to bed 
result_list = map(lambda x:reformat(x),map(lambda y:y.strip(),open(sys.argv[1]).readlines()))
for x in result_list:
	print >>output,"\t".join(x)

output.close()

# sort bed
os.system("sort -k1,1 -k2,2n "+sys.argv[1]+".bed"+" > "+sys.argv[1]+".bed.sorted")

# run bedtools
files = glob.glob(sorted_files_pattern)
Parallel(n_jobs=16)(delayed(run_command)(x) for x in files)

# construct motif mapping table
files = glob.glob("*.count")
df_list = Parallel(n_jobs=16)(delayed(read_df)(x) for x in files)
df = pd.concat(df_list,axis=1)
print df.head()


df.to_csv(output_table)
os.system("rm *.count")
os.system("rm "+sys.argv[1]+".bed*")
