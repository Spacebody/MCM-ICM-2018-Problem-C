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
msncodes = pd.read_csv(
    "data/csv/price_expenditures/sector/price_sector.csv", engine='c', low_memory=True)["MSN"]
#load state data
az_data = pd.read_csv(
    "data/csv/state_data/az_data.csv", engine='c', low_memory=True)
ca_data = pd.read_csv(
    "data/csv/state_data/ca_data.csv", engine='c', low_memory=True)
nm_data = pd.read_csv(
    "data/csv/state_data/nm_data.csv", engine='c', low_memory=True)
tx_data = pd.read_csv(
    "data/csv/state_data/tx_data.csv", engine='c', low_memory=True)

sources = ["TEACD", "TECCD", "TEICD", "TERCD"]

# az
az_msn = []
az_year = []
az_value = []

for i in range(len(az_data["MSN"])):
    for j in range(len(msncodes)):
        if az_data["MSN"][i] == msncodes[j]:
            az_msn.append(az_data["MSN"][i])
            az_year.append(az_data["Year"][i])
            az_value.append(az_data["Data"][i])
        else:
            pass

az_price = OrderedDict()
az_price["MSN"] = az_msn
az_price["Year"] = az_year
az_price["Data"] = az_value
az_price_data = pd.DataFrame(az_price)

az_price_data.to_csv("data/csv/price_expenditures/sector/az/az_price.csv",
                   index=False, index_label=False, sep=',')
# print(az_price_data)

az_teacd = OrderedDict()
az_teacd["Year"] = []
az_teacd["Data"] = []
az_teccd = OrderedDict()
az_teccd["Year"] = []
az_teccd["Data"] = []
az_teicd = OrderedDict()
az_teicd["Year"] = []
az_teicd["Data"] = []
az_tercd = OrderedDict()
az_tercd["Year"] = []
az_tercd["Data"] = []

for i in range(len(az_price_data["MSN"])):
    if az_price_data["MSN"][i] == "TEACD":
        az_teacd["Year"].append(az_price_data["Year"][i])
        az_teacd["Data"].append(az_price_data["Data"][i])
    elif az_price_data["MSN"][i] == "TECCD":
        az_teccd["Year"].append(az_price_data["Year"][i])
        az_teccd["Data"].append(az_price_data["Data"][i])
    elif az_price_data["MSN"][i] == "TEICD":
        az_teicd["Year"].append(az_price_data["Year"][i])
        az_teicd["Data"].append(az_price_data["Data"][i])
    elif az_price_data["MSN"][i] == "TERCD":
        az_tercd["Year"].append(az_price_data["Year"][i])
        az_tercd["Data"].append(az_price_data["Data"][i])
    else:
        pass

az_teacd_data = pd.DataFrame(az_teacd)
az_teacd_data.to_csv("data/csv/price_expenditures/sector/az/price/teacd.csv",
                     index=False, index_label=False, sep=',')
az_teccd_data = pd.DataFrame(az_teccd)
az_teccd_data.to_csv("data/csv/price_expenditures/sector/az/price/teccd.csv",
                     index=False, index_label=False, sep=',')
az_teicd_data = pd.DataFrame(az_teicd)
az_teicd_data.to_csv("data/csv/price_expenditures/sector/az/price/teicd.csv",
                     index=False, index_label=False, sep=',')
az_tercd_data = pd.DataFrame(az_tercd)
az_tercd_data.to_csv("data/csv/price_expenditures/sector/az/price/tercd.csv",
                     index=False, index_label=False, sep=',')
# print(teacd_data)
# print(teccd_data)
# print(teicd_data)
# print(tercd_data)

# ca
ca_msn = []
ca_year = []
ca_value = []

for i in range(len(ca_data["MSN"])):
    for j in range(len(msncodes)):
        if ca_data["MSN"][i] == msncodes[j]:
            ca_msn.append(ca_data["MSN"][i])
            ca_year.append(ca_data["Year"][i])
            ca_value.append(ca_data["Data"][i])
        else:
            pass

ca_price = OrderedDict()
ca_price["MSN"] = ca_msn
ca_price["Year"] = ca_year
ca_price["Data"] = ca_value
ca_price_data = pd.DataFrame(ca_price)

