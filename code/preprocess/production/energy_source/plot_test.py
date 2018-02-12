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
# plt.plot(az_clprb["Year"], az_clprb["Data"], label="Coal")
# plt.plot(az_paprb["Year"], az_paprb["Data"], label="Crude oil")
# plt.plot(az_ngmpb["Year"], az_ngmpb["Data"], label="Natural gas")
# plt.plot(az_reprb["Year"], az_reprb["Data"], label="Renewable")
# plt.plot(az_teprb["Year"], az_teprb["Data"], label="Total Energy")
plt.plot(az_teprb["Year"], az_teprb["Data"]/np.max(az_teprb["Data"]), linestyle='dashed', label="Total Energy(log)")
plt.legend(loc='best')
plt.savefig(
    "code/preprocess/production/energy_source/test/Production_Arizona.png")
plt.savefig(
    "code/preprocess/production/energy_source/test/Production_Arizona.pdf")
# plt.show()
