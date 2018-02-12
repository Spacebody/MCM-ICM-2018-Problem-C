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

# plot
sns.set_style("darkgrid")
fig = plt.figure(figsize=(7, 6))
plt.title("Resident population of Arizona")
plt.xlabel("Year")
plt.ylabel("Data / Thousand")
plt.plot(az_tpopp["Year"], az_tpopp["Data"], label="Arizona")
plt.plot(ca_tpopp["Year"], ca_tpopp["Data"], label="California")
plt.plot(nm_tpopp["Year"], nm_tpopp["Data"], label="New Mexico")
plt.plot(tx_tpopp["Year"], tx_tpopp["Data"], label="Texas")
plt.legend(loc='upper left')
plt.savefig(
    "code/preprocess/population/figures/Population.png")
plt.savefig(
    "code/preprocess/population/figures/Population.pdf")
# plt.show()
