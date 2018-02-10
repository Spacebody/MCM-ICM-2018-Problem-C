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
from price_data import az_teacd_data, az_teccd_data, az_teicd_data, az_tercd_data, \
    ca_teacd_data, ca_teccd_data, ca_teicd_data, ca_tercd_data, \
    nm_teacd_data, nm_teccd_data, nm_teicd_data, nm_tercd_data, \
    tx_teacd_data, tx_teccd_data, tx_teicd_data, tx_tercd_data

#plot
# az
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Energy Average Price(Sectors) of Arizona")
plt.xlabel("Year")
plt.ylabel("Data / Dollars per million Btu")
plt.plot(az_teacd_data["Year"], az_teacd_data["Data"], label="Transportation")
plt.plot(az_teccd_data["Year"], az_teccd_data["Data"], label="Commercial")
plt.plot(az_teicd_data["Year"], az_teicd_data["Data"], label="Industrial")
plt.plot(az_tercd_data["Year"], az_tercd_data["Data"], label="Residential")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/price/sector/figures/Sectors_Arizona.png")
plt.savefig(
    "code/preprocess/price_expenditures/price/sector/figures/Sectors_Arizona.pdf")
# plt.show()

# ca
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Energy Average Price(Sectors) of California")
plt.xlabel("Year")
plt.ylabel("Data / Dollars per million Btu")
plt.plot(ca_teacd_data["Year"], ca_teacd_data["Data"], label="Transportation")
plt.plot(ca_teccd_data["Year"], ca_teccd_data["Data"], label="Commercial")
plt.plot(ca_teicd_data["Year"], ca_teicd_data["Data"], label="Industrial")
plt.plot(ca_tercd_data["Year"], ca_tercd_data["Data"], label="Residential")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/price/sector/figures/Sectors_California.png")
plt.savefig(
    "code/preprocess/price_expenditures/price/sector/figures/Sectors_California.pdf")
# plt.show()

# nm
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Energy Average Price(Sectors) of New Mexico")
plt.xlabel("Year")
plt.ylabel("Data / Dollars per million Btu")
plt.plot(nm_teacd_data["Year"], nm_teacd_data["Data"], label="Transportation")
plt.plot(nm_teccd_data["Year"], nm_teccd_data["Data"], label="Commercial")
plt.plot(nm_teicd_data["Year"], nm_teicd_data["Data"], label="Industrial")
plt.plot(nm_tercd_data["Year"], nm_tercd_data["Data"], label="Residential")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/price/sector/figures/Sectors_New_Mexico.png")
plt.savefig(
    "code/preprocess/price_expenditures/price/sector/figures/Sectors_New_Mexico.pdf")
# plt.show()

# tx
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Energy Average Price(Sectors) of Texas")
plt.xlabel("Year")
plt.ylabel("Data / Dollars per million Btu")
plt.plot(tx_teacd_data["Year"], tx_teacd_data["Data"], label="Transportation")
plt.plot(tx_teccd_data["Year"], tx_teccd_data["Data"], label="Commercial")
plt.plot(tx_teicd_data["Year"], tx_teicd_data["Data"], label="Industrial")
plt.plot(tx_tercd_data["Year"], tx_tercd_data["Data"], label="Residential")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/price/sector/figures/Sectors_Texas.png")
plt.savefig(
    "code/preprocess/price_expenditures/price/sector/figures/Sectors_Texas.pdf")
# plt.show()
