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

#load state data
az_data = pd.read_csv("data/csv/state_data/az_data.csv", engine='c', low_memory=True)
ca_data = pd.read_csv("data/csv/state_data/ca_data.csv", engine='c', low_memory=True)
nm_data = pd.read_csv("data/csv/state_data/nm_data.csv", engine='c', low_memory=True)
tx_data = pd.read_csv("data/csv/state_data/tx_data.csv", engine='c', low_memory=True)

# az
az_clprb = OrderedDict()
az_clprb["Year"] = []
az_clprb["Data"] = []
az_hytcb = OrderedDict()
az_hytcb["Year"] = []
az_hytcb["Data"] = []
az_paprb = OrderedDict()
az_paprb["Year"] = []
az_paprb["Data"] = []
az_ngmpb = OrderedDict()
az_ngmpb["Year"] = []
az_ngmpb["Data"] = []
az_reprb = OrderedDict()
az_reprb["Year"] = []
az_reprb["Data"] = []
az_teprb = OrderedDict()
az_teprb["Year"] = []
az_teprb["Data"] = []

for i in range(len(az_data["MSN"])):
    if az_data["MSN"][i] == "CLPRB":
        az_clprb["Year"].append(az_data["Year"][i])
        az_clprb["Data"].append(az_data["Data"][i])
    elif az_data["MSN"][i] == "HYTCB":
        az_hytcb["Year"].append(az_data["Year"][i])
        az_hytcb["Data"].append(az_data["Data"][i])
    elif az_data["MSN"][i] == "PAPRB":
        az_paprb["Year"].append(az_data["Year"][i])
        az_paprb["Data"].append(az_data["Data"][i])
    elif az_data["MSN"][i] == "NGMPB":
        az_ngmpb["Year"].append(az_data["Year"][i])
        az_ngmpb["Data"].append(az_data["Data"][i])
    elif az_data["MSN"][i] == "REPRB":
        az_reprb["Year"].append(az_data["Year"][i])
        az_reprb["Data"].append(az_data["Data"][i])
    elif az_data["MSN"][i] == "TEPRB":
        az_teprb["Year"].append(az_data["Year"][i])
        az_teprb["Data"].append(az_data["Data"][i])
    else:
        pass


# print(az_teprb)
# ca
ca_clprb = OrderedDict()
ca_clprb["Year"] = []
ca_clprb["Data"] = []
ca_hytcb = OrderedDict()
ca_hytcb["Year"] = []
ca_hytcb["Data"] = []
ca_paprb = OrderedDict()
ca_paprb["Year"] = []
ca_paprb["Data"] = []
ca_ngmpb = OrderedDict()
ca_ngmpb["Year"] = []
ca_ngmpb["Data"] = []
ca_reprb = OrderedDict()
ca_reprb["Year"] = []
ca_reprb["Data"] = []
ca_teprb = OrderedDict()
ca_teprb["Year"] = []
ca_teprb["Data"] = []

for i in range(len(ca_data["MSN"])):
    if ca_data["MSN"][i] == "CLPRB":
        ca_clprb["Year"].append(ca_data["Year"][i])
        ca_clprb["Data"].append(ca_data["Data"][i])
    elif ca_data["MSN"][i] == "HYTCB":
        ca_hytcb["Year"].append(ca_data["Year"][i])
        ca_hytcb["Data"].append(ca_data["Data"][i])
    elif ca_data["MSN"][i] == "PAPRB":
        ca_paprb["Year"].append(ca_data["Year"][i])
        ca_paprb["Data"].append(ca_data["Data"][i])
    elif ca_data["MSN"][i] == "NGMPB":
        ca_ngmpb["Year"].append(ca_data["Year"][i])
        ca_ngmpb["Data"].append(ca_data["Data"][i])
    elif ca_data["MSN"][i] == "REPRB":
        ca_reprb["Year"].append(ca_data["Year"][i])
        ca_reprb["Data"].append(ca_data["Data"][i])
    elif ca_data["MSN"][i] == "TEPRB":
        ca_teprb["Year"].append(ca_data["Year"][i])
        ca_teprb["Data"].append(ca_data["Data"][i])
    else:
        pass

