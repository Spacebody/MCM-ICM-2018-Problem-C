#! usr/bin/python3

import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict, defaultdict
import matplotlib as mpl
import matplotlib.pyplot as plt
# import seaborn as sns
from scipy import stats, integrate

# sns.set() # switch to seaborn default
# sns.set_style("whitegrid")

#load sector msncodes
tn_msncodes = pd.read_csv("data/csv/consumption/sector/tn_sector.csv")["MSN"]
#load state data
nm_data = pd.read_csv("data/csv/consumption/state_data/nm_data.csv")

nm_msn = []
nm_year = []
nm_value = []

for i in range(len(nm_data["MSN"])):
    for j in range(len(tn_msncodes)):
        if nm_data["MSN"][i] == tn_msncodes[j]:
            nm_msn.append(nm_data["MSN"][i])
            nm_year.append(nm_data["Year"][i])
            nm_value.append(nm_data["Data"][i])
        else:
            pass

nm_tn = OrderedDict()
nm_tn["MSN"] = nm_msn
nm_tn["Year"] = nm_year
nm_tn["Data"] = nm_value
nm_tn_data = pd.DataFrame(nm_tn)

nm_tn_data.to_csv("data/csv/consumption/sector/nm/nm_tn_data.csv",
                  index=False, index_label=False, sep=',')
# print(nm_tn_data)

sectors = ["TNACB", "TNCCB", "TNICB", "TNRCB"]
tnacb = OrderedDict()
tnacb["Year"] = []
tnacb["Data"] = []
tnccb = OrderedDict()
tnccb["Year"] = []
tnccb["Data"] = []
tnicb = OrderedDict()
tnicb["Year"] = []
tnicb["Data"] = []
tnrcb = OrderedDict()
tnrcb["Year"] = []
tnrcb["Data"] = []


for i in range(len(nm_tn_data["MSN"])):
    if nm_tn_data["MSN"][i] == "TNACB":
        tnacb["Year"].append(nm_tn_data["Year"][i])
        tnacb["Data"].append(nm_tn_data["Data"][i])
    elif nm_tn_data["MSN"][i] == "TNCCB":
        tnccb["Year"].append(nm_tn_data["Year"][i])
        tnccb["Data"].append(nm_tn_data["Data"][i])
    elif nm_tn_data["MSN"][i] == "TNICB":
        tnicb["Year"].append(nm_tn_data["Year"][i])
        tnicb["Data"].append(nm_tn_data["Data"][i])
    elif nm_tn_data["MSN"][i] == "TNRCB":
        tnrcb["Year"].append(nm_tn_data["Year"][i])
        tnrcb["Data"].append(nm_tn_data["Data"][i])
    else:
        pass

tnacb_data = pd.DataFrame(tnacb)
tnacb_data.to_csv("data/csv/consumption/sector/nm/tn/tnacb.csv",
                  index=False, index_label=False, sep=',')
tnccb_data = pd.DataFrame(tnccb)
tnccb_data.to_csv("data/csv/consumption/sector/nm/tn/tnccb.csv",
                  index=False, index_label=False, sep=',')
tnicb_data = pd.DataFrame(tnicb)
tnicb_data.to_csv("data/csv/consumption/sector/nm/tn/tnicb.csv",
                  index=False, index_label=False, sep=',')
tnrcb_data = pd.DataFrame(tnrcb)
tnrcb_data.to_csv("data/csv/consumption/sector/nm/tn/tnrcb.csv",
                  index=False, index_label=False, sep=',')
# print(tnacb_data)
# print(tnccb_data)
# print(tnicb_data)
# print(tnrcb_data)
