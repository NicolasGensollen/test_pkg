"""
Example dataset 2
=================

This example rely on fake dataset 2 only.
"""

######################################################
# Load dataset
#
# Load fake dataset 2
from toy_pkg.datasets import fetch_fake_dataset_2
data = fetch_fake_dataset_2()
print(data.description)

######################################################
# Perform some computation
import pandas as pd
from toy_pkg.calculus import lazy_add

tot = 0
df = pd.concat(map(pd.read_csv, data.data))
for i,row in df.iterrows():
    tot += lazy_add(row['first term'],
                    row['second term'],
                    0.1)
print(tot)
