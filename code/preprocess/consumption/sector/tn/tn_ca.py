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
tn_msncodes = pd.read_csv("data/csv/consumption/sector/tn_sector.csv", engine='c', low_memory=True)["MSN"]
#load state data
ca_data = pd.read_csv("data/csv/state_data/ca_data.csv", engine='c', low_memory=True)

ca_msn = []
ca_year = []
ca_value = []

for i in range(len(ca_data["MSN"])):
    for j in range(len(tn_msncodes)):
        if ca_data["MSN"][i] == tn_msncodes[j]:
            ca_msn.append(ca_data["MSN"][i])
            ca_year.append(ca_data["Year"][i])
            ca_value.append(ca_data["Data"][i])
        else:
            pass

ca_tn = OrderedDict()
ca_tn["MSN"] = ca_msn
ca_tn["Year"] = ca_year
ca_tn["Data"] = ca_value
ca_tn_data = pd.DataFrame(ca_tn)

ca_tn_data.to_csv("data/csv/consumption/sector/ca/ca_tn_data.csv",
                  index=False, index_label=False, sep=',')
# print(ca_tn_data)

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


for i in range(len(ca_tn_data["MSN"])):
    if ca_tn_data["MSN"][i] == "TNACB":
        tnacb["Year"].append(ca_tn_data["Year"][i])
        tnacb["Data"].append(ca_tn_data["Data"][i])
    elif ca_tn_data["MSN"][i] == "TNCCB":
        tnccb["Year"].append(ca_tn_data["Year"][i])
        tnccb["Data"].append(ca_tn_data["Data"][i])
    elif ca_tn_data["MSN"][i] == "TNICB":
        tnicb["Year"].append(ca_tn_data["Year"][i])
        tnicb["Data"].append(ca_tn_data["Data"][i])
    elif ca_tn_data["MSN"][i] == "TNRCB":
        tnrcb["Year"].append(ca_tn_data["Year"][i])
        tnrcb["Data"].append(ca_tn_data["Data"][i])
    else:
        pass

tnacb_data = pd.DataFrame(tnacb)
tnacb_data.to_csv("data/csv/consumption/sector/ca/tn/tnacb.csv",
                  index=False, index_label=False, sep=',')
tnccb_data = pd.DataFrame(tnccb)
tnccb_data.to_csv("data/csv/consumption/sector/ca/tn/tnccb.csv",
                  index=False, index_label=False, sep=',')
tnicb_data = pd.DataFrame(tnicb)
tnicb_data.to_csv("data/csv/consumption/sector/ca/tn/tnicb.csv",
                  index=False, index_label=False, sep=',')
tnrcb_data = pd.DataFrame(tnrcb)
tnrcb_data.to_csv("data/csv/consumption/sector/ca/tn/tnrcb.csv",
                  index=False, index_label=False, sep=',')
# print(tnacb_data)
# print(tnccb_data)
# print(tnicb_data)
# print(tnrcb_data)
