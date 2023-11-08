#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import sys 
import pandas as pd
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

def parse_bedgraph(fname):
    data = set()
    coverage = []
    methylation = set()
    with open(fname, 'r') as file:
        for line in file:
            parts = line.strip().split()
            #chromosome = parts[0]
            start = int(parts[1])
            #end = int(parts[2])
            methylation = float(parts[3])
            cov = int(parts[4])
            data.add(start)
            coverage.append(cov)
    return data, coverage, methylation

#normal_ONT, tumor_ONT, normal_bisulfite_f, tumor_bisulfite_f, output = sys.argv[1:6]

# Load Data
normal_ONT, normal_bisulfite_f, sample_ONT, tumor_ONT, sample_bi, tumor_bi = sys.argv[1:7]

# Parse Data
normal, normal_coverage, normal_meth = parse_bedgraph(normal_ONT)
normal_bisulfite, normal_bisulfite_coverage, normal_bisulfite_meth = parse_bedgraph(normal_bisulfite_f)
sample, sample_coverage, sample_meth = parse_bedgraph(sample_ONT)
tumor, tumor_coverage, tumor_meth = parse_bedgraph(tumor_ONT)
sample_bi, sample_coverage_bi, sample_meth_bi = parse_bedgraph(sample_bi)
tumor_bi, tumor_coverage_bi, tumor_meth_bi = parse_bedgraph(tumor_bi)

# counting differences 
normal_nano = set()
normal_bi = set()
normal_all = set()
for i in normal:
    if i not in normal_bisulfite:
        normal_nano.add(i)
    else:
        normal_all.add(i)
for i in normal_bisulfite:
    if i not in normal:
        normal_bi.add(i)

# Getting the percent of hits in each model and in both
print(len(normal_nano) / (len(normal_bi)+len(normal_all)) *100)
print(len(normal_bi)/ (len(normal_bi)+len(normal_all)) *100)
print(len(normal_all)/ (len(normal_bi)+len(normal_all)+len(normal_nano)) *100)
#normal_single = normal_set.difference(normal_multi)

#plotting the histogram
fig, ax = plt.subplots()
ax.hist(normal_coverage, label = "Nano", alpha = 0.5, bins = 450, color = "limegreen")
ax.set_xlim(0,100)
ax.set_ylabel("Counts")
ax.set_xlabel("Coverage")
ax.set_title("Coverage Data")
ax.legend()
ax.hist(normal_bisulfite_coverage, label = "Bisulfite", alpha = 0.5, bins = 1050, color = "hotpink")
plt.savefig("Coverage.png")


#Histogram of CpG differences 

# nano_data = pd.read_csv('normal.ONT.chr2.bedgraph', delim_whitespace = True)
# bi_data = pd.read_csv("normal.bisulfite.chr2.bedgraph", delim_whitespace = True)

ONT_meth_scores = {}
with open('ONT.cpg.chr2.bedgraph', 'r') as file:
    for line in file:
        parts = line.strip().split()
        start = int(parts[1])
        methylation = float(parts[3])
        ONT_meth_scores[start] = methylation


bi_meth_scores = {}
with open('bisulfite.cpg.chr2.bedgraph', 'r') as file:
    for line in file:
        parts = line.strip().split()
        start = int(parts[1])
        methylation = float(parts[3])
        bi_meth_scores[start] = methylation

nanolist = []
bilist = []
nano_bi_diff = []
for i in normal_all:
	#print(i)
	nanolist.append(ONT_meth_scores[i])
	bilist.append(bi_meth_scores[i])
	if ONT_meth_scores[i] != bi_meth_scores[i]:
		nano_bi_diff.append(ONT_meth_scores[i]-bi_meth_scores[i])
plt.close()

