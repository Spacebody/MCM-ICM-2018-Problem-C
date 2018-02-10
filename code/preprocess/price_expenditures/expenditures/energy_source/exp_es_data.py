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

#load energy_source msncodes
msncodes = pd.read_csv(
    "data/csv/price_expenditures/energy_source/exp_es.csv", engine='c')["MSN"]
#load state data
az_data = pd.read_csv(
    "data/csv/consumption/state_data/az_data.csv", engine='c')
ca_data = pd.read_csv(
    "data/csv/consumption/state_data/ca_data.csv", engine='c')
nm_data = pd.read_csv(
    "data/csv/consumption/state_data/nm_data.csv", engine='c')
tx_data = pd.read_csv(
    "data/csv/consumption/state_data/tx_data.csv", engine='c')

sources = ["CLTCV", "ESTCV", "NUETV", "NUETV", "PATCV"]

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

az_exp_data.to_csv("data/csv/price_expenditures/energy_source/az/az_exp.csv",
                   index=False, index_label=False, sep=',')
# print(az_exp_data)

az_cltcv = OrderedDict()
az_cltcv["Year"] = []
az_cltcv["Data"] = []
az_estcv = OrderedDict()
az_estcv["Year"] = []
az_estcv["Data"] = []
az_ngtcv = OrderedDict()
az_ngtcv["Year"] = []
az_ngtcv["Data"] = []
az_nuetv = OrderedDict()
az_nuetv["Year"] = []
az_nuetv["Data"] = []
az_patcv = OrderedDict()
az_patcv["Year"] = []
az_patcv["Data"] = []

for i in range(len(az_exp_data["MSN"])):
    if az_exp_data["MSN"][i] == "CLTCV":
        az_cltcv["Year"].append(az_exp_data["Year"][i])
        az_cltcv["Data"].append(az_exp_data["Data"][i])
    elif az_exp_data["MSN"][i] == "ESTCV":
        az_estcv["Year"].append(az_exp_data["Year"][i])
        az_estcv["Data"].append(az_exp_data["Data"][i])
    elif az_exp_data["MSN"][i] == "NGTCV":
        az_ngtcv["Year"].append(az_exp_data["Year"][i])
        az_ngtcv["Data"].append(az_exp_data["Data"][i])
    elif az_exp_data["MSN"][i] == "NUETV":
        az_nuetv["Year"].append(az_exp_data["Year"][i])
        az_nuetv["Data"].append(az_exp_data["Data"][i])
    elif az_exp_data["MSN"][i] == "PATCV":
        az_patcv["Year"].append(az_exp_data["Year"][i])
        az_patcv["Data"].append(az_exp_data["Data"][i])
    else:
        pass

az_cltcv_data = pd.DataFrame(az_cltcv)
az_cltcv_data.to_csv("data/csv/price_expenditures/energy_source/az/expenditures/cltcv.csv",
                     index=False, index_label=False, sep=',')
az_estcv_data = pd.DataFrame(az_estcv)
az_estcv_data.to_csv("data/csv/price_expenditures/energy_source/az/expenditures/estcv.csv",
                     index=False, index_label=False, sep=',')
az_ngtcv_data = pd.DataFrame(az_ngtcv)
az_ngtcv_data.to_csv("data/csv/price_expenditures/energy_source/az/expenditures/ngtcv.csv",
                     index=False, index_label=False, sep=',')
az_nuetv_data = pd.DataFrame(az_nuetv)
az_nuetv_data.to_csv("data/csv/price_expenditures/energy_source/az/expenditures/nuetv.csv",
                     index=False, index_label=False, sep=',')
az_patcv_data = pd.DataFrame(az_patcv)
az_patcv_data.to_csv("data/csv/price_expenditures/energy_source/az/expenditures/patcv.csv",
                     index=False, index_label=False, sep=',')
# print(cltcv_data)
# print(estcv_data)
# print(ngtcv_data)
# print(nuetv_data)

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

ca_exp_data.to_csv("data/csv/price_expenditures/energy_source/ca/ca_exp.csv",
                   index=False, index_label=False, sep=',')
# print(ca_exp_data)

ca_cltcv = OrderedDict()
ca_cltcv["Year"] = []
ca_cltcv["Data"] = []
ca_estcv = OrderedDict()
ca_estcv["Year"] = []
ca_estcv["Data"] = []
ca_ngtcv = OrderedDict()
ca_ngtcv["Year"] = []
ca_ngtcv["Data"] = []
ca_nuetv = OrderedDict()
ca_nuetv["Year"] = []
ca_nuetv["Data"] = []
ca_patcv = OrderedDict()
ca_patcv["Year"] = []
ca_patcv["Data"] = []

