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
    "data/csv/price_expenditures/sector/exp.csv", engine='c', low_memory=True)["MSN"]
#load state data
az_data = pd.read_csv("data/csv/state_data/az_data.csv", engine='c', low_memory=True)
ca_data = pd.read_csv("data/csv/state_data/ca_data.csv", engine='c', low_memory=True)
nm_data = pd.read_csv("data/csv/state_data/nm_data.csv", engine='c', low_memory=True)
tx_data = pd.read_csv("data/csv/state_data/tx_data.csv", engine='c', low_memory=True)

sectors = ["TEACV", "TECCV", "TEICV", "TERCV"]

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

az_exp = OrderedDict()
az_exp["MSN"] = az_msn
az_exp["Year"] = az_year
az_exp["Data"] = az_value
az_exp_data = pd.DataFrame(az_exp)

az_exp_data.to_csv("data/csv/price_expenditures/sector/az/az_exp.csv",
                  index=False, index_label=False, sep=',')
# print(az_exp_data)

az_teacv = OrderedDict()
az_teacv["Year"] = []
az_teacv["Data"] = []
az_teccv = OrderedDict()
az_teccv["Year"] = []
az_teccv["Data"] = []
az_teicv = OrderedDict()
az_teicv["Year"] = []
az_teicv["Data"] = []
az_tercv = OrderedDict()
az_tercv["Year"] = []
az_tercv["Data"] = []


for i in range(len(az_exp_data["MSN"])):
    if az_exp_data["MSN"][i] == "TEACV":
        az_teacv["Year"].append(az_exp_data["Year"][i])
        az_teacv["Data"].append(az_exp_data["Data"][i])
    elif az_exp_data["MSN"][i] == "TECCV":
        az_teccv["Year"].append(az_exp_data["Year"][i])
        az_teccv["Data"].append(az_exp_data["Data"][i])
    elif az_exp_data["MSN"][i] == "TEICV":
        az_teicv["Year"].append(az_exp_data["Year"][i])
        az_teicv["Data"].append(az_exp_data["Data"][i])
    elif az_exp_data["MSN"][i] == "TERCV":
        az_tercv["Year"].append(az_exp_data["Year"][i])
        az_tercv["Data"].append(az_exp_data["Data"][i])
    else:
        pass

az_teacv_data = pd.DataFrame(az_teacv)
az_teacv_data.to_csv("data/csv/price_expenditures/sector/az/expenditures/teacv.csv",
                  index=False, index_label=False, sep=',')
az_teccv_data = pd.DataFrame(az_teccv)
az_teccv_data.to_csv("data/csv/price_expenditures/sector/az/expenditures/teccv.csv",
                  index=False, index_label=False, sep=',')
az_teicv_data = pd.DataFrame(az_teicv)
az_teicv_data.to_csv("data/csv/price_expenditures/sector/az/expenditures/teicv.csv",
                  index=False, index_label=False, sep=',')
az_tercv_data = pd.DataFrame(az_tercv)
az_tercv_data.to_csv("data/csv/price_expenditures/sector/az/expenditures/tercv.csv",
                  index=False, index_label=False, sep=',')
# print(teacv_data)
# print(teccv_data)
# print(teicv_data)
# print(tercv_data)

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

ca_exp = OrderedDict()
ca_exp["MSN"] = ca_msn
ca_exp["Year"] = ca_year
ca_exp["Data"] = ca_value
ca_exp_data = pd.DataFrame(ca_exp)

ca_exp_data.to_csv("data/csv/price_expenditures/sector/ca/ca_exp.csv",
                   index=False, index_label=False, sep=',')
# print(ca_exp_data)

ca_teacv = OrderedDict()
ca_teacv["Year"] = []
ca_teacv["Data"] = []
ca_teccv = OrderedDict()
ca_teccv["Year"] = []
ca_teccv["Data"] = []
ca_teicv = OrderedDict()
ca_teicv["Year"] = []
ca_teicv["Data"] = []
ca_tercv = OrderedDict()
ca_tercv["Year"] = []
ca_tercv["Data"] = []


for i in range(len(ca_exp_data["MSN"])):
    if ca_exp_data["MSN"][i] == "TEACV":
        ca_teacv["Year"].append(ca_exp_data["Year"][i])
        ca_teacv["Data"].append(ca_exp_data["Data"][i])
    elif ca_exp_data["MSN"][i] == "TECCV":
        ca_teccv["Year"].append(ca_exp_data["Year"][i])
        ca_teccv["Data"].append(ca_exp_data["Data"][i])
    elif ca_exp_data["MSN"][i] == "TEICV":
        ca_teicv["Year"].append(ca_exp_data["Year"][i])
        ca_teicv["Data"].append(ca_exp_data["Data"][i])
    elif ca_exp_data["MSN"][i] == "TERCV":
        ca_tercv["Year"].append(ca_exp_data["Year"][i])
        ca_tercv["Data"].append(ca_exp_data["Data"][i])
    else:
        pass

ca_teacv_data = pd.DataFrame(ca_teacv)
ca_teacv_data.to_csv("data/csv/price_expenditures/sector/ca/expenditures/teacv.csv",
                  index=False, index_label=False, sep=',')
ca_teccv_data = pd.DataFrame(ca_teccv)
ca_teccv_data.to_csv("data/csv/price_expenditures/sector/ca/expenditures/teccv.csv",
                  index=False, index_label=False, sep=',')
ca_teicv_data = pd.DataFrame(ca_teicv)
ca_teicv_data.to_csv("data/csv/price_expenditures/sector/ca/expenditures/teicv.csv",
                  index=False, index_label=False, sep=',')
