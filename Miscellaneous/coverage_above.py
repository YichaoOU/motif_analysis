
import sys




import pandas as pd
df = pd.read_csv(sys.argv[1],index_col=0)
pos = df[df[df.columns[-1]] == 1]
pos_size = pos.shape[0]
T = float(sys.argv[2]) * pos_size
print len(pos.columns[pos.sum() >= T].tolist())
print pos.columns[pos.sum() >= T].tolist()

