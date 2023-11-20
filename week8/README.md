1.1

Rscript runChicago.R raw/PCHIC_data/GM_rep1.chinput,raw/PCHIC_data/GM_rep2.chinput,raw/PCHIC_data/GM_rep3.chinput output --design-dir raw/Design --en-feat-list raw/Features/featuresGM.txt --export-format washU_text


1.2
Do these enrichments make sense to you? Are any surprising? Explain your reasoning briefly for each feature.

yes, CTCF-bound to promoters, H3K4me1 and H3k27ac are euchromatin marks with significant overlap at promoter regions which makes sense. H3K4me3 are associated with active genes and are very similar to the CTCF, which makes sense. H3K9me3, and H3K27me3 are heterochromatin marks are less than the CTCF, not interacting with promoters which makes sense. All of the overlaps are expected when compared to CTCF, so nothing is paticularly surprising. 


2.2
Top 6 interactions of pro-pro:

chr20	52476392	52560771	.	143	5.0	.	0	chr20	52556648	52560771	AC005220.3	+	chr20	52476392	52480847	.	-
chr20	25227277	25324806	.	143	5.0	.	0	chr20	25227277	25231213	PYGB	+	chr20	25317055	25324806	.	-
chr21	33755386	33938278	.	143	5.0	.	0	chr21	33755386	33767163	C21orf119;URB1	+	chr21	33933703	33938278	.	-
chr20	36954175	37001381	.	143	5.0	.	0	chr20	36954175	36958047	CTD-2308N23.2	+	chr20	36998177	37001381	.	-
chr20	60635322	60762448	.	143	5.0	.	0	chr20	60756847	60762448	MTG2	+	chr20	60635322	60638149	.	-
chr20	55627168	55850068	.	143	5.0	.	0	chr20	55627168	55633941	AL117380.1	+	chr20	55839193	55850068	BMP7;RP4-813D12.3	+

working on other interactions :(
