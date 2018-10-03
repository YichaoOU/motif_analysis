
import sys




import pandas as pd
df = pd.read_csv(sys.argv[2],index_col=0)
selected_motifs_name = map(lambda x:x.strip(),open(sys.argv[1]).readlines())
pos = df[df[df.columns[-1]] == 1]
neg = df[df[df.columns[-1]] == 0]
pos_size = pos.shape[0]
neg_size = neg.shape[0]
out = []
for i in selected_motifs_name:
	
	pos_number = pos[i].sum()
	neg_number = neg[i].sum()
	FGC = pos_number/float(pos_size)
	BGC = neg_number/float(neg_size)
	Ratio = FGC/BGC
	out.append([i,pos_number,neg_number,FGC,BGC,Ratio])

re = pd.DataFrame(out,columns=["Motif name",'ForeNum','BackNum',"ForeCov","BackCov","Relative Coverage"])

re.to_csv(sys.argv[3],index=False)