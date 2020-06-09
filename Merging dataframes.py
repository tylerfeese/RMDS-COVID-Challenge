# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:35:58 2020

@author: Tyler
"""

import pandas as pd

df1 = pd.read_csv(r'C:\Users\Tyler\Desktop\Projects\LA-RMSD COVID Challenge\Safegraph\patterns_backfill\2020\05\07\12\2020\04\patterns-part1.csv\patterns-part1.csv')
df2 = pd.read_csv(r'C:\Users\Tyler\Desktop\Projects\LA-RMSD COVID Challenge\Safegraph\patterns_backfill\2020\05\07\12\2020\04\patterns-part2.csv\patterns-part2.csv')
df3 = pd.read_csv(r'C:\Users\Tyler\Desktop\Projects\LA-RMSD COVID Challenge\Safegraph\patterns_backfill\2020\05\07\12\2020\04\patterns-part3.csv\patterns-part3.csv')
df4 = pd.read_csv(r'C:\Users\Tyler\Desktop\Projects\LA-RMSD COVID Challenge\Safegraph\patterns_backfill\2020\05\07\12\2020\04\patterns-part4.csv\patterns-part4.csv')

df1 = df1.loc[:,df1.columns.intersection(['postal_code','raw_visitor_counts','raw_visit_counts'])]
df2 = df2.loc[:,df2.columns.intersection(['postal_code','raw_visitor_counts','raw_visit_counts'])]
df3 = df3.loc[:,df3.columns.intersection(['postal_code','raw_visitor_counts','raw_visit_counts'])]
df4 = df4.loc[:,df4.columns.intersection(['postal_code','raw_visitor_counts','raw_visit_counts'])]

df1 = df1.append(df2)
df1 = df1.append(df3)
df1 = df1.append(df4)

df1 = df1.groupby('postal_code')['raw_visitor_counts','raw_visit_counts'].sum()
df1 = df1.sort_values('postal_code')
df1 = df1.reset_index()

df1.to_csv(r'C:\Users\Tyler\Desktop\Projects\LA-RMSD COVID Challenge\Working files\Python export\Visitor Traffic by Zip Code.csv')
