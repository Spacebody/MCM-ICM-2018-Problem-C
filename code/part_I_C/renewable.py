import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict, defaultdict
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats, integrate

# load msncodes
msncodes = pd.read_csv("data/csv/original/msncodes.csv")
# load state data 
az = pd.read_csv("data/csv/state_data/az_data.csv", engine='c', low_memory=True)
ca = pd.read_csv("data/csv/state_data/ca_data.csv", engine='c', low_memory=True)
nm = pd.read_csv("data/csv/state_data/nm_data.csv", engine='c', low_memory=True)
tx = pd.read_csv("data/csv/state_data/tx_data.csv", engine='c', low_memory=True)

# select msncodes of renewable energy
msn = []
description = []
unit = []
for i in range(len(msncodes["MSN"])):
    if re.search("[R|r]enewable", msncodes["Description"][i]):
        msn.append(msncodes["MSN"][i])
        description.append(msncodes["Description"][i])
        unit.append(msncodes["Unit"][i])

renewable = OrderedDict()
renewable["MSN"] = msn
renewable["Description"] = description
renewable["Unit"] = unit
renewable_data = pd.DataFrame(renewable)
renewable_data.to_csv("data/csv/renewable/renewable.csv", index=False, index_label=False, sep=',')

# select data of renewable energy

# az
az_msn = []
az_year = []
az_data = []
for i in range(len(az["MSN"])):
    if az["Year"][i] == 2009:
        if az["MSN"][i] == "REPRB":
            az_reprb = az["Data"][i]
            az_msn.append(az["MSN"][i])
            az_year.append(az["Year"][i])
            az_data.append(az["Data"][i])
        elif az["MSN"][i] == "RETCB":
            az_retcb = az["Data"][i]
            az_msn.append(az["MSN"][i])
            az_year.append(az["Year"][i])
            az_data.append(az["Data"][i])
        elif az["MSN"][i] == "ROPRB":
            az_roprb = az["Data"][i]
            az_msn.append(az["MSN"][i])
            az_year.append(az["Year"][i])
            az_data.append(az["Data"][i])
        elif az["MSN"][i] == "TPOPP":
            az_tpopp=az["Data"][i]
            az_msn.append(az["MSN"][i])
            az_year.append(az["Year"][i])
            az_data.append(az["Data"][i])
        elif az["MSN"][i] == "TETCB":
            az_tetcb = az["Data"][i]
            az_msn.append(az["MSN"][i])
            az_year.append(az["Year"][i])
            az_data.append(az["Data"][i])
        elif az["MSN"][i] == "TEPRB":
            az_teprb = az["Data"][i]
            az_msn.append(az["MSN"][i])
            az_year.append(az["Year"][i])
            az_data.append(az["Data"][i])
        else:
            pass
    else:
        pass

az_renewable = OrderedDict()
az_renewable["MSN"] = az_msn
az_renewable["Year"] = az_year
az_renewable["Data"] = az_data
az_renewable_data = pd.DataFrame(az_renewable)
az_renewable_data.to_csv("data/csv/renewable/az_renewable.csv", index=False, index_label=False, sep=',')

# ca
ca_msn = []
ca_year = []
ca_data = []
for i in range(len(ca["MSN"])):
    if ca["Year"][i] == 2009:
        if ca["MSN"][i] == "REPRB":
            ca_reprb = ca["Data"][i]
            ca_msn.append(ca["MSN"][i])
            ca_year.append(ca["Year"][i])
            ca_data.append(ca["Data"][i])
        elif ca["MSN"][i] == "RETCB":
            ca_retcb = ca["Data"][i]
            ca_msn.append(ca["MSN"][i])
            ca_year.append(ca["Year"][i])
            ca_data.append(ca["Data"][i])
        elif ca["MSN"][i] == "ROPRB":
            ca_roprb = ca["Data"][i]
            ca_msn.append(ca["MSN"][i])
            ca_year.append(ca["Year"][i])
            ca_data.append(ca["Data"][i])
        elif ca["MSN"][i] == "TPOPP":
            ca_tpopp = ca["Data"][i]
            ca_msn.append(ca["MSN"][i])
            ca_year.append(ca["Year"][i])
            ca_data.append(ca["Data"][i])
        elif ca["MSN"][i] == "TETCB":
            ca_tetcb = ca["Data"][i]
            ca_msn.append(ca["MSN"][i])
            ca_year.append(ca["Year"][i])
            ca_data.append(ca["Data"][i])
        elif ca["MSN"][i] == "TEPRB":
            ca_teprb = ca["Data"][i]
            ca_msn.append(ca["MSN"][i])
            ca_year.append(ca["Year"][i])
            ca_data.append(ca["Data"][i])
        else:
            pass
    else:
        pass
