"""
Example dataset 1
=================

This example rely on fake dataset 1 only.
"""

######################################################
# Load dataset
#
# Load fake dataset 1
from toy_pkg.datasets import fetch_fake_dataset_1
data = fetch_fake_dataset_1()
print(data.description)

######################################################
# Perform some computation
import pandas as pd
from toy_pkg.lazy_calculator import lazy_add

tot = 0
df = pd.read_csv(data.data)
for i,row in df.iterrows():
    tot += lazy_add(row['first term'],
                    row['second term'],
                    0.1)
print(tot)
