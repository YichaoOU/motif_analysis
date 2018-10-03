
## Given motif list, output the statistics

`python individual_coverage.py sample_motif.list HRGP_raw_both_strand.csv sample_motif.list.csv`


| Motif name     | ForeNum | BackNum | ForeCov | BackCov | Relative Coverage |
|----------------|---------|---------|---------|---------|-------------------|
| DME_GADGAYKAS  | 11      | 25      | 85%     | 19%     | 4.467692          |
| DME_GRHTGDTGA  | 11      | 27      | 85%     | 20%     | 4.136752          |
| DME_MARKGDSRGA | 11      | 29      | 85%     | 22%     | 3.851459          |

## Output all motifs with FGC > X%.


`python coverage_above.py HRGP_raw_both_strand.csv 1`

38
['gimme_100_Improbizer_ACGAAAGAGAGAGAAAAG', 'gimme_140_MEME_1_w12', 'gimme_141_MEME_2_w12', 'gimme_136_MEME_7_w10', 'gimme_20_BioProspector_w12_5', 'gimme_142_MEME_3_w12', 'gimme_133_MEME_4_w10', 'gimme_153_MEME_4_w14', 'gimme_151_MEME_2_w14', 'gimme_105_Improbizer_AACACACGTTTATTAGATGTTT', 'gimme_25_BioProspector_w14_5', 'gimme_157_MEME_8_w14', 'gimme_135_MEME_6_w10', 'DECOD_Motif1_14', 'DECOD_Motif1_15', 'DECOD_Motif2_15', 'DECOD_Motif1_16', 'DECOD_Motif3_16', 'DECOD_Motif2_16', 'DME_TWTTTKTTCTT', 'DME_TTTTATTTRKTT', 'DME_TKYKYTTTCT', 'DME_TTTKYTCTTTT', 'DME_TDTTTTMTTTTTS', 'DME_YTRTTTTATTTTT', 'DME_KTTTCTTTTT', 'DME_TRTTTTMTTYTT', 'DME_KTTTTTTSTTT', 'DME_KATTTTATTTKT', 'DME_TTTTTBTTKTT', 'DME_AGAAAAARRA', 'DME_TGTTTTVTTT', 'DME_TTTTATTTTTM', 'DME_TKTTTCTDTT', 'DME_TYTATTTTATTT', 'DME_TRTTTTATTTK', 'DME_RTTTTMTTTTTS', 'class']

**Note** that the last column 'class' is included

