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
    "data/csv/price_expenditures/energy_source/price_es.csv", engine='c')["MSN"]
#load state data
az_data = pd.read_csv(
    "data/csv/consumption/state_data/az_data.csv", engine='c')
ca_data = pd.read_csv(
    "data/csv/consumption/state_data/ca_data.csv", engine='c')
nm_data = pd.read_csv(
    "data/csv/consumption/state_data/nm_data.csv", engine='c')
tx_data = pd.read_csv(
    "data/csv/consumption/state_data/tx_data.csv", engine='c')

sources = ["CLTCD", "ESTCD", "NUETD", "NGTCD", "PATCD", "WWTCD"]

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

az_price_data.to_csv("data/csv/price_expenditures/energy_source/az/az_price.csv",
                   index=False, index_label=False, sep=',')
# print(az_price_data)

az_cltcd = OrderedDict()
az_cltcd["Year"] = []
az_cltcd["Data"] = []
az_estcd = OrderedDict()
az_estcd["Year"] = []
az_estcd["Data"] = []
az_ngtcd = OrderedDict()
az_ngtcd["Year"] = []
az_ngtcd["Data"] = []
az_nuetd = OrderedDict()
az_nuetd["Year"] = []
az_nuetd["Data"] = []
az_patcd = OrderedDict()
az_patcd["Year"] = []
az_patcd["Data"] = []
az_wwtcd = OrderedDict()
az_wwtcd["Year"] = []
az_wwtcd["Data"] = []

for i in range(len(az_price_data["MSN"])):
    if az_price_data["MSN"][i] == "CLTCD":
        az_cltcd["Year"].append(az_price_data["Year"][i])
        az_cltcd["Data"].append(az_price_data["Data"][i])
    elif az_price_data["MSN"][i] == "ESTCD":
        az_estcd["Year"].append(az_price_data["Year"][i])
        az_estcd["Data"].append(az_price_data["Data"][i])
    elif az_price_data["MSN"][i] == "NGTCD":
        az_ngtcd["Year"].append(az_price_data["Year"][i])
        az_ngtcd["Data"].append(az_price_data["Data"][i])
    elif az_price_data["MSN"][i] == "NUETD":
        az_nuetd["Year"].append(az_price_data["Year"][i])
        az_nuetd["Data"].append(az_price_data["Data"][i])
    elif az_price_data["MSN"][i] == "PATCD":
        az_patcd["Year"].append(az_price_data["Year"][i])
        az_patcd["Data"].append(az_price_data["Data"][i])
    elif az_price_data["MSN"][i] == "WWTCD":
        az_wwtcd["Year"].append(az_price_data["Year"][i])
        az_wwtcd["Data"].append(az_price_data["Data"][i])
    else:
        pass

az_cltcd_data = pd.DataFrame(az_cltcd)
az_cltcd_data.to_csv("data/csv/price_expenditures/energy_source/az/price/cltcd.csv",
                     index=False, index_label=False, sep=',')
az_estcd_data = pd.DataFrame(az_estcd)
az_estcd_data.to_csv("data/csv/price_expenditures/energy_source/az/price/estcd.csv",
                     index=False, index_label=False, sep=',')
az_ngtcd_data = pd.DataFrame(az_ngtcd)
az_ngtcd_data.to_csv("data/csv/price_expenditures/energy_source/az/price/ngtcd.csv",
                     index=False, index_label=False, sep=',')
az_nuetd_data = pd.DataFrame(az_nuetd)
az_nuetd_data.to_csv("data/csv/price_expenditures/energy_source/az/price/nuetd.csv",
                     index=False, index_label=False, sep=',')
az_patcd_data = pd.DataFrame(az_patcd)
az_patcd_data.to_csv("data/csv/price_expenditures/energy_source/az/price/patcd.csv",
                     index=False, index_label=False, sep=',')
az_wwtcd_data = pd.DataFrame(az_wwtcd)
az_wwtcd_data.to_csv("data/csv/price_expenditures/energy_source/az/price/wwtcd.csv",
                     index=False, index_label=False, sep=',')

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

ca_price_data.to_csv("data/csv/price_expenditures/energy_source/ca/ca_price.csv",
                   index=False, index_label=False, sep=',')
# print(ca_price_data)

ca_cltcd = OrderedDict()
ca_cltcd["Year"] = []
ca_cltcd["Data"] = []
ca_estcd = OrderedDict()
ca_estcd["Year"] = []
ca_estcd["Data"] = []
ca_ngtcd = OrderedDict()
ca_ngtcd["Year"] = []
ca_ngtcd["Data"] = []
ca_nuetd = OrderedDict()
ca_nuetd["Year"] = []
ca_nuetd["Data"] = []
ca_patcd = OrderedDict()
ca_patcd["Year"] = []
ca_patcd["Data"] = []
ca_wwtcd = OrderedDict()
ca_wwtcd["Year"] = []
ca_wwtcd["Data"] = []

