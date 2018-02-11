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
from economy import az_tegds, ca_tegds, nm_tegds, tx_tegds

#plot
# az
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Energy expenditures as percent of current-dollar GDP of Arizona")
plt.xlabel("Year")
plt.ylabel("Data / Percent(%)")
plt.plot(az_tegds["Year"], az_tegds["Data"], label="Energy expenditures percent")
plt.legend(loc='best')
plt.savefig(
    "code/preprocess/economy/figures/Economy_Arizona.png")
plt.savefig(
    "code/preprocess/economy/figures/Economy_Arizona.pdf")
# plt.show()


# ca
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Energy expenditures as percent of current-dollar GDP of California")
plt.xlabel("Year")
plt.ylabel("Data / Percent(%)")
plt.plot(ca_tegds["Year"], ca_tegds["Data"], label="Energy expenditures percent")
plt.legend(loc='best')
plt.savefig(
    "code/preprocess/economy/figures/Economy_California.png")
plt.savefig(
    "code/preprocess/economy/figures/Economy_California.pdf")
# plt.show()

# nm
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Energy expenditures as percent of current-dollar GDP of New Mexico")
plt.xlabel("Year")
plt.ylabel("Data / Percent(%)")
plt.plot(nm_tegds["Year"], nm_tegds["Data"], label="Energy expenditures percent")
plt.legend(loc='best')
plt.savefig(
    "code/preprocess/economy/figures/Economy_New_Mexico.png")
plt.savefig(
    "code/preprocess/economy/figures/Economy_New_Mexico.pdf")
# plt.show()

# tx
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Energy expenditures as percent of current-dollar GDP of Texas")
plt.xlabel("Year")
plt.ylabel("Data / Percent(%)")
plt.plot(tx_tegds["Year"], tx_tegds["Data"], label="Energy expenditures percent")
plt.legend(loc='best')
plt.savefig(
    "code/preprocess/economy/figures/Economy_Texas.png")
plt.savefig(
    "code/preprocess/economy/figures/Economy_Texas.pdf")
# plt.show()
