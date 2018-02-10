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
from exp_data import az_teacv_data, az_teccv_data, az_teicv_data, az_tercv_data, \
                     ca_teacv_data, ca_teccv_data, ca_teicv_data, ca_tercv_data, \
                     nm_teacv_data, nm_teccv_data, nm_teicv_data, nm_tercv_data, \
                     tx_teacv_data, tx_teccv_data, tx_teicv_data, tx_tercv_data

#plot
# az
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Expenditures by Sectors of Arizona")
plt.xlabel("Year")
plt.ylabel("Data/Million dollars")
plt.plot(az_teacv_data["Year"], az_teacv_data["Data"],  label="Transportation")
plt.plot(az_teccv_data["Year"], az_teccv_data["Data"], label="Commercial")
plt.plot(az_teicv_data["Year"], az_teicv_data["Data"],  label="Industrial")
plt.plot(az_tercv_data["Year"], az_tercv_data["Data"],  label="Residential")
plt.legend(loc='upper left')
plt.savefig("code/preprocess/price_expenditures/expenditures/sector/figures/Sectors_Arizona.png")
plt.savefig("code/preprocess/price_expenditures/expenditures/sector/figures/Sectors_Arizona.pdf")
# plt.show()

# ca
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Expenditures by Sectors of California")
plt.xlabel("Year")
plt.ylabel("Data/Million dollars")
plt.plot(ca_teacv_data["Year"], ca_teacv_data["Data"],  label="Transportation")
plt.plot(ca_teccv_data["Year"], ca_teccv_data["Data"], label="Commercial")
plt.plot(ca_teicv_data["Year"], ca_teicv_data["Data"],  label="Industrial")
plt.plot(ca_tercv_data["Year"], ca_tercv_data["Data"],  label="Residential")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/expenditures/sector/figures/Sectors_California.png")
plt.savefig(
    "code/preprocess/price_expenditures/expenditures/sector/figures/Sectors_California.pdf")
# plt.show()

# nm
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Expenditures by Sectors of New Mexico")
plt.xlabel("Year")
plt.ylabel("Data/Million dollars")
plt.plot(nm_teacv_data["Year"], nm_teacv_data["Data"],  label="Transportation")
plt.plot(nm_teccv_data["Year"], nm_teccv_data["Data"], label="Commercial")
plt.plot(nm_teicv_data["Year"], nm_teicv_data["Data"],  label="Industrial")
plt.plot(nm_tercv_data["Year"], nm_tercv_data["Data"],  label="Residential")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/expenditures/sector/figures/Sectors_New_Mexico.png")
plt.savefig(
    "code/preprocess/price_expenditures/expenditures/sector/figures/Sectors_New_Mexico.pdf")
# plt.show()

# tx
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Expenditures by Sectors of Texas")
plt.xlabel("Year")
plt.ylabel("Data/Million dollars")
plt.plot(tx_teacv_data["Year"], tx_teacv_data["Data"],  label="Transportation")
plt.plot(tx_teccv_data["Year"], tx_teccv_data["Data"], label="Commercial")
plt.plot(tx_teicv_data["Year"], tx_teicv_data["Data"],  label="Industrial")
plt.plot(tx_tercv_data["Year"], tx_tercv_data["Data"],  label="Residential")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/price_expenditures/expenditures/sector/figures/Sectors_Texas.png")
plt.savefig(
    "code/preprocess/price_expenditures/expenditures/sector/figures/Sectors_Texas.pdf")
# plt.show()
