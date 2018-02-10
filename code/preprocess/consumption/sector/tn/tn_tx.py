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
tx_data = pd.read_csv("data/csv/state_data/tx_data.csv", engine='c', low_memory=True)

tx_msn = []
tx_year = []
tx_value = []

for i in range(len(tx_data["MSN"])):
    for j in range(len(tn_msncodes)):
        if tx_data["MSN"][i] == tn_msncodes[j]:
            tx_msn.append(tx_data["MSN"][i])
            tx_year.append(tx_data["Year"][i])
            tx_value.append(tx_data["Data"][i])
        else:
            pass

tx_tn = OrderedDict()
tx_tn["MSN"] = tx_msn
tx_tn["Year"] = tx_year
tx_tn["Data"] = tx_value
tx_tn_data = pd.DataFrame(tx_tn)

tx_tn_data.to_csv("data/csv/consumption/sector/tx/tx_tn_data.csv",
                  index=False, index_label=False, sep=',')
# print(tx_tn_data)

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


for i in range(len(tx_tn_data["MSN"])):
    if tx_tn_data["MSN"][i] == "TNACB":
        tnacb["Year"].append(tx_tn_data["Year"][i])
        tnacb["Data"].append(tx_tn_data["Data"][i])
    elif tx_tn_data["MSN"][i] == "TNCCB":
        tnccb["Year"].append(tx_tn_data["Year"][i])
        tnccb["Data"].append(tx_tn_data["Data"][i])
    elif tx_tn_data["MSN"][i] == "TNICB":
        tnicb["Year"].append(tx_tn_data["Year"][i])
        tnicb["Data"].append(tx_tn_data["Data"][i])
    elif tx_tn_data["MSN"][i] == "TNRCB":
        tnrcb["Year"].append(tx_tn_data["Year"][i])
        tnrcb["Data"].append(tx_tn_data["Data"][i])
    else:
        pass

tnacb_data = pd.DataFrame(tnacb)
tnacb_data.to_csv("data/csv/consumption/sector/tx/tn/tnacb.csv",
                  index=False, index_label=False, sep=',')
tnccb_data = pd.DataFrame(tnccb)
tnccb_data.to_csv("data/csv/consumption/sector/tx/tn/tnccb.csv",
                  index=False, index_label=False, sep=',')
tnicb_data = pd.DataFrame(tnicb)
tnicb_data.to_csv("data/csv/consumption/sector/tx/tn/tnicb.csv",
                  index=False, index_label=False, sep=',')
tnrcb_data = pd.DataFrame(tnrcb)
tnrcb_data.to_csv("data/csv/consumption/sector/tx/tn/tnrcb.csv",
                  index=False, index_label=False, sep=',')
# print(tnacb_data)
# print(tnccb_data)
# print(tnicb_data)
# print(tnrcb_data)
