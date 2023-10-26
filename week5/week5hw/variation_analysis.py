#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

#3.0
#______________________________________________________________________________________
read_depth = []
geneotype_quality = []
allele_freq = []
predictions = []

for line in open("annotated.vcf"):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')

    for chrom in fields[9:]:
    	if chrom.split(':')[2] != '.':
    		depth = chrom.split(':')[2]
    		depth = depth.split(',')[0]
    		depth = int(depth)
    		read_depth.append(depth)
    	if chrom.split(':')[1] != '.':
    		GQ = float(chrom.split(':')[1])
    		geneotype_quality.append(GQ)

    freq = fields[7].split(';')[3][3:]
    var_freq = freq.split(',')[0]
    var_freq = float(var_freq)
    allele_freq.append(var_freq)


    pred = fields[7].split(';')[41][5:]
    pred = pred.split('|')[2]
    pred = pred.split(',')[0]
    predictions.append(pred)
pred_count = []
pred_effect = []
for p in set(predictions):
	pred_effect.append(p)
	pred_count.append(predictions.count(p))


# print(geneotype_quality)
# print(read_depth)
# print(allele_freq)	
# print(predictions)	
    		
    

fig, axs = plt.subplots(1,4, figsize=[20,10])
plt.tight_layout()
plt.xticks(rotation=90)

#3.1
## make histogram of D=DP,Number=1,Type=Integer,Description="Read Depth"
axs[0].set_title("Read Depths")
axs[0].hist(read_depth, color = "red", bins = 1200)
axs[0].set_xlabel("Read Depth")
axs[0].set_ylabel("Counts")
axs[0].set_xlim(0,20)
axs[0].set_ylim(0,200000)
# 3.2
## make histogram of ID=GQ,Number=1,Type=Integer,Description="Genotype Quality"
axs[1].set_title("Genotype Quality")
axs[1].hist(geneotype_quality, color = "blue", bins = 1100)
axs[1].set_xlabel("Genotype Quality")
axs[1].set_ylabel("Counts")
axs[1].set_ylim(0,70000)
axs[1].set_xlim(0,30)
# 3.3 
## make histogram of INFO=<ID=AF,Number=A,Type=Float,Description="Allele Frequency"
axs[2].set_title("Allele Frequency")
axs[2].hist(allele_freq, color = "black", bins = 100)
axs[2].set_xlabel("Alelle Frequency")
axs[2].set_ylabel("Counts")
axs[2].set_ylim(0,7500)
# 3.4
## make bar graph of predicted effects (in annotated VCF)
axs[3].set_title("Predicted Effects")
axs[3].bar(pred_effect, pred_count, color = "hotpink")
axs[3].set_xlabel("Predicted Effects")
axs[3].set_ylabel("Counts")


fig.savefig("Graphs", bbox_inches="tight")

















