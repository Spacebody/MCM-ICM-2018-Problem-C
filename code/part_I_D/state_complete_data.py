import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict, defaultdict
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

complete = pd.read_csv("data/csv/original/complete.csv", engine='c', low_memory=True)

az_complete = OrderedDict()
ca_complete = OrderedDict()
nm_complete = OrderedDict()
tx_complete = OrderedDict()

az_msn = []
az_year = []
az_data = []

ca_msn = []
ca_year = []
ca_data = []

nm_msn = []
nm_year = []
nm_data = []

tx_msn = []
tx_year = []
tx_data = []

for i in range(len(complete["MSN"])):
    if complete["StateCode"][i] == "AZ":
        az_msn.append(complete["MSN"][i])
        az_year.append(complete["Year"][i])
        az_data.append(complete["Data"][i])
    elif complete["StateCode"][i] == "CA":
        ca_msn.append(complete["MSN"][i])
        ca_year.append(complete["Year"][i])
        ca_data.append(complete["Data"][i])
    elif complete["StateCode"][i] == "NM":
        nm_msn.append(complete["MSN"][i])
        nm_year.append(complete["Year"][i])
        nm_data.append(complete["Data"][i])
    elif complete["StateCode"][i] == "TX":
        tx_msn.append(complete["MSN"][i])
        tx_year.append(complete["Year"][i])
        tx_data.append(complete["Data"][i])
    else:
        pass

az_complete["MSN"] = az_msn
az_complete["Year"] = az_year
az_complete["Data"] = az_data
az_complete_data = pd.DataFrame(az_complete)
az_complete_data.to_csv("data/csv/state_data/az_complete.csv", index=False, index_label=False, sep=',')

ca_complete["MSN"] = ca_msn
ca_complete["Year"] = ca_year
ca_complete["Data"] = ca_data
ca_complete_data = pd.DataFrame(ca_complete)
ca_complete_data.to_csv("data/csv/state_data/ca_complete.csv", index=False, index_label=False, sep=',')

nm_complete["MSN"] = nm_msn
nm_complete["Year"] = nm_year
nm_complete["Data"] = nm_data
nm_complete_data = pd.DataFrame(nm_complete)
nm_complete_data.to_csv("data/csv/state_data/nm_complete.csv", index=False, index_label=False, sep=',')

tx_complete["MSN"] = tx_msn
tx_complete["Year"] = tx_year
tx_complete["Data"] = tx_data
tx_complete_data = pd.DataFrame(tx_complete)
tx_complete_data.to_csv("data/csv/state_data/tx_complete.csv", index=False, index_label=False, sep=',')

az_new = OrderedDict()
ca_new = OrderedDict()
nm_new = OrderedDict()
tx_new = OrderedDict()

az_new_msn = []
az_new_year = []
az_new_data = []

ca_new_msn = []
ca_new_year = []
ca_new_data = []

nm_new_msn = []
nm_new_year = []
nm_new_data = []

tx_new_msn = []
tx_new_year = []
tx_new_data = []

az_data = pd.read_csv("data/csv/state_data/az_complete.csv", engine='c', low_memory=True)
ca_data = pd.read_csv("data/csv/state_data/ca_complete.csv", engine='c', low_memory=True)
nm_data = pd.read_csv("data/csv/state_data/nm_complete.csv", engine='c', low_memory=True)
tx_data = pd.read_csv("data/csv/state_data/tx_complete.csv", engine='c', low_memory=True)

for i in range(len(az_data["MSN"])):
    if az_data["Year"][i] > 2009:
        az_new_msn.append(az_data["MSN"][i])
        az_new_year.append(az_data["Year"][i])
        az_new_data.append(az_data["Data"][i])
    else:
        pass
az_new["MSN"] = az_new_msn
az_new["Year"] = az_new_year
az_new["Data"] = az_new_data
az_new = pd.DataFrame(az_new)
az_new.to_csv("data/csv/state_data/az_new_data.csv", index=False, index_label=False, sep=',')



for i in range(len(ca_data["MSN"])):
    if ca_data["Year"][i] > 2009:
        ca_new_msn.append(ca_data["MSN"][i])
        ca_new_year.append(ca_data["Year"][i])
        ca_new_data.append(ca_data["Data"][i])
    else:
        pass

ca_new["MSN"] = ca_new_msn
ca_new["Year"] = ca_new_year
ca_new["Data"] = ca_new_data
ca_new = pd.DataFrame(ca_new)
ca_new.to_csv("data/csv/state_data/ca_new_data.csv", index=False, index_label=False, sep=',')


for i in range(len(nm_data["MSN"])):
    if nm_data["Year"][i] > 2009:
        nm_new_msn.append(nm_data["MSN"][i])
        
        nm_new_year.append(nm_data["Year"][i])

        nm_new_data.append(nm_data["Data"][i])
    else:
        pass

nm_new["MSN"] = nm_new_msn
nm_new["Year"] = nm_new_year
nm_new["Data"] = nm_new_data
nm_new = pd.DataFrame(nm_new)
nm_new.to_csv("data/csv/state_data/nm_new_data.csv", index=False, index_label=False, sep=',')

for i in range(len(tx_data["MSN"])):
    if tx_data["Year"][i] > 2009:
        tx_new_msn.append(tx_data["MSN"][i])
        tx_new_year.append(tx_data["Year"][i])
        tx_new_data.append(tx_data["Data"][i])
    else:
        pass

tx_new["MSN"] = tx_new_msn
tx_new["Year"] = tx_new_year
tx_new["Data"] = tx_new_data
tx_new = pd.DataFrame(tx_new)
tx_new.to_csv("data/csv/state_data/tx_new_data.csv", index=False, index_label=False, sep=',')
