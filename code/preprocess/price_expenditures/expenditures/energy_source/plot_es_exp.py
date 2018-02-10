#! usr/bin/python3

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
from exp_es_data import az_cltcv_data, az_estcv_data, az_ngtcv_data, az_nuetv_data, az_patcv_data, az_wwtcv_data, \
    ca_cltcv_data, ca_estcv_data, ca_ngtcv_data, ca_nuetv_data, ca_patcv_data, ca_wwtcv_data, \
    nm_cltcv_data, nm_estcv_data, nm_ngtcv_data, nm_nuetv_data, nm_patcv_data, nm_wwtcv_data, \
    tx_cltcv_data, tx_estcv_data, tx_ngtcv_data, tx_nuetv_data, tx_patcv_data, tx_wwtcv_data

#plot
# az
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Expenditures(Energy Source) of Arizona")
plt.xlabel("Year")
plt.ylabel("Data / Million dollars")
plt.plot(az_cltcv_data["Year"], az_cltcv_data["Data"], label="Coal")
plt.plot(az_estcv_data["Year"], az_estcv_data["Data"], label="Electricity")
plt.plot(az_ngtcv_data["Year"], az_ngtcv_data["Data"], label="Natural gas")
plt.plot(az_nuetv_data["Year"], az_nuetv_data["Data"], label="Nuclear")
plt.plot(az_patcv_data["Year"], az_patcv_data["Data"], label="Petroleum products")
plt.plot(az_wwtcv_data["Year"], az_wwtcv_data["Data"], label="Wood and Waste")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/expenditures/energy_source/figures/Energy_Source_Arizona.png")
plt.savefig(
    "code/preprocess/price_expenditures/expenditures/energy_source/figures/Energy_Source_Arizona.pdf")
# plt.show()

# ca
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Expenditures(Energy Source) of California")
plt.xlabel("Year")
plt.ylabel("Data / Million dollars")
plt.plot(ca_cltcv_data["Year"], ca_cltcv_data["Data"], label="Coal")
plt.plot(ca_estcv_data["Year"], ca_estcv_data["Data"], label="Electricity")
plt.plot(ca_ngtcv_data["Year"], ca_ngtcv_data["Data"], label="Natural gas")
plt.plot(ca_nuetv_data["Year"], ca_nuetv_data["Data"], label="Nuclear")
plt.plot(ca_patcv_data["Year"], ca_patcv_data["Data"], label="Petroleum products")
plt.plot(ca_wwtcv_data["Year"], ca_wwtcv_data["Data"], label="Wood and Waste")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/expenditures/energy_source/figures/Energy_Source_California.png")
plt.savefig(
    "code/preprocess/price_expenditures/expenditures/energy_source/figures/Energy_Source_California.pdf")
# plt.show()

# nm
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Expenditures(Energy Source) of New Mexico")
plt.xlabel("Year")
plt.ylabel("Data / Million dollars")
plt.plot(nm_cltcv_data["Year"], nm_cltcv_data["Data"], label="Coal")
plt.plot(nm_estcv_data["Year"], nm_estcv_data["Data"], label="Electricity")
plt.plot(nm_ngtcv_data["Year"], nm_ngtcv_data["Data"], label="Natural gas")
plt.plot(nm_nuetv_data["Year"], nm_nuetv_data["Data"], label="Nuclear")
plt.plot(nm_patcv_data["Year"], nm_patcv_data["Data"], label="Petroleum products")
plt.plot(nm_wwtcv_data["Year"], nm_wwtcv_data["Data"], label="Wood and Waste")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/expenditures/energy_source/figures/Energy_Source_New_Mexico.png")
plt.savefig(
    "code/preprocess/price_expenditures/expenditures/energy_source/figures/Energy_Source_New_Mexico.pdf")
# plt.show()

# tx
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Expenditures(Energy Source) of Texas")
plt.xlabel("Year")
plt.ylabel("Data / Million dollars")
plt.plot(tx_cltcv_data["Year"], tx_cltcv_data["Data"], label="Coal")
plt.plot(tx_estcv_data["Year"], tx_estcv_data["Data"], label="Electricity")
plt.plot(tx_ngtcv_data["Year"], tx_ngtcv_data["Data"], label="Natural gas")
plt.plot(tx_nuetv_data["Year"], tx_nuetv_data["Data"], label="Nuclear")
plt.plot(tx_patcv_data["Year"], tx_patcv_data["Data"], label="Petroleum products")
plt.plot(tx_wwtcv_data["Year"], tx_wwtcv_data["Data"], label="Wood and Waste")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/expenditures/energy_source/figures/Energy_Source_Texas.png")
plt.savefig(
    "code/preprocess/price_expenditures/expenditures/energy_source/figures/Energy_Source_Texas.pdf")
# plt.show()
