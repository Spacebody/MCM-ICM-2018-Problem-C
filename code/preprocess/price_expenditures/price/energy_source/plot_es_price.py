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
from price_es_data import az_cltcd_data, az_estcd_data, az_ngtcd_data, az_nuetd_data, az_patcd_data, az_wwtcd_data, \
    ca_cltcd_data, ca_estcd_data, ca_ngtcd_data, ca_nuetd_data, ca_patcd_data, ca_wwtcd_data, \
    nm_cltcd_data, nm_estcd_data, nm_ngtcd_data, nm_nuetd_data, nm_patcd_data, nm_wwtcd_data, \
    tx_cltcd_data, tx_estcd_data, tx_ngtcd_data, tx_nuetd_data, tx_patcd_data, tx_wwtcd_data

#plot
# az
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Average Price by Energy Source of Arizona")
plt.xlabel("Year")
plt.ylabel("Data/Dollars per million Btu")
plt.plot(az_cltcd_data["Year"], az_cltcd_data["Data"], label="Coal")
plt.plot(az_estcd_data["Year"], az_estcd_data["Data"], label="Electricity")
plt.plot(az_ngtcd_data["Year"], az_ngtcd_data["Data"], label="Natural gas")
plt.plot(az_nuetd_data["Year"], az_nuetd_data["Data"], label="Nuclear")
plt.plot(az_patcd_data["Year"], az_patcd_data["Data"], label="Petroleum products")
plt.plot(az_wwtcd_data["Year"], az_wwtcd_data["Data"], label="Wood and Waste")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/price/energy_source/figures/Energy_Source_Arizona.png")
plt.savefig(
    "code/preprocess/price_expenditures/price/energy_source/figures/Energy_Source_Arizona.pdf")
# plt.show()

# ca
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Energy Average Price by Energy Source of California")
plt.xlabel("Year")
plt.ylabel("Data/Dollars per million Btu")
plt.plot(ca_cltcd_data["Year"], ca_cltcd_data["Data"], label="Coal")
plt.plot(ca_estcd_data["Year"], ca_estcd_data["Data"], label="Electricity")
plt.plot(ca_ngtcd_data["Year"], ca_ngtcd_data["Data"], label="Natural gas")
plt.plot(ca_nuetd_data["Year"], ca_nuetd_data["Data"], label="Nuclear")
plt.plot(ca_patcd_data["Year"], ca_patcd_data["Data"], label="Petroleum products")
plt.plot(ca_wwtcd_data["Year"], ca_wwtcd_data["Data"], label="Wood and Waste")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/price/energy_source/figures/Energy_Source_California.png")
plt.savefig(
    "code/preprocess/price_expenditures/price/energy_source/figures/Energy_Source_California.pdf")
# plt.show()

# nm
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Energy Average Price by Energy Source of New Mexico")
plt.xlabel("Year")
plt.ylabel("Data/Dollars per million Btu")
plt.plot(nm_cltcd_data["Year"], nm_cltcd_data["Data"], label="Coal")
plt.plot(nm_estcd_data["Year"], nm_estcd_data["Data"], label="Electricity")
plt.plot(nm_ngtcd_data["Year"], nm_ngtcd_data["Data"], label="Natural gas")
plt.plot(nm_nuetd_data["Year"], nm_nuetd_data["Data"], label="Nuclear")
plt.plot(nm_patcd_data["Year"], nm_patcd_data["Data"], label="Petroleum products")
plt.plot(nm_wwtcd_data["Year"], nm_wwtcd_data["Data"], label="Wood and Waste")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/price/energy_source/figures/Energy_Source_New_Mexico.png")
plt.savefig(
    "code/preprocess/price_expenditures/price/energy_source/figures/Energy_Source_New_Mexico.pdf")
# plt.show()

# tx
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Energy Average Price by Energy Source of Texas")
plt.xlabel("Year")
plt.ylabel("Data/Dollars per million Btu")
plt.plot(tx_cltcd_data["Year"], tx_cltcd_data["Data"], label="Coal")
plt.plot(tx_estcd_data["Year"], tx_estcd_data["Data"], label="Electricity")
plt.plot(tx_ngtcd_data["Year"], tx_ngtcd_data["Data"], label="Natural gas")
plt.plot(tx_nuetd_data["Year"], tx_nuetd_data["Data"], label="Nuclear")
plt.plot(tx_patcd_data["Year"], tx_patcd_data["Data"], label="Petroleum products")
plt.plot(tx_wwtcd_data["Year"], tx_wwtcd_data["Data"], label="Wood and Waste")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/price/energy_source/figures/Energy_Source_Texas.png")
plt.savefig(
    "code/preprocess/price_expenditures/price/energy_source/figures/Energy_Source_Texas.pdf")
# plt.show()
