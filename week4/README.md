Step 2: 
OUTPUT:
(base) [~/qbb2023-answers/week4 $]wc - l sample1_peaks.bed 
      42     126    1008 sample1_peaks.bed
      42     126    1008 total
(base) [~/qbb2023-answers/week4 $]wc - l sample2_peaks.bed 
      33      99     792 sample2_peaks.bed
(base) [~/qbb2023-answers/week4 $]wc - l combined_peaks.bed 
      32      96     768 combined_peaks.bed

sample 1 = 32/42 = 0.76
sample 2 = 32/33 = 0.97

Step 3:
How reproducible are the peaks called between the two samples? 
The peaks look very similar, suggesting the sample is a good representation of the area we are investigating, so the rest of the chromosome could look similar as well. Perhaps both samples are wildtype?

 Is the p-value range of a peak indicative of reproducibility?
Yes, because the p-value are able to give acccurate sample overlap making it indicitave to reproducibility

 Is it completely consistent?
 No, because there are some line ups where high pvalues are observed but the sequences are not accurately overlapping. 
