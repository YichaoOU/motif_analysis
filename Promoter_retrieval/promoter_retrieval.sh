#!/bin/bash


BioMart_gene_tsv=$1
Genome_fasta=$2
Promoter_length=$3
gene_list=$4

python BioMart_tsv_To_Promoter_bed.py $BioMart_gene_tsv $BioMart_gene_tsv.bed $Promoter_length


bedtools getfasta -fi $Genome_fasta -bed $BioMart_gene_tsv.bed -s -name > $BioMart_gene_tsv.bed.fa

python Create_FG_BG_fasta_files.py $gene_list $BioMart_gene_tsv.bed.fa

