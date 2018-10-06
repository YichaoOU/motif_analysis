









# Whole Genome Motif Scanning

### Why and when you need to do it?

If you have multiple input files and the sequences are very long, then it will be much faster and convenient to first do motif scanning on the whole genome and then run `bedtools` to extract motif mapping info for each file.

### HOW TO

1. Download the mm9 genome: http://hgdownload.soe.ucsc.edu/goldenPath/mm9/bigZips/chromFa.tar.gz

`tar -zxvf chromFa.tar.gz`

`cat *.fa > mm9.fa`

`rm chr*.fa`

2. `./whole_genome_scanning.sh [motif_pwm] [genome_fa] [input_list] [output_motif_mapping_table]`

Example: `./whole_genome_scanning.sh HOCOMOCOv11_core_MOUSE_mono_meme_format.meme mm9.fa GAM.total_window.list mm9.GAM.motif_window_mapping_table.csv`