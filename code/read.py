#! usr/bin/python3

import pandas as pd 
import re 
import numpy as np

seseds = pd.read_csv('data/csv/seseds.csv', skiprows=None, engine='c', low_memory=True)
msncodes = pd.read_csv('data/csv/msncodes.csv', skiprows=None, engine='c', low_memory=True)
# print(seseds) 
# print(msncodes)
# print(type(msncodes)) # dict
# for key in msncodes.keys():
#     print(msncodes[key])

for i in range(len(msncodes["Description"])):
    if re.search("price", msncodes["Description"][i]) or re.search("expanditures", msncodes["Description"][i]) or re.search("production", msncodes["Description"][i]):
        msncodes["Description"].drop(labels=i, axis=0)
        # print(i)
print(msncodes["Description"])


