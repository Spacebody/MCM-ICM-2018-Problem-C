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
az_data = pd.read_csv("data/csv/consumption/state_data/az_data.csv")

az_msn = []
az_year = []
az_value = []

for i in range(len(az_data["MSN"])):
    for j in range(len(te_msncodes)):
        if az_data["MSN"][i] == te_msncodes[j]:
            az_msn.append(az_data["MSN"][i])
            az_year.append(az_data["Year"][i])
            az_value.append(az_data["Data"][i])
        else:
            pass

az_te = OrderedDict()
az_te["MSN"] = az_msn
az_te["Year"] = az_year
az_te["Data"] = az_value
az_te_data = pd.DataFrame(az_te)

az_te_data.to_csv("data/csv/consumption/sector/az/az_te_data.csv", index=False, index_label=False, sep=',')
# print(az_te_data)

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


for i in range(len(az_te_data["MSN"])):
    if az_te_data["MSN"][i] == "TEACB":
        teacb["Year"].append(az_te_data["Year"][i])
        teacb["Data"].append(az_te_data["Data"][i])
    elif az_te_data["MSN"][i] == "TECCB":
        teccb["Year"].append(az_te_data["Year"][i])
        teccb["Data"].append(az_te_data["Data"][i])
    elif az_te_data["MSN"][i] == "TEEIB":
        teeib["Year"].append(az_te_data["Year"][i])
        teeib["Data"].append(az_te_data["Data"][i])
    elif az_te_data["MSN"][i] == "TEICB":
        teicb["Year"].append(az_te_data["Year"][i])
        teicb["Data"].append(az_te_data["Data"][i])
    elif az_te_data["MSN"][i] == "TERCB":
        tercb["Year"].append(az_te_data["Year"][i])
        tercb["Data"].append(az_te_data["Data"][i])
    else:
        pass

teacb_data = pd.DataFrame(teacb)
teacb_data.to_csv("data/csv/consumption/sector/az/te/teacb.csv", 
             index=False, index_label=False, sep=',')
teccb_data = pd.DataFrame(teccb)
teccb_data.to_csv("data/csv/consumption/sector/az/te/teccb.csv",
             index=False, index_label=False, sep=',')
teeib_data = pd.DataFrame(teeib)
teeib_data.to_csv("data/csv/consumption/sector/az/te/teeib.csv",
             index=False, index_label=False, sep=',')
teicb_data = pd.DataFrame(teicb)
teicb_data.to_csv("data/csv/consumption/sector/az/te/teicb.csv",
             index=False, index_label=False, sep=',')
tercb_data = pd.DataFrame(tercb)
tercb_data.to_csv("data/csv/consumption/sector/az/te/tercb.csv",
             index=False, index_label=False, sep=',')
# print(teacb_data)
# print(teccb_data)
# print(teeib_data)
# print(teicb_data)
# print(tercb_data)







