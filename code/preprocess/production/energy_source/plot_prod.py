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
from prod import az_clprb, az_hytcb, az_paprb, az_ngmpb, az_reprb, az_teprb, \
    ca_clprb, ca_hytcb, ca_paprb, ca_ngmpb, ca_reprb, ca_teprb, \
    nm_clprb, nm_hytcb, nm_paprb, nm_ngmpb, nm_reprb, nm_teprb, \
    tx_clprb, tx_hytcb, tx_paprb, tx_ngmpb, tx_reprb, tx_teprb

#plot
# az
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Energy Production of Arizona")
plt.xlabel("Year")
plt.ylabel("Data / Billion Btu")
plt.plot(az_clprb["Year"], az_clprb["Data"], label="Coal")
plt.plot(az_paprb["Year"], az_paprb["Data"], label="Crude oil")
plt.plot(az_ngmpb["Year"], az_ngmpb["Data"], label="Natural gas")
plt.plot(az_reprb["Year"], az_reprb["Data"], label="Renewable")
plt.plot(az_teprb["Year"], az_teprb["Data"], linestyle='dashed', label="Total Energy")
plt.legend(loc='best')
plt.savefig("code/preprocess/production/energy_source/figures/Production_Arizona.png")
plt.savefig("code/preprocess/production/energy_source/figures/Production_Arizona.pdf")
# plt.show()


# ca
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Energy Production of California")
plt.xlabel("Year")
plt.ylabel("Data / Billion Btu")
plt.plot(ca_clprb["Year"], ca_clprb["Data"], label="Coal")
plt.plot(ca_paprb["Year"], ca_paprb["Data"], label="Crude oil")
plt.plot(ca_ngmpb["Year"], ca_ngmpb["Data"], label="Natural gas")
plt.plot(ca_reprb["Year"], ca_reprb["Data"], label="Renewable")
plt.plot(ca_teprb["Year"], ca_teprb["Data"], linestyle='dashed', label="Total Energy")
plt.legend(loc='upper left')
plt.savefig("code/preprocess/production/energy_source/figures/Production_California.png")
plt.savefig("code/preprocess/production/energy_source/figures/Production_California.pdf")
# plt.show()

# nm
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Energy Production of New Mexico")
plt.xlabel("Year")
plt.ylabel("Data / Billion Btu")
plt.plot(nm_clprb["Year"], nm_clprb["Data"], label="Coal")
plt.plot(nm_paprb["Year"], nm_paprb["Data"], label="Crude oil")
plt.plot(nm_ngmpb["Year"], nm_ngmpb["Data"], label="Natural gas")
plt.plot(nm_reprb["Year"], nm_reprb["Data"], label="Renewable")
plt.plot(nm_teprb["Year"], nm_teprb["Data"], linestyle='dashed', label="Total Energy")
plt.legend(loc='best')
plt.savefig("code/preprocess/production/energy_source/figures/Production_New_Mexico.png")
plt.savefig("code/preprocess/production/energy_source/figures/Production_New_Mexico.pdf")
# plt.show()

# tx
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Energy Production of Texas")
plt.xlabel("Year")
plt.ylabel("Data / Billion Btu")
plt.plot(tx_clprb["Year"], tx_clprb["Data"], label="Coal")
plt.plot(tx_paprb["Year"], tx_paprb["Data"], label="Crude oil")
plt.plot(tx_ngmpb["Year"], tx_ngmpb["Data"], label="Natural gas")
plt.plot(tx_reprb["Year"], tx_reprb["Data"], label="Renewable")
plt.plot(tx_teprb["Year"], tx_teprb["Data"], linestyle='dashed', label="Total Energy")
plt.legend(loc='best')
plt.savefig("code/preprocess/production/energy_source/figures/Production_Texas.png")
plt.savefig("code/preprocess/production/energy_source/figures/Production_Texas.pdf")
# plt.show()
