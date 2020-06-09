# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:08:17 2020

@author: Tyler
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from sklearn.preprocessing import PowerTransformer

df = pd.read_csv(r'C:\Users\Tyler\Desktop\Projects\LA-RMSD COVID Challenge\Working files\Python export\Visitor Traffic by Zip Code.csv')

#statistics
mu = np.mean(df['raw_visitor_counts'])
sigma = np.std(df['raw_visitor_counts'])
x = df['raw_visitor_counts']
fig, ax = plt.subplots()
num_bins = 25

#histogram
n, bins, patches = ax.hist(x, num_bins, facecolor='blue')

#best fit line
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
ax.set_xlabel('Number of Visitors')
ax.set_ylabel('Probability')
ax.set_title(r'Histogram of Distribution of Visitors')

fig.tight_layout()
plt.show()

#statistics
mu = np.mean(df['raw_visit_counts'])
sigma = np.std(df['raw_visit_counts'])
x = df['raw_visit_counts']
fig, ax = plt.subplots()
num_bins = 25

#histogram
n, bins, patches = ax.hist(x, num_bins, facecolor='blue')

#best fit line
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y,'--')
ax.set_xlabel('Number of Visits')
ax.set_ylabel('Probability')
ax.set_title(r'Histogram of Distribution of Visits')

fig.tight_layout()
plt.show()

#transforming data for normalization for both variables
pow_trans = PowerTransformer()

pow_trans.fit(df[['raw_visit_counts']])
df['raw_visit_counts_log'] = pow_trans.transform(df[['raw_visit_counts']])

df[['raw_visit_counts_log']].hist()
plt.show()

pow_trans = PowerTransformer()

pow_trans.fit(df[['raw_visitor_counts']])
df['raw_visitor_counts_log'] = pow_trans.transform(df[['raw_visitor_counts']])

df[['raw_visitor_counts_log']].hist()

plt.show()


# Exporting to csv
# df.to_csv(r'C:\Users\Tyler\Desktop\Projects\LA-RMSD COVID Challenge\Working files\Python export\Transformed data.csv')
