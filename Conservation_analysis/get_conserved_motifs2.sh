

motif_list=$1
homologs=$2
all_motifs_pwm=$3
species1_fasta=$4
label1=$5
species2_fasta=$6
label2=$7
output=$8


python ./subPWM.py $motif_list.pwm $all_motifs_pwm $motif_list

python ./do_MSA2.py $homologs $species1_fasta $species2_fasta

fimo -text --no-qvalue $motif_list.pwm $species1_fasta > $species1_fasta.fimo

fimo -text --no-qvalue $motif_list.pwm $species2_fasta > $species2_fasta.fimo

python ./check_conservation2.py $species1_fasta.fimo $label1 $species2_fasta.fimo $label2 $output


