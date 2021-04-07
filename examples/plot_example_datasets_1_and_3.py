"""
Example datasets 1 and 3
========================

This example rely on fake datasets 1 and 3.
"""

######################################################
# Load dataset 1
#
# Load fake dataset 1
from toy_pkg.datasets import fetch_fake_dataset_1
data1 = fetch_fake_dataset_1()
print(data1.description)

######################################################
# Load dataset 3
#
# Load fake dataset 3
from toy_pkg.datasets import fetch_fake_dataset_3
data3 = fetch_fake_dataset_3()
print(data3.description)

######################################################
# Perform some computation
#
# computation on both datasets
import pandas as pd
from toy_pkg.lazy_calculator import lazy_add

tot = 0
df = pd.concat([pd.read_csv(data1.data),
                pd.read_csv(data3.data)])
for i,row in df.iterrows():
    tot += lazy_add(row['first term'],
                    row['second term'],
                    0.1)
print(tot)
