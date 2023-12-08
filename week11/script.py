#!/usr/bin/env python

import sys

import scanpy as sc
import numpy
import matplotlib.pyplot as plt

# Read the 10x dataset filtered down to just the highly-variable genes
adata = sc.read_h5ad("variable_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 


# Step 1.1: Computing a neighborhood graph
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)


# Step 1.2: Leiden clustering
sc.tl.leiden(adata)

# Step 1.3: Visualizing clusters
sc.tl.umap(adata, maxiter = 900)
sc.tl.tsne(adata)


# # Plotting
# fig, ax = plt.subplots(ncols=2)
# sc.pl.umap(adata, color = 'leiden', title = "Umap", show = False, ax = ax[0])
# sc.pl.tsne(adata, color = 'leiden', title = "Tsne", show = False, ax = ax[1])
# plt.tight_layout()
# plt.savefig("Exercise1.png")


adata_copy = adata.copy()

# Step 2.1: Ranking genes in each cluster
wilcoxon_adata = sc.tl.rank_genes_groups(adata, method = 'wilcoxon', groupby='leiden', use_raw=True, copy=True)
#wilcoxon_adata = adata.copy()
logreg_adata = sc.tl.rank_genes_groups(adata, method = 'logreg', groupby='leiden', use_raw=True, copy=True)
#logreg_adata = adata.copy()


# Step 2.2: Visualizing marker genes
# #fig, ax = plt.subplots(ncols=2)
# sc.pl.rank_genes_groups(wilcoxon_adata, n_genes = 25, title = "Wilcox", sharey=False, show=False, use_raw=True)
# plt.savefig('wilcoxon.png')

# sc.pl.rank_genes_groups(logreg_adata, n_genes = 25, title = 'Log-reg', sharey=False, show=False, use_raw=True)
# plt.savefig('logreg.png')


#Step 3.1: Reload Missing Genes
leiden = adata.obs['leiden']
umap = adata.obsm['X_umap']
tsne = adata.obsm['X_tsne']
adata = sc.read_h5ad('filtered_data.h5')
adata.obs['leiden'] = leiden
adata.obsm['X_umap'] = umap
adata.obsm['X_tsne'] = tsne
adata.write('filtered_clustered_data.h5')

adata = sc.read_h5ad("filtered_clustered_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 


# Step 3.2: Matching genes to cell types - why am i googling genes rn 

marker_genes = [] # sorry i cannot google genes at this moment in time





