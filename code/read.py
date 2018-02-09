#! usr/bin/python3

import pandas as pd 
import re 
import numpy as np
import os
import sys

parent_path = os.path.realpath(os.pardir)
if sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
    seseds_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C\\data\\csv\\seseds.csv')
    msncodes_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C\\data\\csv\\msncodes.csv')
elif sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
    seseds_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C/data/csv/seseds.csv')
    msncodes_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C/data/csv/msncodes.csv')
else:
    pass
seseds = pd.read_csv(seseds_path, skiprows=None, engine='c', low_memory=True)
msncodes = pd.read_csv(msncodes_path, skiprows=None, engine='c', low_memory=True)
# print(seseds) 
# print(msncodes)
# print(type(msncodes)) # dict
# for key in msncodes.keys():
#     print(msncodes[key])

# msn = []
# description = []
# unit = []
# for i in range(len(msncodes["Description"])):
#     if not re.search("price", msncodes["Description"][i]) and not re.search("expanditures", msncodes["Description"][i])\
#             and not re.search("production", msncodes["Description"][i]):
#         msn.append(msncodes["MSN"][i])
#         description.append(msncodes["Description"][i])
#         unit.append(msncodes["Unit"][i])
# data_frame = pd.DataFrame({"MSN": msn, "Description": description, "Unit": unit})
# data_frame.to_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM2018\\data\\test.csv",index=False,index_label=False,sep=',')