for i in range(len(ca_exp_data["MSN"])):
    if ca_exp_data["MSN"][i] == "CLTCV":
        ca_cltcv["Year"].append(ca_exp_data["Year"][i])
        ca_cltcv["Data"].append(ca_exp_data["Data"][i])
    elif ca_exp_data["MSN"][i] == "ESTCV":
        ca_estcv["Year"].append(ca_exp_data["Year"][i])
        ca_estcv["Data"].append(ca_exp_data["Data"][i])
    elif ca_exp_data["MSN"][i] == "NGTCV":
        ca_ngtcv["Year"].append(ca_exp_data["Year"][i])
        ca_ngtcv["Data"].append(ca_exp_data["Data"][i])
    elif ca_exp_data["MSN"][i] == "NUETV":
        ca_nuetv["Year"].append(ca_exp_data["Year"][i])
        ca_nuetv["Data"].append(ca_exp_data["Data"][i])
    elif ca_exp_data["MSN"][i] == "PATCV":
        ca_patcv["Year"].append(ca_exp_data["Year"][i])
        ca_patcv["Data"].append(ca_exp_data["Data"][i])
    else:
        pass

ca_cltcv_data = pd.DataFrame(ca_cltcv)
ca_cltcv_data.to_csv("data/csv/price_expenditures/energy_source/ca/expenditures/cltcv.csv",
                     index=False, index_label=False, sep=',')
ca_estcv_data = pd.DataFrame(ca_estcv)
ca_estcv_data.to_csv("data/csv/price_expenditures/energy_source/ca/expenditures/estcv.csv",
                     index=False, index_label=False, sep=',')
ca_ngtcv_data = pd.DataFrame(ca_ngtcv)
ca_ngtcv_data.to_csv("data/csv/price_expenditures/energy_source/ca/expenditures/ngtcv.csv",
                     index=False, index_label=False, sep=',')
ca_nuetv_data = pd.DataFrame(ca_nuetv)
ca_nuetv_data.to_csv("data/csv/price_expenditures/energy_source/ca/expenditures/nuetv.csv",
                     index=False, index_label=False, sep=',')