ca_tercv_data = pd.DataFrame(ca_tercv)
ca_tercv_data.to_csv("data/csv/price_expenditures/sector/ca/expenditures/tercv.csv",
                  index=False, index_label=False, sep=',')
# print(teacv_data)
# print(teccv_data)
# print(teicv_data)
# print(tercv_data)

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

nm_exp = OrderedDict()
nm_exp["MSN"] = nm_msn
nm_exp["Year"] = nm_year
nm_exp["Data"] = nm_value
nm_exp_data = pd.DataFrame(nm_exp)

nm_exp_data.to_csv("data/csv/price_expenditures/sector/nm/nm_exp.csv",
                   index=False, index_label=False, sep=',')
# print(nm_exp_data)

nm_teacv = OrderedDict()
nm_teacv["Year"] = []
nm_teacv["Data"] = []
nm_teccv = OrderedDict()
nm_teccv["Year"] = []
nm_teccv["Data"] = []
nm_teicv = OrderedDict()
nm_teicv["Year"] = []
nm_teicv["Data"] = []
nm_tercv = OrderedDict()
nm_tercv["Year"] = []
nm_tercv["Data"] = []


for i in range(len(nm_exp_data["MSN"])):
    if nm_exp_data["MSN"][i] == "TEACV":
        nm_teacv["Year"].append(nm_exp_data["Year"][i])
        nm_teacv["Data"].append(nm_exp_data["Data"][i])
    elif nm_exp_data["MSN"][i] == "TECCV":
        nm_teccv["Year"].append(nm_exp_data["Year"][i])
        nm_teccv["Data"].append(nm_exp_data["Data"][i])
    elif nm_exp_data["MSN"][i] == "TEICV":
        nm_teicv["Year"].append(nm_exp_data["Year"][i])
        nm_teicv["Data"].append(nm_exp_data["Data"][i])
    elif nm_exp_data["MSN"][i] == "TERCV":
        nm_tercv["Year"].append(nm_exp_data["Year"][i])
        nm_tercv["Data"].append(nm_exp_data["Data"][i])
    else:
        pass

nm_teacv_data = pd.DataFrame(nm_teacv)
nm_teacv_data.to_csv("data/csv/price_expenditures/sector/nm/expenditures/teacv.csv",
                  index=False, index_label=False, sep=',')
nm_teccv_data = pd.DataFrame(nm_teccv)
nm_teccv_data.to_csv("data/csv/price_expenditures/sector/nm/expenditures/teccv.csv",
                  index=False, index_label=False, sep=',')
nm_teicv_data = pd.DataFrame(nm_teicv)
nm_teicv_data.to_csv("data/csv/price_expenditures/sector/nm/expenditures/teicv.csv",
                  index=False, index_label=False, sep=',')
nm_tercv_data = pd.DataFrame(nm_tercv)
nm_tercv_data.to_csv("data/csv/price_expenditures/sector/nm/expenditures/tercv.csv",
                  index=False, index_label=False, sep=',')
# print(teacv_data)
# print(teccv_data)
# print(teicv_data)
# print(tercv_data)

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

tx_exp = OrderedDict()
tx_exp["MSN"] = tx_msn
tx_exp["Year"] = tx_year
tx_exp["Data"] = tx_value
tx_exp_data = pd.DataFrame(tx_exp)

tx_exp_data.to_csv("data/csv/price_expenditures/sector/tx/tx_exp.csv",
                   index=False, index_label=False, sep=',')
# print(tx_exp_data)

tx_teacv = OrderedDict()
tx_teacv["Year"] = []
tx_teacv["Data"] = []
tx_teccv = OrderedDict()
tx_teccv["Year"] = []
tx_teccv["Data"] = []
tx_teicv = OrderedDict()
tx_teicv["Year"] = []
tx_teicv["Data"] = []
tx_tercv = OrderedDict()
tx_tercv["Year"] = []
tx_tercv["Data"] = []


for i in range(len(tx_exp_data["MSN"])):
    if tx_exp_data["MSN"][i] == "TEACV":
        tx_teacv["Year"].append(tx_exp_data["Year"][i])
        tx_teacv["Data"].append(tx_exp_data["Data"][i])
    elif tx_exp_data["MSN"][i] == "TECCV":
        tx_teccv["Year"].append(tx_exp_data["Year"][i])
        tx_teccv["Data"].append(tx_exp_data["Data"][i])
    elif tx_exp_data["MSN"][i] == "TEICV":
        tx_teicv["Year"].append(tx_exp_data["Year"][i])
        tx_teicv["Data"].append(tx_exp_data["Data"][i])
    elif tx_exp_data["MSN"][i] == "TERCV":
        tx_tercv["Year"].append(tx_exp_data["Year"][i])
        tx_tercv["Data"].append(tx_exp_data["Data"][i])
    else:
        pass

tx_teacv_data = pd.DataFrame(tx_teacv)
tx_teacv_data.to_csv("data/csv/price_expenditures/sector/tx/expenditures/teacv.csv",
                  index=False, index_label=False, sep=',')
tx_teccv_data = pd.DataFrame(tx_teccv)
tx_teccv_data.to_csv("data/csv/price_expenditures/sector/tx/expenditures/teccv.csv",
                  index=False, index_label=False, sep=',')
tx_teicv_data = pd.DataFrame(tx_teicv)
tx_teicv_data.to_csv("data/csv/price_expenditures/sector/tx/expenditures/teicv.csv",
                  index=False, index_label=False, sep=',')
tx_tercv_data = pd.DataFrame(tx_tercv)
tx_tercv_data.to_csv("data/csv/price_expenditures/sector/tx/expenditures/tercv.csv",
                  index=False, index_label=False, sep=',')
# print(teacv_data)
# print(teccv_data)
# print(teicv_data)
# print(tercv_data)
