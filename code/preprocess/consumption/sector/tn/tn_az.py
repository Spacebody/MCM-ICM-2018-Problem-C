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
az_data = pd.read_csv("data/csv/consumption/state_data/az_data.csv")

az_msn = []
az_year = []
az_value = []

for i in range(len(az_data["MSN"])):
    for j in range(len(tn_msncodes)):
        if az_data["MSN"][i] == tn_msncodes[j]:
            az_msn.append(az_data["MSN"][i])
            az_year.append(az_data["Year"][i])
            az_value.append(az_data["Data"][i])
        else:
            pass

az_tn = OrderedDict()
az_tn["MSN"] = az_msn
az_tn["Year"] = az_year
az_tn["Data"] = az_value
az_tn_data = pd.DataFrame(az_tn)

az_tn_data.to_csv("data/csv/consumption/sector/az/az_tn_data.csv",
                  index=False, index_label=False, sep=',')
# print(az_tn_data)

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


for i in range(len(az_tn_data["MSN"])):
    if az_tn_data["MSN"][i] == "TNACB":
        tnacb["Year"].append(az_tn_data["Year"][i])
        tnacb["Data"].append(az_tn_data["Data"][i])
    elif az_tn_data["MSN"][i] == "TNCCB":
        tnccb["Year"].append(az_tn_data["Year"][i])
        tnccb["Data"].append(az_tn_data["Data"][i])
    elif az_tn_data["MSN"][i] == "TNICB":
        tnicb["Year"].append(az_tn_data["Year"][i])
        tnicb["Data"].append(az_tn_data["Data"][i])
    elif az_tn_data["MSN"][i] == "TNRCB":
        tnrcb["Year"].append(az_tn_data["Year"][i])
        tnrcb["Data"].append(az_tn_data["Data"][i])
    else:
        pass

tnacb_data = pd.DataFrame(tnacb)
tnacb_data.to_csv("data/csv/consumption/sector/az/tn/tnacb.csv",
                  index=False, index_label=False, sep=',')
tnccb_data = pd.DataFrame(tnccb)
tnccb_data.to_csv("data/csv/consumption/sector/az/tn/tnccb.csv",
                  index=False, index_label=False, sep=',')
tnicb_data = pd.DataFrame(tnicb)
tnicb_data.to_csv("data/csv/consumption/sector/az/tn/tnicb.csv",
                  index=False, index_label=False, sep=',')
tnrcb_data = pd.DataFrame(tnrcb)
tnrcb_data.to_csv("data/csv/consumption/sector/az/tn/tnrcb.csv",
                  index=False, index_label=False, sep=',')
# print(tnacb_data)
# print(tnccb_data)
# print(tnicb_data)
# print(tnrcb_data)