ca_patcv_data = pd.DataFrame(ca_patcv)
ca_patcv_data.to_csv("data/csv/price_expenditures/energy_source/ca/expenditures/patcv.csv",
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

nm_exp = OrderedDict()
nm_exp["MSN"] = nm_msn
nm_exp["Year"] = nm_year
nm_exp["Data"] = nm_value
nm_exp_data = pd.DataFrame(nm_exp)

nm_exp_data.to_csv("data/csv/price_expenditures/energy_source/nm/nm_exp.csv",
                   index=False, index_label=False, sep=',')
# print(nm_exp_data)

nm_cltcv = OrderedDict()
nm_cltcv["Year"] = []
nm_cltcv["Data"] = []
nm_estcv = OrderedDict()
nm_estcv["Year"] = []
nm_estcv["Data"] = []
nm_ngtcv = OrderedDict()
nm_ngtcv["Year"] = []
nm_ngtcv["Data"] = []
nm_nuetv = OrderedDict()
nm_nuetv["Year"] = []
nm_nuetv["Data"] = []
nm_patcv = OrderedDict()
nm_patcv["Year"] = []
nm_patcv["Data"] = []

for i in range(len(nm_exp_data["MSN"])):
    if nm_exp_data["MSN"][i] == "CLTCV":
        nm_cltcv["Year"].append(nm_exp_data["Year"][i])
        nm_cltcv["Data"].append(nm_exp_data["Data"][i])
    elif nm_exp_data["MSN"][i] == "ESTCV":
        nm_estcv["Year"].append(nm_exp_data["Year"][i])
        nm_estcv["Data"].append(nm_exp_data["Data"][i])
    elif nm_exp_data["MSN"][i] == "NGTCV":
        nm_ngtcv["Year"].append(nm_exp_data["Year"][i])
        nm_ngtcv["Data"].append(nm_exp_data["Data"][i])
    elif nm_exp_data["MSN"][i] == "NUETV":
        nm_nuetv["Year"].append(nm_exp_data["Year"][i])
        nm_nuetv["Data"].append(nm_exp_data["Data"][i])
    elif nm_exp_data["MSN"][i] == "PATCV":
        nm_patcv["Year"].append(nm_exp_data["Year"][i])
        nm_patcv["Data"].append(nm_exp_data["Data"][i])
    else:
        pass

nm_cltcv_data = pd.DataFrame(nm_cltcv)
nm_cltcv_data.to_csv("data/csv/price_expenditures/energy_source/nm/expenditures/cltcv.csv",
                     index=False, index_label=False, sep=',')
nm_estcv_data = pd.DataFrame(nm_estcv)
nm_estcv_data.to_csv("data/csv/price_expenditures/energy_source/nm/expenditures/estcv.csv",
                     index=False, index_label=False, sep=',')
nm_ngtcv_data = pd.DataFrame(nm_ngtcv)
nm_ngtcv_data.to_csv("data/csv/price_expenditures/energy_source/nm/expenditures/ngtcv.csv",
                     index=False, index_label=False, sep=',')
nm_nuetv_data = pd.DataFrame(nm_nuetv)
nm_nuetv_data.to_csv("data/csv/price_expenditures/energy_source/nm/expenditures/nuetv.csv",
                     index=False, index_label=False, sep=',')
nm_patcv_data = pd.DataFrame(nm_patcv)
nm_patcv_data.to_csv("data/csv/price_expenditures/energy_source/nm/expenditures/patcv.csv",
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

tx_exp = OrderedDict()
tx_exp["MSN"] = tx_msn
tx_exp["Year"] = tx_year
tx_exp["Data"] = tx_value
tx_exp_data = pd.DataFrame(tx_exp)

tx_exp_data.to_csv("data/csv/price_expenditures/energy_source/tx/tx_exp.csv",
                   index=False, index_label=False, sep=',')
# print(tx_exp_data)

tx_cltcv = OrderedDict()
tx_cltcv["Year"] = []
tx_cltcv["Data"] = []
tx_estcv = OrderedDict()
tx_estcv["Year"] = []
tx_estcv["Data"] = []
tx_ngtcv = OrderedDict()
tx_ngtcv["Year"] = []
tx_ngtcv["Data"] = []
tx_nuetv = OrderedDict()
tx_nuetv["Year"] = []
tx_nuetv["Data"] = []
tx_patcv = OrderedDict()
tx_patcv["Year"] = []
tx_patcv["Data"] = []

for i in range(len(tx_exp_data["MSN"])):
    if tx_exp_data["MSN"][i] == "CLTCV":
        tx_cltcv["Year"].append(tx_exp_data["Year"][i])
        tx_cltcv["Data"].append(tx_exp_data["Data"][i])
    elif tx_exp_data["MSN"][i] == "ESTCV":
        tx_estcv["Year"].append(tx_exp_data["Year"][i])
        tx_estcv["Data"].append(tx_exp_data["Data"][i])
    elif tx_exp_data["MSN"][i] == "NGTCV":
        tx_ngtcv["Year"].append(tx_exp_data["Year"][i])
        tx_ngtcv["Data"].append(tx_exp_data["Data"][i])
    elif tx_exp_data["MSN"][i] == "NUETV":
        tx_nuetv["Year"].append(tx_exp_data["Year"][i])
        tx_nuetv["Data"].append(tx_exp_data["Data"][i])
    elif tx_exp_data["MSN"][i] == "PATCV":
        tx_patcv["Year"].append(tx_exp_data["Year"][i])
        tx_patcv["Data"].append(tx_exp_data["Data"][i])
    else:
        pass

tx_cltcv_data = pd.DataFrame(tx_cltcv)
tx_cltcv_data.to_csv("data/csv/price_expenditures/energy_source/tx/expenditures/cltcv.csv",
                     index=False, index_label=False, sep=',')
tx_estcv_data = pd.DataFrame(tx_estcv)
tx_estcv_data.to_csv("data/csv/price_expenditures/energy_source/tx/expenditures/estcv.csv",
                     index=False, index_label=False, sep=',')
tx_ngtcv_data = pd.DataFrame(tx_ngtcv)
tx_ngtcv_data.to_csv("data/csv/price_expenditures/energy_source/tx/expenditures/ngtcv.csv",
                     index=False, index_label=False, sep=',')
tx_nuetv_data = pd.DataFrame(tx_nuetv)
tx_nuetv_data.to_csv("data/csv/price_expenditures/energy_source/tx/expenditures/nuetv.csv",
                     index=False, index_label=False, sep=',')
tx_patcv_data = pd.DataFrame(tx_patcv)
tx_patcv_data.to_csv("data/csv/price_expenditures/energy_source/tx/expenditures/patcv.csv",
                     index=False, index_label=False, sep=',')

