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
az_data = pd.read_csv("data/csv/state_data/az_data.csv",
                      engine='c', low_memory=True)
ca_data = pd.read_csv("data/csv/state_data/ca_data.csv",
                      engine='c', low_memory=True)
nm_data = pd.read_csv("data/csv/state_data/nm_data.csv",
                      engine='c', low_memory=True)
tx_data = pd.read_csv("data/csv/state_data/tx_data.csv",
                      engine='c', low_memory=True)

# az
az_tegds = OrderedDict()
az_tegds["Year"] = []
az_tegds["Data"] = []

for i in range(len(az_data["MSN"])):
    if az_data["MSN"][i] == "TEGDS":
        az_tegds["Year"].append(az_data["Year"][i])
        az_tegds["Data"].append(az_data["Data"][i])
    else:
        pass

# ca
ca_tegds = OrderedDict()
ca_tegds["Year"] = []
ca_tegds["Data"] = []

for i in range(len(ca_data["MSN"])):
    if ca_data["MSN"][i] == "TEGDS":
        ca_tegds["Year"].append(ca_data["Year"][i])
        ca_tegds["Data"].append(ca_data["Data"][i])
    else:
        pass


# nm
nm_tegds = OrderedDict()
nm_tegds["Year"] = []
nm_tegds["Data"] = []

for i in range(len(nm_data["MSN"])):
    if nm_data["MSN"][i] == "TEGDS":
        nm_tegds["Year"].append(nm_data["Year"][i])
        nm_tegds["Data"].append(nm_data["Data"][i])
    else:
        pass


# tx
tx_tegds = OrderedDict()
tx_tegds["Year"] = []
tx_tegds["Data"] = []

for i in range(len(tx_data["MSN"])):
    if tx_data["MSN"][i] == "TEGDS":
        tx_tegds["Year"].append(tx_data["Year"][i])
        tx_tegds["Data"].append(tx_data["Data"][i])
    else:
        pass