for i in range(len(ca_price_data["MSN"])):
    if ca_price_data["MSN"][i] == "CLTCD":
        ca_cltcd["Year"].append(ca_price_data["Year"][i])
        ca_cltcd["Data"].append(ca_price_data["Data"][i])
    elif ca_price_data["MSN"][i] == "ESTCD":
        ca_estcd["Year"].append(ca_price_data["Year"][i])
        ca_estcd["Data"].append(ca_price_data["Data"][i])
    elif ca_price_data["MSN"][i] == "NGTCD":
        ca_ngtcd["Year"].append(ca_price_data["Year"][i])
        ca_ngtcd["Data"].append(ca_price_data["Data"][i])
    elif ca_price_data["MSN"][i] == "NUETD":
        ca_nuetd["Year"].append(ca_price_data["Year"][i])
        ca_nuetd["Data"].append(ca_price_data["Data"][i])
    elif ca_price_data["MSN"][i] == "PATCD":
        ca_patcd["Year"].append(ca_price_data["Year"][i])
        ca_patcd["Data"].append(ca_price_data["Data"][i])
    elif ca_price_data["MSN"][i] == "WWTCD":
        ca_wwtcd["Year"].append(ca_price_data["Year"][i])
        ca_wwtcd["Data"].append(ca_price_data["Data"][i])
    else:
        pass

ca_cltcd_data = pd.DataFrame(ca_cltcd)
ca_cltcd_data.to_csv("data/csv/price_expenditures/energy_source/ca/price/cltcd.csv",
                     index=False, index_label=False, sep=',')
ca_estcd_data = pd.DataFrame(ca_estcd)
ca_estcd_data.to_csv("data/csv/price_expenditures/energy_source/ca/price/estcd.csv",
                     index=False, index_label=False, sep=',')
ca_ngtcd_data = pd.DataFrame(ca_ngtcd)
ca_ngtcd_data.to_csv("data/csv/price_expenditures/energy_source/ca/price/ngtcd.csv",
                     index=False, index_label=False, sep=',')
ca_nuetd_data = pd.DataFrame(ca_nuetd)
ca_nuetd_data.to_csv("data/csv/price_expenditures/energy_source/ca/price/nuetd.csv",
                     index=False, index_label=False, sep=',')
ca_patcd_data = pd.DataFrame(ca_patcd)
ca_patcd_data.to_csv("data/csv/price_expenditures/energy_source/ca/price/patcd.csv",
                     index=False, index_label=False, sep=',')
