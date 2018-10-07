import tensorflow as tf
import glob
import os
from joblib import Parallel, delayed
import pandas as pd
import seaborn as sns
import logging
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import sys
from random import choice

#input:
# [fore list]
# [total_window_list]
# [num_BG_to_test]
# [motif occurrence threshold]
# [motif_mapping_df]
# [motif_exp file]
# [motif expression threshold]
# [output_label]
# (local) -bash-4.2$ python MP_finding_foreground_and_random_BG.py test.foreground_window_pairs.list ../Motif_scanning/GAM.total_window.list 10 1 mm9.GAM.motif_window_mapping_table.csv.gz motif_TF_expression.tsv 1 test.motif_pair.csv

def get_motif_pair_occurrences_matrix(motif_mapping_df,interaction_input_list,motif_list,name):
	print name
	print interaction_input_list[0]
	print motif_list[0]
	print motif_mapping_df.head()
	left_df = motif_mapping_df.loc[map(lambda x:x[0],interaction_input_list)][motif_list]
	right_df = motif_mapping_df.loc[map(lambda x:x[1],interaction_input_list)][motif_list]


	matrix_multiply_left = pd.concat([left_df,right_df])
	matrix_multiply_right = pd.concat([right_df,left_df])

	tf_mat1 = tf.constant(matrix_multiply_left.values, dtype=tf.int32)
	tf_mat2 = tf.constant(matrix_multiply_right.values, dtype=tf.int32)
	tf_mat3 = tf.constant(left_df.values, dtype=tf.int32)
	tf_mat4 = tf.constant(right_df.values, dtype=tf.int32)

	with tf.Session() as sess:
		union_obj = tf.matmul(tf.transpose(tf_mat1),tf_mat2)

		tf_mat5 = tf.multiply(tf_mat3,tf_mat4)
		intersect_obj = tf.matmul(tf.transpose(tf_mat5),tf_mat5)

		obj = tf.subtract(union_obj,intersect_obj)

		MP_df = pd.DataFrame(obj.eval())
		MP_df.columns = motif_list
		MP_df.index = motif_list
	melt_MP_df = MP_df.where(np.triu(np.ones(MP_df.shape)).astype(np.bool))
	melt_MP_df = melt_MP_df.stack().reset_index()
	melt_MP_df.columns = ['Motif1','Motif2',name+'#Num']			
	melt_MP_df['id'] = 	melt_MP_df['Motif1'] + "%%"+melt_MP_df['Motif2']
	melt_MP_df = melt_MP_df.set_index('id')
	melt_MP_df = melt_MP_df.drop(['Motif1','Motif2'],axis=1)
	return melt_MP_df

def parse_file(file):
	lines = open(file).readlines()
	lines = map(lambda x:x.strip().split(),lines)
	# print file,number_inter,len(lines)
	return lines

def generate_BG_pairs(my_list,size):
	my_pairs=[]
	for i in range(size):
		while True:
			
			c1 = choice(my_list)
			c2 = choice(my_list)
			if c1 != c2:
				break
		my_pairs.append([c1,c2])
			
	return my_pairs

fore_pair_list = map(lambda x:x.strip().split(","),open(sys.argv[1]).readlines())
total_window_list = map(lambda x:x.strip(),open(sys.argv[2]).readlines())
num_BG_to_test = int(sys.argv[3])
threshold = int(sys.argv[4]) # a motif should occur at least this many times 
motif_mapping_df =  sys.argv[5]


motif_mapping_df = pd.read_csv(motif_mapping_df,index_col=0)
motif_mapping_df = (motif_mapping_df>=threshold).astype(int)
print motif_mapping_df.head()

motif_exp = pd.read_csv(sys.argv[6],index_col=0,sep="\t")
motif_list = motif_exp[motif_exp[motif_exp.columns[-1]] >=float(sys.argv[7])].index.tolist()

output_label = sys.argv[8]




fore_interactions_unique_regions_list = list(set([j for sub in fore_pair_list for j in sub]))
BG_candidates = list(set(total_window_list).difference(set(fore_interactions_unique_regions_list)))
print BG_candidates[0]
testing_list = [fore_pair_list]

# generate BG pairs
testing_list += Parallel(n_jobs=-1,verbose=10)(delayed(generate_BG_pairs)(BG_candidates,len(fore_pair_list)) for i in range(num_BG_to_test))


# count occurrences for each list
name_list=['Fore'] + map(lambda x:"BG."+str(x),range(num_BG_to_test))

df_list = map(lambda i:get_motif_pair_occurrences_matrix(motif_mapping_df,testing_list[i],motif_list,name_list[i]),range(num_BG_to_test+1))

df = pd.concat(df_list,axis=1)
print df.head()
df.to_csv(output_label)