ca_renewable = OrderedDict()
ca_renewable["MSN"] = ca_msn
ca_renewable["Year"] = ca_year
ca_renewable["Data"] = ca_data
ca_renewable_data = pd.DataFrame(ca_renewable)
ca_renewable_data.to_csv("data/csv/renewable/ca_renewable.csv", index=False, index_label=False, sep=',')

# nm
nm_msn = []
nm_year = []
nm_data = []
for i in range(len(nm["MSN"])):
    if nm["Year"][i] == 2009:
        if nm["MSN"][i] == "REPRB":
            nm_reprb = nm["Data"][i]
            nm_msn.append(nm["MSN"][i])
            nm_year.append(nm["Year"][i])
            nm_data.append(nm["Data"][i])
        elif nm["MSN"][i] == "RETCB":
            nm_retcb = nm["Data"][i]
            nm_msn.append(nm["MSN"][i])
            nm_year.append(nm["Year"][i])
            nm_data.append(nm["Data"][i])
        elif nm["MSN"][i] == "ROPRB":
            nm_roprb = nm["Data"][i]
            nm_msn.append(nm["MSN"][i])
            nm_year.append(nm["Year"][i])
            nm_data.append(nm["Data"][i])
        elif nm["MSN"][i] == "TPOPP":
            nm_tpopp = nm["Data"][i]
            nm_msn.append(nm["MSN"][i])
            nm_year.append(nm["Year"][i])
            nm_data.append(nm["Data"][i])
        elif nm["MSN"][i] == "TETCB":
            nm_tetcb = nm["Data"][i]
            nm_msn.append(nm["MSN"][i])
            nm_year.append(nm["Year"][i])
            nm_data.append(nm["Data"][i])
        elif az["MSN"][i] == "TEPRB":
            nm_teprb = nm["Data"][i]
            nm_msn.append(nm["MSN"][i])
            nm_year.append(nm["Year"][i])
            nm_data.append(nm["Data"][i])
        else:
            pass
    else:
        pass
nm_renewable = OrderedDict()
nm_renewable["MSN"] = nm_msn
nm_renewable["Year"] = nm_year
nm_renewable["Data"] = nm_data
nm_renewable_data = pd.DataFrame(nm_renewable)
nm_renewable_data.to_csv("data/csv/renewable/nm_renewable.csv", index=False, index_label=False, sep=',')

# tx
tx_msn = []
tx_year = []
tx_data = []
for i in range(len(tx["MSN"])):
    if tx["Year"][i] == 2009:
        if tx["MSN"][i] == "REPRB":
            tx_reprb = tx["Data"][i]
            tx_msn.append(tx["MSN"][i])
            tx_year.append(tx["Year"][i])
            tx_data.append(tx["Data"][i])
        elif tx["MSN"][i] == "RETCB":
            tx_retcb = tx["Data"][i]
            tx_msn.append(tx["MSN"][i])
            tx_year.append(tx["Year"][i])
            tx_data.append(tx["Data"][i])
        elif tx["MSN"][i] == "ROPRB":
            tx_roprb = tx["Data"][i]
            tx_msn.append(tx["MSN"][i])
            tx_year.append(tx["Year"][i])
            tx_data.append(tx["Data"][i])
        elif tx["MSN"][i] == "TPOPP":
            tx_tpopp = tx["Data"][i]
            tx_msn.append(tx["MSN"][i])
            tx_year.append(tx["Year"][i])
            tx_data.append(tx["Data"][i])
        elif tx["MSN"][i] == "TETCB":
            tx_tetcb = tx["Data"][i]
            tx_msn.append(tx["MSN"][i])
            tx_year.append(tx["Year"][i])
            tx_data.append(tx["Data"][i])
        elif tx["MSN"][i] == "TEPRB":
            tx_teprb = tx["Data"][i]
            tx_msn.append(tx["MSN"][i])
            tx_year.append(tx["Year"][i])
            tx_data.append(tx["Data"][i])
        else:
            pass
    else:
        pass
tx_renewable = OrderedDict()
tx_renewable["MSN"] = tx_msn
tx_renewable["Year"] = tx_year
tx_renewable["Data"] = tx_data
tx_renewable_data = pd.DataFrame(tx_renewable)
tx_renewable_data.to_csv("data/csv/renewable/tx_renewable.csv", index=False, index_label=False, sep=',')
