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
te_msncodes = pd.read_csv("data/csv/consumption/sector/te_sector.csv")["MSN"]
#load state data
nm_data = pd.read_csv("data/csv/consumption/state_data/nm_data.csv")

nm_msn = []
nm_year = []
nm_value = []

for i in range(len(nm_data["MSN"])):
    for j in range(len(te_msncodes)):
        if nm_data["MSN"][i] == te_msncodes[j]:
            nm_msn.append(nm_data["MSN"][i])
            nm_year.append(nm_data["Year"][i])
            nm_value.append(nm_data["Data"][i])
        else:
            pass

nm_te = OrderedDict()
nm_te["MSN"] = nm_msn
nm_te["Year"] = nm_year
nm_te["Data"] = nm_value
nm_te_data = pd.DataFrame(nm_te)

nm_te_data.to_csv("data/csv/consumption/sector/nm/nm_te_data.csv",
                  index=False, index_label=False, sep=',')
# print(nm_te_data)

sectors = ["TEACB", "TECCB", "TEEIB", "TEICB", "TERCB"]
teacb = OrderedDict()
teacb["Year"] = []
teacb["Data"] = []
teccb = OrderedDict()
teccb["Year"] = []
teccb["Data"] = []
teeib = OrderedDict()
teeib["Year"] = []
teeib["Data"] = []
teicb = OrderedDict()
teicb["Year"] = []
teicb["Data"] = []
tercb = OrderedDict()
tercb["Year"] = []
tercb["Data"] = []


for i in range(len(nm_te_data["MSN"])):
    if nm_te_data["MSN"][i] == "TEACB":
        teacb["Year"].append(nm_te_data["Year"][i])
        teacb["Data"].append(nm_te_data["Data"][i])
    elif nm_te_data["MSN"][i] == "TECCB":
        teccb["Year"].append(nm_te_data["Year"][i])
        teccb["Data"].append(nm_te_data["Data"][i])
    elif nm_te_data["MSN"][i] == "TEEIB":
        teeib["Year"].append(nm_te_data["Year"][i])
        teeib["Data"].append(nm_te_data["Data"][i])
    elif nm_te_data["MSN"][i] == "TEICB":
        teicb["Year"].append(nm_te_data["Year"][i])
        teicb["Data"].append(nm_te_data["Data"][i])
    elif nm_te_data["MSN"][i] == "TERCB":
        tercb["Year"].append(nm_te_data["Year"][i])
        tercb["Data"].append(nm_te_data["Data"][i])
    else:
        pass

teacb_data = pd.DataFrame(teacb)
teacb_data.to_csv("data/csv/consumption/sector/nm/te/teacb.csv",
                  index=False, index_label=False, sep=',')
teccb_data = pd.DataFrame(teccb)
teccb_data.to_csv("data/csv/consumption/sector/nm/te/teccb.csv",
                  index=False, index_label=False, sep=',')
teeib_data = pd.DataFrame(teeib)
teeib_data.to_csv("data/csv/consumption/sector/nm/te/teeib.csv",
                  index=False, index_label=False, sep=',')
teicb_data = pd.DataFrame(teicb)
teicb_data.to_csv("data/csv/consumption/sector/nm/te/teicb.csv",
                  index=False, index_label=False, sep=',')
tercb_data = pd.DataFrame(tercb)
tercb_data.to_csv("data/csv/consumption/sector/nm/te/tercb.csv",
                  index=False, index_label=False, sep=',')
# print(teacb_data)
# print(teccb_data)
# print(teeib_data)
# print(teicb_data)
# print(tercb_data)