# nm
nm_clprb = OrderedDict()
nm_clprb["Year"] = []
nm_clprb["Data"] = []
nm_hytcb = OrderedDict()
nm_hytcb["Year"] = []
nm_hytcb["Data"] = []
nm_paprb = OrderedDict()
nm_paprb["Year"] = []
nm_paprb["Data"] = []
nm_ngmpb = OrderedDict()
nm_ngmpb["Year"] = []
nm_ngmpb["Data"] = []
nm_reprb = OrderedDict()
nm_reprb["Year"] = []
nm_reprb["Data"] = []
nm_teprb = OrderedDict()
nm_teprb["Year"] = []
nm_teprb["Data"] = []

for i in range(len(nm_data["MSN"])):
    if nm_data["MSN"][i] == "CLPRB":
        nm_clprb["Year"].append(nm_data["Year"][i])
        nm_clprb["Data"].append(nm_data["Data"][i])
    elif nm_data["MSN"][i] == "HYTCB":
        nm_hytcb["Year"].append(nm_data["Year"][i])
        nm_hytcb["Data"].append(nm_data["Data"][i])
    elif nm_data["MSN"][i] == "PAPRB":
        nm_paprb["Year"].append(nm_data["Year"][i])
        nm_paprb["Data"].append(nm_data["Data"][i])
    elif nm_data["MSN"][i] == "NGMPB":
        nm_ngmpb["Year"].append(nm_data["Year"][i])
        nm_ngmpb["Data"].append(nm_data["Data"][i])
    elif nm_data["MSN"][i] == "REPRB":
        nm_reprb["Year"].append(nm_data["Year"][i])
        nm_reprb["Data"].append(nm_data["Data"][i])
    elif nm_data["MSN"][i] == "TEPRB":
        nm_teprb["Year"].append(nm_data["Year"][i])
        nm_teprb["Data"].append(nm_data["Data"][i])
    else:
        pass

# tx
tx_clprb = OrderedDict()
tx_clprb["Year"] = []
tx_clprb["Data"] = []
tx_hytcb = OrderedDict()
tx_hytcb["Year"] = []
tx_hytcb["Data"] = []
tx_paprb = OrderedDict()
tx_paprb["Year"] = []
tx_paprb["Data"] = []
tx_ngmpb = OrderedDict()
tx_ngmpb["Year"] = []
tx_ngmpb["Data"] = []
tx_reprb = OrderedDict()
tx_reprb["Year"] = []
tx_reprb["Data"] = []
tx_teprb = OrderedDict()
tx_teprb["Year"] = []
tx_teprb["Data"] = []

for i in range(len(tx_data["MSN"])):
    if tx_data["MSN"][i] == "CLPRB":
        tx_clprb["Year"].append(tx_data["Year"][i])
        tx_clprb["Data"].append(tx_data["Data"][i])
    elif tx_data["MSN"][i] == "HYTCB":
        tx_hytcb["Year"].append(tx_data["Year"][i])
        tx_hytcb["Data"].append(tx_data["Data"][i])
    elif tx_data["MSN"][i] == "PAPRB":
        tx_paprb["Year"].append(tx_data["Year"][i])
        tx_paprb["Data"].append(tx_data["Data"][i])
    elif tx_data["MSN"][i] == "NGMPB":
        tx_ngmpb["Year"].append(tx_data["Year"][i])
        tx_ngmpb["Data"].append(tx_data["Data"][i])
    elif tx_data["MSN"][i] == "REPRB":
        tx_reprb["Year"].append(tx_data["Year"][i])
        tx_reprb["Data"].append(tx_data["Data"][i])
    elif tx_data["MSN"][i] == "TEPRB":
        tx_teprb["Year"].append(tx_data["Year"][i])
        tx_teprb["Data"].append(tx_data["Data"][i])
    else:
        pass
