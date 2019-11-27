import csv
import pandas as pd

pandas_dataset = pd.read_csv('../dataset/USvideos_modified.csv')

mean = pandas_dataset["views"].mean()

for i in range(0, 4546):
    if pandas_dataset.loc[i].at['views'] >= mean:
        pandas_dataset.at[i, 'is_famous'] = 1
    else:
        pandas_dataset.at[i, 'is_famous'] = 0

pandas_dataset.to_csv('../dataset/USvideos_treated.csv')