

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
tx_data = pd.read_csv("data/csv/consumption/state_data/tx_data.csv")
# print(tx_data)
tx_msn = []
tx_year = []
tx_value = []

for i in range(len(tx_data["MSN"])):
    for j in range(len(te_msncodes)):
        if tx_data["MSN"][i] == te_msncodes[j]:
            tx_msn.append(tx_data["MSN"][i])
            tx_year.append(tx_data["Year"][i])
            tx_value.append(tx_data["Data"][i])
        else:
            pass

tx_te = OrderedDict()
tx_te["MSN"] = tx_msn
tx_te["Year"] = tx_year
tx_te["Data"] = tx_value
tx_te_data = pd.DataFrame(tx_te)

tx_te_data.to_csv("data/csv/consumption/sector/tx/tx_te_data.csv",
                  index=False, index_label=False, sep=',')
# print(tx_te_data)

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


for i in range(len(tx_te_data["MSN"])):
    if tx_te_data["MSN"][i] == "TEACB":
        teacb["Year"].append(tx_te_data["Year"][i])
        teacb["Data"].append(tx_te_data["Data"][i])
    elif tx_te_data["MSN"][i] == "TECCB":
        teccb["Year"].append(tx_te_data["Year"][i])
        teccb["Data"].append(tx_te_data["Data"][i])
    elif tx_te_data["MSN"][i] == "TEEIB":
        teeib["Year"].append(tx_te_data["Year"][i])
        teeib["Data"].append(tx_te_data["Data"][i])
    elif tx_te_data["MSN"][i] == "TEICB":
        teicb["Year"].append(tx_te_data["Year"][i])
        teicb["Data"].append(tx_te_data["Data"][i])
    elif tx_te_data["MSN"][i] == "TERCB":
        tercb["Year"].append(tx_te_data["Year"][i])
        tercb["Data"].append(tx_te_data["Data"][i])
    else:
        pass

teacb_data = pd.DataFrame(teacb)
teacb_data.to_csv("data/csv/consumption/sector/tx/te/teacb.csv",
                  index=False, index_label=False, sep=',')
teccb_data = pd.DataFrame(teccb)
teccb_data.to_csv("data/csv/consumption/sector/tx/te/teccb.csv",
                  index=False, index_label=False, sep=',')
teeib_data = pd.DataFrame(teeib)
teeib_data.to_csv("data/csv/consumption/sector/tx/te/teeib.csv",
                  index=False, index_label=False, sep=',')
teicb_data = pd.DataFrame(teicb)
teicb_data.to_csv("data/csv/consumption/sector/tx/te/teicb.csv",
                  index=False, index_label=False, sep=',')
tercb_data = pd.DataFrame(tercb)
tercb_data.to_csv("data/csv/consumption/sector/tx/te/tercb.csv",
                  index=False, index_label=False, sep=',')
# print(teacb_data)
# print(teccb_data)
# print(teeib_data)
# print(teicb_data)
# print(tercb_data)









