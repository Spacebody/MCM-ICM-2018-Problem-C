import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


ca_data = pd.read_csv("data/csv/state_data/ca_data.csv", skiprows=None, engine='c', low_memory=True)
ca_CLTCB_year = []
ca_CLTCB_data = []
ca_NNTCB_year = []
ca_NNTCB_data = []
ca_PATCB_year = []
ca_PATCB_data = []
ca_RETCB_year = []
ca_RETCB_data = []
ca_WWTCB_year = []
ca_WWTCB_data = []
for i in range(len(ca_data["MSN"])):
    if re.search("CLTCB", ca_data["MSN"][i]):
        ca_CLTCB_year.append(ca_data["Year"][i])
        ca_CLTCB_data.append(ca_data["Data"][i])
    if re.search("NNTCB", ca_data["MSN"][i]):
        ca_NNTCB_year.append(ca_data["Year"][i])
        ca_NNTCB_data.append(ca_data["Data"][i])
    if re.search("PATCB", ca_data["MSN"][i]):
        ca_PATCB_year.append(ca_data["Year"][i])
        ca_PATCB_data.append(ca_data["Data"][i])
    if re.search("RETCB", ca_data["MSN"][i]):
        ca_RETCB_year.append(ca_data["Year"][i])
        ca_RETCB_data.append(ca_data["Data"][i])
    if re.search("WWTCB", ca_data["MSN"][i]):
        ca_WWTCB_year.append(ca_data["Year"][i])
        ca_WWTCB_data.append(ca_data["Data"][i])
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Consumption(Energy Source) of California")
plt.xlabel("Year")
plt.ylabel("Data / Billion Btu")
plt.plot(ca_CLTCB_year, ca_CLTCB_data,  label="Coal")
plt.plot(ca_NNTCB_year, ca_NNTCB_data,  label="Natural gas")
plt.plot(ca_PATCB_year, ca_PATCB_data,  label="Petroleum products")
plt.plot(ca_RETCB_year, ca_RETCB_data,  label="Renewable energy")
plt.plot(ca_WWTCB_year, ca_WWTCB_data,  label="Wood and Waste")
plt.legend(loc='upper left')
plt.savefig("code/preprocess/consumption/energy_source/figures/Energy_Source_California.png")
plt.savefig("code/preprocess/consumption/energy_source/figures/Energy_Source_California.pdf")
