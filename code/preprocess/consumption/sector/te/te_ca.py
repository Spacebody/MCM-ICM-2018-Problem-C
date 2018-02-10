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
te_msncodes = pd.read_csv("data/csv/consumption/sector/te_sector.csv", engine='c', low_memory=True)["MSN"]
#load state data
ca_data = pd.read_csv("data/csv/state_data/ca_data.csv", engine='c', low_memory=True)

ca_msn = []
ca_year = []
ca_value = []

for i in range(len(ca_data["MSN"])):
    for j in range(len(te_msncodes)):
        if ca_data["MSN"][i] == te_msncodes[j]:
            ca_msn.append(ca_data["MSN"][i])
            ca_year.append(ca_data["Year"][i])
            ca_value.append(ca_data["Data"][i])
        else:
            pass

ca_te = OrderedDict()
ca_te["MSN"] = ca_msn
ca_te["Year"] = ca_year
ca_te["Data"] = ca_value
ca_te_data = pd.DataFrame(ca_te)

ca_te_data.to_csv("data/csv/consumption/sector/ca/ca_te_data.csv",
                  index=False, index_label=False, sep=',')
# print(ca_te_data)

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


for i in range(len(ca_te_data["MSN"])):
    if ca_te_data["MSN"][i] == "TEACB":
        teacb["Year"].append(ca_te_data["Year"][i])
        teacb["Data"].append(ca_te_data["Data"][i])
    elif ca_te_data["MSN"][i] == "TECCB":
        teccb["Year"].append(ca_te_data["Year"][i])
        teccb["Data"].append(ca_te_data["Data"][i])
    elif ca_te_data["MSN"][i] == "TEEIB":
        teeib["Year"].append(ca_te_data["Year"][i])
        teeib["Data"].append(ca_te_data["Data"][i])
    elif ca_te_data["MSN"][i] == "TEICB":
        teicb["Year"].append(ca_te_data["Year"][i])
        teicb["Data"].append(ca_te_data["Data"][i])
    elif ca_te_data["MSN"][i] == "TERCB":
        tercb["Year"].append(ca_te_data["Year"][i])
        tercb["Data"].append(ca_te_data["Data"][i])
    else:
        pass

teacb_data = pd.DataFrame(teacb)
teacb_data.to_csv("data/csv/consumption/sector/ca/te/teacb.csv",
                  index=False, index_label=False, sep=',')
teccb_data = pd.DataFrame(teccb)
teccb_data.to_csv("data/csv/consumption/sector/ca/te/teccb.csv",
                  index=False, index_label=False, sep=',')
teeib_data = pd.DataFrame(teeib)
teeib_data.to_csv("data/csv/consumption/sector/ca/te/teeib.csv",
                  index=False, index_label=False, sep=',')
teicb_data = pd.DataFrame(teicb)
teicb_data.to_csv("data/csv/consumption/sector/ca/te/teicb.csv",
                  index=False, index_label=False, sep=',')
tercb_data = pd.DataFrame(tercb)
tercb_data.to_csv("data/csv/consumption/sector/ca/te/tercb.csv",
                  index=False, index_label=False, sep=',')
# print(teacb_data)
# print(teccb_data)
# print(teeib_data)
# print(teicb_data)
# print(tercb_data)
