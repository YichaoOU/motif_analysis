
python /home/bobcat/project/Brugia/subPWM.py matched_motifs.pwm ../up_in_F30_motif_scanning_final_motifs.pwm ../matched_motif.list ../motif_p_value.list ;
 
python /home/bobcat/project/Brugia/do_MSA.py ../up_in_F30 ; fimo -text --no-qvalue matched_motifs.pwm /users/PHS0293/ohu0404/project/Brugia/conservation/elegans_promoters.1000.fa > elegans.fimo ; 

fimo -text --no-qvalue matched_motifs.pwm /users/PHS0293/ohu0404/project/Brugia/conservation/OVOC_promoters.1000.fa > OVOC.fimo ; 

cp /home/bobcat/project/Brugia/check_conservation.py . ; 

python check_conservation.py /home/bobcat/project/Brugia/task1.1/up_in_F30_motif_scanning/up_in_F30_motif_scanning_Motif_Scanning/up_in_F30_motif_scanning_fore_Fimo/fimo.txt &


