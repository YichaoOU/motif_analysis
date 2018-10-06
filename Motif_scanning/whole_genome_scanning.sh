


# This is a fully paralleled process

motif_pwm=$1
genome_fa=$2
input_list=$3
output_motif_mapping_table=$4


python pwm_to_gene_list.py $motif_pwm $motif_pwm.list


python run_motif_scanning.py $motif_pwm.list $motif_pwm $genome_fa


python batch_fimo_sorted_bed.py 

rm *.fimo

python generate_motif_mapping_table.py $input_list sorted_bed_files/*.sorted $output_motif_mapping_table


