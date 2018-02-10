#! usr/bin/python3

import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict

parent_path = os.path.realpath(os.pardir)
if sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
    seseds_path = os.path.join(
        parent_path, 'MCM-ICM-2018-Problem-C\\data\\csv\\seseds.csv')
    msncodes_path = os.path.join(
        parent_path, 'MCM-ICM-2018-Problem-C\\data\\csv\\msncodes.csv')
elif sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
    seseds_path = os.path.join(
        parent_path, 'MCM-ICM-2018-Problem-C/data/csv/seseds.csv')
    msncodes_path = os.path.join(
        parent_path, 'MCM-ICM-2018-Problem-C/data/csv/msncodes.csv')
else:
    pass
seseds = pd.read_csv(seseds_path, skiprows=None, engine='c', low_memory=True)
msncodes = pd.read_csv(msncodes_path, skiprows=None,
                       engine='c', low_memory=True)

# print(seseds)
# print(msncodes)
# print(type(msncodes)) # dict
# for key in msncodes.keys():
#     print(msncodes[key])

msn = []
description = []
unit = []

te_msn = []
te_description = []
te_unit = []

tn_msn = []
tn_description = []
tn_unit = []

for i in range(len(msncodes["Description"])):
    if not re.search("price", msncodes["Description"][i]) and not re.search("expenditures", msncodes["Description"][i]) and \
                not re.search("production", msncodes["Description"][i]) and not re.search("imported", msncodes["Description"][i]) and \
                not re.search("imports", msncodes["Description"][i]) and not re.search("exported", msncodes["Description"][i]) and \
                not re.search("exported", msncodes["Description"][i]) and not re.search("Factor", msncodes["Description"][i]) and \
            (re.search("Total", msncodes["Description"][i]) or re.search("total", msncodes["Description"][i])) and \
        re.search("sector", msncodes["Description"][i]):
        msn.append(msncodes["MSN"][i])
        description.append(msncodes["Description"][i])
        unit.append(msncodes["Unit"][i])

comp_data = OrderedDict()
item_dict = OrderedDict()
item_dict["MSN"] = msn
item_dict["Description"] = description
item_dict["Unit"] = unit
comp_data = pd.DataFrame(item_dict)

for i in range(len(comp_data["MSN"])):
    if re.search("TE", comp_data["MSN"][i]):
            te_msn.append(comp_data["MSN"][i])
            te_description.append(comp_data["Description"][i])
            te_unit.append(comp_data["Unit"][i])
    elif re.search("TN", comp_data["MSN"][i]):
        tn_msn.append(comp_data["MSN"][i])
        tn_description.append(comp_data["Description"][i])
        tn_unit.append(comp_data["Unit"][i])
    else:
        pass
te_data = OrderedDict()
item_dict = OrderedDict()
item_dict["MSN"] = te_msn
item_dict["Description"] = te_description
item_dict["Unit"] = te_unit
te_data = pd.DataFrame(item_dict)

tn_data = OrderedDict()
item_dict = OrderedDict()
item_dict["MSN"] = tn_msn
item_dict["Description"] = tn_description
item_dict["Unit"] = tn_unit
tn_data = pd.DataFrame(item_dict)


# data_frame.to_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM2018\\data\\test.csv",index=False,index_label=False,sep=',')
comp_data.to_csv("data/csv/total_sector.csv", index=False, index_label=False, sep=',')
print(comp_data)
print(tn_data)
print(te_data)
tn_data.to_csv("data/csv/tn_sector.csv", index=False, index_label=False, sep=',')
te_data.to_csv("data/csv/te_sector.csv", index=False, index_label=False, sep=',')