# fig, ax = plt.subplots()
# inferno = cm.get_cmap('cubehelix')
# plt.set_cmap(inferno)
# hist, x_edges, y_edges = np.histogram2d(nanolist, bilist)
# hist =  np.log10(hist + 1)
# pearson_r = np.corrcoef(nanolist, bilist)[0, 1]
# print(pearson_r)
# #plt.imshow(hist, extent=[x_edges[0], x_edges[-1], y_edges[0], y_edges[-1]])
# plt.imshow(hist, extent=[x_edges[0], x_edges[-1], y_edges[0], y_edges[-1]])
# plt.colorbar(label='log10(count + 1)')
# plt.xlabel('Nano Score ')
# plt.ylabel('Bisulfite Score')
# plt.title(f"Pearson R: {pearson_r}")
# plt.savefig("histogram2d")
# plt.close()


# Violin plot for tumor vs normal
ONT_tumor_only = set()
ONT_sample_only = set()
ONT_both_sample_tumor = set()
for i in tumor:
    if i not in sample:
        ONT_tumor_only.add(i)
    else:
        ONT_both_sample_tumor.add(i)
for i in sample:
    if i not in tumor:
        ONT_tumor_only.add(i)

tumor_only_bi = set()
sample_only_bi = set()
both_sample_tumor_bi = set()
for i in tumor_bi:
    if i not in sample_bi:
        tumor_only_bi.add(i)
    else:
        both_sample_tumor_bi.add(i)
for i in sample_bi:
    if i not in tumor_bi:
        tumor_only_bi.add(i)

sample_meth_scores_ONT = {}
with open('normal.ONT.chr2.bedgraph', 'r') as file:
    for line in file:
        parts = line.strip().split()
        start = int(parts[1])
        methylation = float(parts[3])
        sample_meth_scores_ONT[start] = methylation


tumor_meth_scores_ONT = {}
with open('tumor.ONT.chr2.bedgraph', 'r') as file:
    for line in file:
        parts = line.strip().split()
        start = int(parts[1])
        methylation = float(parts[3])
        tumor_meth_scores_ONT[start] = methylation

tumor_meth_scores_bi = {}
with open('tumor.bisulfite.chr2.bedgraph', 'r') as file:
    for line in file:
        parts = line.strip().split()
        start = int(parts[1])
        methylation = float(parts[3])
        tumor_meth_scores_bi[start] = methylation

sample_meth_scores_bi = {}
with open('normal.bisulfite.chr2.bedgraph', 'r') as file:
    for line in file:
        parts = line.strip().split()
        start = int(parts[1])
        methylation = float(parts[3])
        sample_meth_scores_bi[start] = methylation

bi_r = []
nano_r = []
for i in both_sample_tumor_bi:
	if i in ONT_both_sample_tumor:
		nano_r.append(sample_meth_scores_ONT[i]-tumor_meth_scores_ONT[i])
		bi_r.append(sample_meth_scores_bi[i]-tumor_meth_scores_bi[i])

ONT_tumor_sample_diff = []
for i in ONT_both_sample_tumor:
	if tumor_meth_scores_ONT[i] != sample_meth_scores_ONT[i]:
		ONT_tumor_sample_diff.append(sample_meth_scores_ONT[i]-tumor_meth_scores_ONT[i])

bi_tumor_sample_diff = []
for i in both_sample_tumor_bi:
	if tumor_meth_scores_bi[i] != sample_meth_scores_bi[i]:
		bi_tumor_sample_diff.append(sample_meth_scores_bi[i]-tumor_meth_scores_bi[i])


fig, ax = plt.subplots()
ax.violinplot([ONT_tumor_sample_diff, bi_tumor_sample_diff])
ax.set_xticks([1,2], ["nano tumor/sample", "bisulfite tumor/sample"])
pearson_r_violin = np.corrcoef(nano_r, bi_r)[0, 1]
ax.set_title(f"Pearson R: {pearson_r_violin}")
# for pc in v["bodies"]:
# 	pc.set_facecolor("hotpink")
plt.savefig("violin")


