ca_wwtcd_data = pd.DataFrame(ca_wwtcd)
ca_wwtcd_data.to_csv("data/csv/price_expenditures/energy_source/ca/price/wwtcd.csv",
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

nm_price_data.to_csv("data/csv/price_expenditures/energy_source/nm/nm_price.csv",
                   index=False, index_label=False, sep=',')
# print(nm_price_data)

nm_cltcd = OrderedDict()
nm_cltcd["Year"] = []
nm_cltcd["Data"] = []
nm_estcd = OrderedDict()
nm_estcd["Year"] = []
nm_estcd["Data"] = []
nm_ngtcd = OrderedDict()
nm_ngtcd["Year"] = []
nm_ngtcd["Data"] = []
nm_nuetd = OrderedDict()
nm_nuetd["Year"] = []
nm_nuetd["Data"] = []
nm_patcd = OrderedDict()
nm_patcd["Year"] = []
nm_patcd["Data"] = []
nm_wwtcd = OrderedDict()
nm_wwtcd["Year"] = []
nm_wwtcd["Data"] = []

for i in range(len(nm_price_data["MSN"])):
    if nm_price_data["MSN"][i] == "CLTCD":
        nm_cltcd["Year"].append(nm_price_data["Year"][i])
        nm_cltcd["Data"].append(nm_price_data["Data"][i])
    elif nm_price_data["MSN"][i] == "ESTCD":
        nm_estcd["Year"].append(nm_price_data["Year"][i])
        nm_estcd["Data"].append(nm_price_data["Data"][i])
    elif nm_price_data["MSN"][i] == "NGTCD":
        nm_ngtcd["Year"].append(nm_price_data["Year"][i])
        nm_ngtcd["Data"].append(nm_price_data["Data"][i])
    elif nm_price_data["MSN"][i] == "NUETD":
        nm_nuetd["Year"].append(nm_price_data["Year"][i])
        nm_nuetd["Data"].append(nm_price_data["Data"][i])
    elif nm_price_data["MSN"][i] == "PATCD":
        nm_patcd["Year"].append(nm_price_data["Year"][i])
        nm_patcd["Data"].append(nm_price_data["Data"][i])
    elif nm_price_data["MSN"][i] == "WWTCD":
        nm_wwtcd["Year"].append(nm_price_data["Year"][i])
        nm_wwtcd["Data"].append(nm_price_data["Data"][i])
    else:
        pass

nm_cltcd_data = pd.DataFrame(nm_cltcd)
nm_cltcd_data.to_csv("data/csv/price_expenditures/energy_source/nm/price/cltcd.csv",
                     index=False, index_label=False, sep=',')
nm_estcd_data = pd.DataFrame(nm_estcd)
nm_estcd_data.to_csv("data/csv/price_expenditures/energy_source/nm/price/estcd.csv",
                     index=False, index_label=False, sep=',')
nm_ngtcd_data = pd.DataFrame(nm_ngtcd)
nm_ngtcd_data.to_csv("data/csv/price_expenditures/energy_source/nm/price/ngtcd.csv",
                     index=False, index_label=False, sep=',')
nm_nuetd_data = pd.DataFrame(nm_nuetd)
nm_nuetd_data.to_csv("data/csv/price_expenditures/energy_source/nm/price/nuetd.csv",
                     index=False, index_label=False, sep=',')
nm_patcd_data = pd.DataFrame(nm_patcd)
nm_patcd_data.to_csv("data/csv/price_expenditures/energy_source/nm/price/patcd.csv",
                     index=False, index_label=False, sep=',')
nm_wwtcd_data = pd.DataFrame(nm_wwtcd)
nm_wwtcd_data.to_csv("data/csv/price_expenditures/energy_source/nm/price/wwtcd.csv",
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

tx_price_data.to_csv("data/csv/price_expenditures/energy_source/tx/tx_price.csv",
                   index=False, index_label=False, sep=',')
# print(tx_price_data)

tx_cltcd = OrderedDict()
tx_cltcd["Year"] = []
tx_cltcd["Data"] = []
tx_estcd = OrderedDict()
tx_estcd["Year"] = []
tx_estcd["Data"] = []
tx_ngtcd = OrderedDict()
tx_ngtcd["Year"] = []
tx_ngtcd["Data"] = []
tx_nuetd = OrderedDict()
tx_nuetd["Year"] = []
tx_nuetd["Data"] = []
tx_patcd = OrderedDict()
tx_patcd["Year"] = []
tx_patcd["Data"] = []
tx_wwtcd = OrderedDict()
tx_wwtcd["Year"] = []
tx_wwtcd["Data"] = []

for i in range(len(tx_price_data["MSN"])):
    if tx_price_data["MSN"][i] == "CLTCD":
        tx_cltcd["Year"].append(tx_price_data["Year"][i])
        tx_cltcd["Data"].append(tx_price_data["Data"][i])
    elif tx_price_data["MSN"][i] == "ESTCD":
        tx_estcd["Year"].append(tx_price_data["Year"][i])
        tx_estcd["Data"].append(tx_price_data["Data"][i])
    elif tx_price_data["MSN"][i] == "NGTCD":
        tx_ngtcd["Year"].append(tx_price_data["Year"][i])
        tx_ngtcd["Data"].append(tx_price_data["Data"][i])
    elif tx_price_data["MSN"][i] == "NUETD":
        tx_nuetd["Year"].append(tx_price_data["Year"][i])
        tx_nuetd["Data"].append(tx_price_data["Data"][i])
    elif tx_price_data["MSN"][i] == "PATCD":
        tx_patcd["Year"].append(tx_price_data["Year"][i])
        tx_patcd["Data"].append(tx_price_data["Data"][i])
    elif tx_price_data["MSN"][i] == "WWTCD":
        tx_wwtcd["Year"].append(tx_price_data["Year"][i])
        tx_wwtcd["Data"].append(tx_price_data["Data"][i])
    else:
        pass

tx_cltcd_data = pd.DataFrame(tx_cltcd)
tx_cltcd_data.to_csv("data/csv/price_expenditures/energy_source/tx/price/cltcd.csv",
                     index=False, index_label=False, sep=',')
tx_estcd_data = pd.DataFrame(tx_estcd)
tx_estcd_data.to_csv("data/csv/price_expenditures/energy_source/tx/price/estcd.csv",
                     index=False, index_label=False, sep=',')
tx_ngtcd_data = pd.DataFrame(tx_ngtcd)
tx_ngtcd_data.to_csv("data/csv/price_expenditures/energy_source/tx/price/ngtcd.csv",
                     index=False, index_label=False, sep=',')
tx_nuetd_data = pd.DataFrame(tx_nuetd)
tx_nuetd_data.to_csv("data/csv/price_expenditures/energy_source/tx/price/nuetd.csv",
                     index=False, index_label=False, sep=',')
tx_patcd_data = pd.DataFrame(tx_patcd)
tx_patcd_data.to_csv("data/csv/price_expenditures/energy_source/tx/price/patcd.csv",
                     index=False, index_label=False, sep=',')
tx_wwtcd_data = pd.DataFrame(tx_wwtcd)
tx_wwtcd_data.to_csv("data/csv/price_expenditures/energy_source/tx/price/wwtcd.csv",
                     index=False, index_label=False, sep=',')
