#!/usr/bin/env python:

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sps
import statsmodels.formula.api as smf
import statsmodels.api as sm

#___________________________________________________________________________________

# Exercise 1

### 1.1
data = pd.read_csv('aau1043_dnm.csv')
#print(data)

### 1.2 and 1.3 skipped dictionary step
roi1 = data.loc[:, 'Phase_combined'] == 'mother'
maternal_list = data.loc[roi1, "Proband_id" ]
roi2 = data.loc[:, 'Phase_combined'] == 'father'
paternal_list = data.loc[roi2, "Proband_id" ]

maternal_counts = maternal_list.value_counts()
maternal_counts = maternal_counts.rename('maternal')
paternal_counts = paternal_list.value_counts()
paternal_counts = paternal_counts.rename('paternal')

# print(maternal_counts)
# print(paternal_counts)
#print(maternal_counts.index)

deNovoCounts = pd.concat([maternal_counts, paternal_counts], axis = 1)
# print(deNovoCounts)

### 1.4
parental_df = pd.read_csv('aau1043_parental_age.csv', index_col=0)
print(parental_df)

# ### 1.5
final_dataframe = pd.concat([deNovoCounts, parental_df], axis = 1, join = "inner")
print(final_dataframe)


#_____________________________________________________________________________________

# Exercise 2

###2.1

#Use matplotlib to count of maternal de novo mutations vs. maternal age (upload as ex2_a.png in your submission directory)
#and count of paternal de novo mutations vs. paternal age (upload as ex2_b.png in your submission directory)
fig1, ax1 = plt.subplots()
xm = final_dataframe.loc[:, "Mother_age"]
ym = final_dataframe.loc[:, "maternal"]
ax1.set_xlabel("Mother Age")
ax1.set_ylabel("Maternal deNovoCounts")
ax1.set_title("Maternal Age vs. Counts")
ax1.scatter(xm, ym, color = 'pink')
fig1.savefig("ex2_a.png")
fig2, ax2 = plt.subplots()
xp = final_dataframe.loc[:, "Father_age"]
yp = final_dataframe.loc[:, "paternal"]
ax2.set_xlabel("Father Age")
ax2.set_ylabel("Paternal deNovoCounts")
ax2.set_title("Paternal Age vs. Counts")
ax2.scatter(xp, yp, color = 'lightblue')
fig2.savefig("ex2_b.png")
#plt.show()
plt.close()

###2.2
modelm = smf.ols(formula = 'maternal ~ 1 + Mother_age', data = final_dataframe).fit()
print(modelm.summary())

###2.3
modelp = smf.ols(formula = 'paternal ~ 1 + Father_age', data = final_dataframe).fit()
print(modelp.summary())

###2.4
# in README.md

###2.5 
fig3, ax3 = plt.subplots()
ax3.hist(ym, color = 'pink', label = "Maternal", alpha = 0.5)
ax3.hist(yp, color = 'lightblue', label = "Paternal", alpha = 0.5)
ax3.legend()
ax3.set_xlabel("deNovoCounts")
ax3.set_ylabel("Frequency")
ax3.set_title("Maternal vs Paternal Frequency")
fig3.savefig("ex2_c.png")
#plt.show()

### 2.6
print(sps.ttest_ind(
final_dataframe.loc[:, 'maternal'],
final_dataframe.loc[:, "paternal"]
))











