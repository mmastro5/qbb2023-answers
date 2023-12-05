#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# normalization
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]
counts_df_normed = np.log2(counts_df_normed + 1)


# creating design matrix
full_design_df = pd.concat([counts_df_normed, metadata], axis=1)
full_design_df['DTHHRDY'] = full_design_df['DTHHRDY'].fillna(1.0)


# running regression for a gene
model = smf.ols(formula = 'Q("DDX11L1") ~ SEX', data=full_design_df)
results = model.fit()

slope = results.params[1]
pval = results.pvalues[1]

# # # for loop for all genes
# genes = list(full_design_df.columns.values)
# genes = genes[: len(genes)-3]

# #all_results = {'Gene_ID': [], 'Slope': [], 'P_Value': []}
# f = open('all_results', 'w')
# f.write('gene\tslope\tpval\n')

# for gene in genes:
# 	model = smf.ols(formula = 'Q("'+gene+'") ~ SEX', data=full_design_df)
# 	results = model.fit()
# 	slope = results.params[1]
# 	pval = results.pvalues[1]

# 	#f.write(gene + '\t' + str(slope) + '\t' + str(pval) + '\n')
# 	f.write(f'{gene}\t{slope}\t{pval}\n')

# f.close()

my_dataframe = pd.read_csv("all_results", header=0, index_col=False, sep='\t')
my_dataframe['pval'] = my_dataframe['pval'].fillna(1.0)

my_dataframe["rejected"], my_dataframe['corrected'] = multitest.fdrcorrection(my_dataframe['pval'], alpha =0.10, method = 'indep', is_sorted = False)

#print(my_dataframe)

FDR_hits = my_dataframe.loc[my_dataframe['corrected'] <= 0.1]
FDR_hits2 = FDR_hits['gene'].tolist()
FDR_hits.to_csv("Step1hits")

# trying PyDESeq2

dds = DeseqDataSet(
    counts=counts_df,
    metadata=metadata,
    design_factors="SEX",
    n_cpus=4,
)

dds.deseq2()
stat_res = DeseqStats(dds)
stat_res.summary()
results_df = stat_res.results_df
print(results_df)

results_df['padj'] = results_df['padj'].fillna(1.0)
print(results_df)

ddsFDR_genes = results_df.loc[results_df['padj'] <= 0.1]
ddsFDR_genes.to_csv("DeseqDataSet_10percentFDRgenes.txt", header = None, index = None, sep = '\t')
significant_genes = results_df[(results_df['padj'] <= 0.1) & (abs(results_df['log2FoldChange']) < 1)]
significant_genes.to_csv("Step2hits")

print(significant_genes)
sg2 = significant_genes.index.tolist()

#creating lists of genes because idk why
in_FDR = set(FDR_hits2)
in_significant_genes = set(sg2)

both = in_FDR.intersection(in_significant_genes)
unique = in_FDR.difference(in_significant_genes)


# Creating Jaccard index - intersct of two lists and the union of two lists
j_index = len(unique)/len(both) * 100
print(j_index)


# # volcano plot
# plt.figure(figsize=(12, 9))
# plt.scatter(results_df['log2FoldChange'], -np.log10(results_df['padj']), color='gray', label='Non-Significant')
# plt.scatter(significant_genes['log2FoldChange'], -np.log10(significant_genes['padj']), color='hotpink', label='Significant (FDR<0.1, |log2FC|>1)')

# plt.xlabel('log2FoldChange')
# plt.ylabel('-log10(padj)')
# plt.title('Volcano Plot')

# plt.axvline(x=0, linestyle='--', color='black', linewidth=0.8)
# plt.axhline(y=-np.log10(0.1), linestyle='--', color='black', linewidth=0.8)
# plt.legend(loc = 3)

# # Save plot as .png
# plt.savefig('volcano_plot.png')















