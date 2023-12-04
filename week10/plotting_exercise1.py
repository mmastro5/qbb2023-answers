#!/usr/bin/env python


import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# normalize
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# log
counts_df_logged = np.log2(counts_df_normed + 1)

# merge with metadata
full_design_df = pd.concat([counts_df_logged, metadata], axis=1)

#print(full_design_df)

## 1.1 data
data1 = full_design_df.iloc[4].tolist()
data1 = data1[: len(data1)-3]
data1 = [i for i in data1 if i != 0]
#print(data1)
#plotting
plt.figure(figsize = (10,10))
plt.hist(data1, bins = 80, color = 'crimson') 
plt.xlabel("logged normalized counts")
plt.ylabel("Counts")
plt.title("GTEX-113JC Gene Expression")
plt.tight_layout()
plt.savefig("histogram1.1.png")
plt.close()


#1.2 data -- 1 is male, 2 is female 
data2 = full_design_df.filter(['MXD4','SEX'], axis=1)
d2m = data2[data2['SEX'] == 1]
d2f = data2[data2['SEX'] == 2]
#plotting
plt.figure(figsize = (10,10))
plt.hist(d2m['MXD4'], label = "male", color = "midnightblue", bins = 80) 
plt.hist(d2f['MXD4'], label = "female", color = "deeppink", bins = 80) 
plt.legend()
plt.xlabel("logged normalized counts")
plt.ylabel("Counts")
plt.title("Distribution of Expression of gene MXD4")
plt.tight_layout()
plt.savefig("histogram1.2.png")
plt.close()

# 1.3 data
data3_counts =  full_design_df['AGE'].value_counts().sort_index()

plt.figure(figsize = (10,10))
data3_counts.plot(kind='bar', color = "green")
plt.legend()
plt.ylabel("number of subject")
plt.xlabel("age category")
plt.title("Subjects per Age Category")
plt.tight_layout()
plt.savefig("barplot1.3.png")
plt.close()


#1.4 data

fig, ax = plt.subplots(figsize=(10, 10))

full_design_df = full_design_df.reset_index()
# data4 = full_design_df[["LPXN", "SEX", "AGE"]]
median_by_age_sex = full_design_df.groupby(['AGE', 'SEX'])['LPXN'].median().reset_index()
male_medians = []
female_medians = []
for line in range(len(median_by_age_sex)):
    sex = median_by_age_sex.at[line, "SEX"]
    value = median_by_age_sex.at[line, "LPXN"]
    if sex == 1:
        male_medians.append(value)
    elif sex == 2:
        female_medians.append(value)
time = ["20-29", "30-39", "40-49", "50-59", "60-69", "70-79"]
ax.plot(time, male_medians, label= 'male', color = "midnightblue")
ax.plot(time, female_medians, label= 'female', color = "deeppink")
ax.set_xlabel("age categories")
ax.set_ylabel("median value")
plt.title("Median expression of LPXN by Age")
ax.legend()
fig.tight_layout()
fig.savefig("plot1.4.png")



