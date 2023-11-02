#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#1.1 in README

#1.2
pc = np.loadtxt('plink.eigenvec')

figa, (axa1, axa2) = plt.subplots(nrows=1, ncols=2, figsize = (8,13))
x = pc[:,2]
y =pc[:,3]


axa1.scatter(x,y, color = 'hotpink')
axa1.set_xlabel('PC1')
axa1.set_ylabel('PC2')
axa1.set_title("Genotype PCs")



#2.1 in README

#2.2
freqs = np.loadtxt('allele_frequencies.frq', skiprows = 1, usecols = 4)

#figb, axb = plt.subplots()

axa2.hist(freqs, color = "limegreen", bins = 82)
axa2.set_xlabel('MAF')
axa2.set_ylabel('counts')
axa2.set_title("AlleleFrequency")

figa.savefig("GenotypeGraph_Allele.png")
#figb.savefig("AlleleGraph.png")


#3.1 in README

#3.2

# For the first GWAS analysis
analysis1_data = pd.read_csv("phenotypeA_gwas_results.assoc.linear", delim_whitespace = True)

# For the second GWAS analysis
analysis2_data = pd.read_csv("phenotypeB_gwas_results.assoc.linear", delim_whitespace = True)

# Get DATA
# For the first GWAS analysis
analysis1_data['-log10_p'] = -(np.log10(analysis1_data['P']))

# For the second GWAS analysis
analysis2_data['-log10_p'] = -(np.log10(analysis2_data['P']))

# Manhattan plot
# Create a single figure with two panels
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize = (13,8))
ax1.scatter(analysis2_data['BP'], analysis1_data['-log10_p'], c=analysis1_data['P'] < 1e-5, cmap='spring')
ax1.set_xlabel("SNP index")
ax1.set_ylabel("-log10(P-Value)")
ax1.set_title("GS451_IC50")
ax1.axhline(-np.log10(1e-5), color='black', linestyle='--', linewidth=1, label = "Threshold")
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_ylim(0,10)
ax1.legend()

ax2.scatter(analysis2_data['BP'], analysis2_data['-log10_p'], c= analysis2_data['P'] < 1e-5, cmap='autumn')
ax2.set_xlabel("SNP index")
ax2.set_ylabel("-log10(P-Value)")
ax2.set_title("CB1908_IC50")
ax2.axhline(-np.log10(1e-5), color='black', linestyle='--', linewidth=1, label = "Threshold")
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_ylim(0,10)
ax2.legend()

plt.tight_layout()
plt.savefig("manhattan_combined_plot.png")


#3.3 
#create the boxplot of top associations 
figc, axc = plt.subplots()
BP_max = np.max(analysis1_data['-log10_p'])
rowID = analysis1_data[analysis1_data['-log10_p'] == BP_max]
snpID = rowID.loc[:,'SNP'].values[0]

BP2_max = np.max(analysis2_data['-log10_p'])
rowID2 = analysis2_data[analysis2_data['-log10_p'] == BP2_max]
snpID2 = rowID2.loc[:,'SNP'].values[0]


genotype_vcf = pd.read_csv('genotypes.vcf', delimiter='\t', skiprows =27)
snpInterest = genotype_vcf[genotype_vcf['ID'] == snpID]
phenotypeInterest= pd.read_csv('GS451_IC50.txt', delim_whitespace = True)
wt = []
het = []
hom = []

for i in range(len(snpInterest.values[0])):
	if snpInterest.values[0][i] == '0/0':
		wt.append(phenotypeInterest.iloc[i-7, 2])
	elif snpInterest.values[0][i] == '0/1':
		het.append(phenotypeInterest.iloc[i-7, 2])
	elif snpInterest.values[0][i]== '1/1':
		hom.append(phenotypeInterest.iloc[i-7, 2])
	else:
		continue

boxdata = [wt, het, hom]

for j in range(len(boxdata)):
	boxdata[j] = [x for x in boxdata[j] if str(x) != 'nan']

axc.boxplot(boxdata)
axc.set_title("boxplot with love")
axc.set_xlabel("Genotype")
axc.set_ylabel("Phenotype")
figc.savefig("Boxplot")
print(snpID2)