ca_price_data.to_csv("data/csv/price_expenditures/sector/ca/ca_price.csv",
                   index=False, index_label=False, sep=',')
# print(ca_price_data)

ca_teacd = OrderedDict()
ca_teacd["Year"] = []
ca_teacd["Data"] = []
ca_teccd = OrderedDict()
ca_teccd["Year"] = []
ca_teccd["Data"] = []
ca_teicd = OrderedDict()
ca_teicd["Year"] = []
ca_teicd["Data"] = []
ca_tercd = OrderedDict()
ca_tercd["Year"] = []
ca_tercd["Data"] = []

for i in range(len(ca_price_data["MSN"])):
    if ca_price_data["MSN"][i] == "TEACD":
        ca_teacd["Year"].append(ca_price_data["Year"][i])
        ca_teacd["Data"].append(ca_price_data["Data"][i])
    elif ca_price_data["MSN"][i] == "TECCD":
        ca_teccd["Year"].append(ca_price_data["Year"][i])
        ca_teccd["Data"].append(ca_price_data["Data"][i])
    elif ca_price_data["MSN"][i] == "TEICD":
        ca_teicd["Year"].append(ca_price_data["Year"][i])
        ca_teicd["Data"].append(ca_price_data["Data"][i])
    elif ca_price_data["MSN"][i] == "TERCD":
        ca_tercd["Year"].append(ca_price_data["Year"][i])
        ca_tercd["Data"].append(ca_price_data["Data"][i])
    else:
        pass

ca_teacd_data = pd.DataFrame(ca_teacd)
ca_teacd_data.to_csv("data/csv/price_expenditures/sector/ca/price/teacd.csv",
                     index=False, index_label=False, sep=',')
ca_teccd_data = pd.DataFrame(ca_teccd)
ca_teccd_data.to_csv("data/csv/price_expenditures/sector/ca/price/teccd.csv",
                     index=False, index_label=False, sep=',')
ca_teicd_data = pd.DataFrame(ca_teicd)
ca_teicd_data.to_csv("data/csv/price_expenditures/sector/ca/price/teicd.csv",
                     index=False, index_label=False, sep=',')
ca_tercd_data = pd.DataFrame(ca_tercd)
ca_tercd_data.to_csv("data/csv/price_expenditures/sector/ca/price/tercd.csv",
                     index=False, index_label=False, sep=',')

# nm
nm_msn = []
nm_year = []
nm_value = []

for i in range(len(nm_data["MSN"])):
    for j in range(len(msncodes)):
        if nm_data["MSN"][i] == msncodes[j]:
            nm_msn.append(nm_data["MSN"][i])
            nm_year.append(nm_data["Year"][i])
            nm_value.append(nm_data["Data"][i])
        else:
            pass

nm_price = OrderedDict()
nm_price["MSN"] = nm_msn
nm_price["Year"] = nm_year
nm_price["Data"] = nm_value
nm_price_data = pd.DataFrame(nm_price)

nm_price_data.to_csv("data/csv/price_expenditures/sector/nm/nm_price.csv",
                   index=False, index_label=False, sep=',')
# print(nm_price_data)

nm_teacd = OrderedDict()
nm_teacd["Year"] = []
nm_teacd["Data"] = []
nm_teccd = OrderedDict()
nm_teccd["Year"] = []
nm_teccd["Data"] = []
nm_teicd = OrderedDict()
nm_teicd["Year"] = []
nm_teicd["Data"] = []
nm_tercd = OrderedDict()
nm_tercd["Year"] = []
nm_tercd["Data"] = []

for i in range(len(nm_price_data["MSN"])):
    if nm_price_data["MSN"][i] == "TEACD":
        nm_teacd["Year"].append(nm_price_data["Year"][i])
        nm_teacd["Data"].append(nm_price_data["Data"][i])
    elif nm_price_data["MSN"][i] == "TECCD":
        nm_teccd["Year"].append(nm_price_data["Year"][i])
        nm_teccd["Data"].append(nm_price_data["Data"][i])
    elif nm_price_data["MSN"][i] == "TEICD":
        nm_teicd["Year"].append(nm_price_data["Year"][i])
        nm_teicd["Data"].append(nm_price_data["Data"][i])
    elif nm_price_data["MSN"][i] == "TERCD":
        nm_tercd["Year"].append(nm_price_data["Year"][i])
        nm_tercd["Data"].append(nm_price_data["Data"][i])
    else:
        pass

