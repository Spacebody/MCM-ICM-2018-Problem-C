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
from pop import az_tpopp, ca_tpopp, nm_tpopp, tx_tpopp

#plot
# az
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Resident population of Arizona")
plt.xlabel("Year")
plt.ylabel("Data / Thousand")
plt.plot(az_tpopp["Year"], az_tpopp["Data"], label="Population")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/population/figures/Population_Arizona.png")
plt.savefig(
    "code/preprocess/population/figures/Population_Arizona.pdf")
# plt.show()


# ca
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Resident population of California")
plt.xlabel("Year")
plt.ylabel("Data / Thousand")
plt.plot(ca_tpopp["Year"], ca_tpopp["Data"], label="Population")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/population/figures/Production_California.png")
plt.savefig(
    "code/preprocess/population/figures/Production_California.pdf")
# plt.show()

# nm
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Resident population of New Mexico")
plt.xlabel("Year")
plt.ylabel("Data / Thousand")
plt.plot(nm_tpopp["Year"], nm_tpopp["Data"], label="Population")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/population/figures/Production_New_Mexico.png")
plt.savefig(
    "code/preprocess/population/figures/Production_New_Mexico.pdf")
# plt.show()

# tx
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Resident population of Texas")
plt.xlabel("Year")
plt.ylabel("Data / Thousand")
plt.plot(tx_tpopp["Year"], tx_tpopp["Data"], label="Population")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/population/figures/Production_Texas.png")
plt.savefig(
    "code/preprocess/population/figures/Production_Texas.pdf")
# plt.show()



