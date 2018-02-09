#! usr/bin/python3

import pandas as pd 
import re 
import numpy as np

seseds = pd.read_csv(b'data/csv/seseds.csv', skiprows=None, engine='c', low_memory=True)
msncodes = pd.read_csv(b'data/csv/msncodes.csv', skiprows=None, engine='c', low_memory=True)
# print(seseds) 
# print(msncodes)
# print(type(msncodes)) # dict
# for key in msncodes.keys():
#     print(msncodes[key])

msn = []
description = []
unit = []
for i in range(len(msncodes["Description"])):
    if not re.search("price", msncodes["Description"][i]) and not re.search("expanditures", msncodes["Description"][i])\
            and not re.search("production", msncodes["Description"][i]):
        msn.append(msncodes["MSN"][i])
        description.append(msncodes["Description"][i])
        unit.append(msncodes["Unit"][i])
data_frame = pd.DataFrame({"MSN": msn, "Description": description, "Unit": unit})
data_frame.to_csv("data/test.csv",index=False,index_label=False,sep=',')