nm_teacd_data = pd.DataFrame(nm_teacd)
nm_teacd_data.to_csv("data/csv/price_expenditures/sector/nm/price/teacd.csv",
                     index=False, index_label=False, sep=',')
nm_teccd_data = pd.DataFrame(nm_teccd)
nm_teccd_data.to_csv("data/csv/price_expenditures/sector/nm/price/teccd.csv",
                     index=False, index_label=False, sep=',')
nm_teicd_data = pd.DataFrame(nm_teicd)
nm_teicd_data.to_csv("data/csv/price_expenditures/sector/nm/price/teicd.csv",
                     index=False, index_label=False, sep=',')
nm_tercd_data = pd.DataFrame(nm_tercd)
nm_tercd_data.to_csv("data/csv/price_expenditures/sector/nm/price/tercd.csv",
                     index=False, index_label=False, sep=',')


# tx
tx_msn = []
tx_year = []
tx_value = []

for i in range(len(tx_data["MSN"])):
    for j in range(len(msncodes)):
        if tx_data["MSN"][i] == msncodes[j]:
            tx_msn.append(tx_data["MSN"][i])
            tx_year.append(tx_data["Year"][i])
            tx_value.append(tx_data["Data"][i])
        else:
            pass

tx_price = OrderedDict()
tx_price["MSN"] = tx_msn
tx_price["Year"] = tx_year
tx_price["Data"] = tx_value
tx_price_data = pd.DataFrame(tx_price)

tx_price_data.to_csv("data/csv/price_expenditures/sector/tx/tx_price.csv",
                   index=False, index_label=False, sep=',')
# print(tx_price_data)

tx_teacd = OrderedDict()
tx_teacd["Year"] = []
tx_teacd["Data"] = []
tx_teccd = OrderedDict()
tx_teccd["Year"] = []
tx_teccd["Data"] = []
tx_teicd = OrderedDict()
tx_teicd["Year"] = []
tx_teicd["Data"] = []
tx_tercd = OrderedDict()
tx_tercd["Year"] = []
tx_tercd["Data"] = []

for i in range(len(tx_price_data["MSN"])):
    if tx_price_data["MSN"][i] == "TEACD":
        tx_teacd["Year"].append(tx_price_data["Year"][i])
        tx_teacd["Data"].append(tx_price_data["Data"][i])
    elif tx_price_data["MSN"][i] == "TECCD":
        tx_teccd["Year"].append(tx_price_data["Year"][i])
        tx_teccd["Data"].append(tx_price_data["Data"][i])
    elif tx_price_data["MSN"][i] == "TEICD":
        tx_teicd["Year"].append(tx_price_data["Year"][i])
        tx_teicd["Data"].append(tx_price_data["Data"][i])
    elif tx_price_data["MSN"][i] == "TERCD":
        tx_tercd["Year"].append(tx_price_data["Year"][i])
        tx_tercd["Data"].append(tx_price_data["Data"][i])
    else:
        pass

tx_teacd_data = pd.DataFrame(tx_teacd)
tx_teacd_data.to_csv("data/csv/price_expenditures/sector/tx/price/teacd.csv",
                     index=False, index_label=False, sep=',')
tx_teccd_data = pd.DataFrame(tx_teccd)
tx_teccd_data.to_csv("data/csv/price_expenditures/sector/tx/price/teccd.csv",
                     index=False, index_label=False, sep=',')
tx_teicd_data = pd.DataFrame(tx_teicd)
tx_teicd_data.to_csv("data/csv/price_expenditures/sector/tx/price/teicd.csv",
                     index=False, index_label=False, sep=',')
tx_tercd_data = pd.DataFrame(tx_tercd)
tx_tercd_data.to_csv("data/csv/price_expenditures/sector/tx/price/tercd.csv",
                     index=False, index_label=False, sep=',')
