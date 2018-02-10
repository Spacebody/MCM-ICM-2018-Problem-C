import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


az_data = pd.read_csv("data/csv/state_data/az_data.csv", skiprows=None, engine='c', low_memory=True)
az_CLTCB_year = []
az_CLTCB_data = []
az_NNTCB_year = []
az_NNTCB_data = []
az_PATCB_year = []
az_PATCB_data = []
az_RETCB_year = []
az_RETCB_data = []
az_WWTCB_year = []
az_WWTCB_data = []
for i in range(len(az_data["MSN"])):
    if re.search("CLTCB", az_data["MSN"][i]):
        az_CLTCB_year.append(az_data["Year"][i])
        az_CLTCB_data.append(az_data["Data"][i])
    if re.search("NNTCB", az_data["MSN"][i]):
        az_NNTCB_year.append(az_data["Year"][i])
        az_NNTCB_data.append(az_data["Data"][i])
    if re.search("PATCB", az_data["MSN"][i]):
        az_PATCB_year.append(az_data["Year"][i])
        az_PATCB_data.append(az_data["Data"][i])
    if re.search("RETCB", az_data["MSN"][i]):
        az_RETCB_year.append(az_data["Year"][i])
        az_RETCB_data.append(az_data["Data"][i])
    if re.search("WWTCB", az_data["MSN"][i]):
        az_WWTCB_year.append(az_data["Year"][i])
        az_WWTCB_data.append(az_data["Data"][i])
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Consumption(Energy Source) of Arizona")
plt.xlabel("Year")
plt.ylabel("Data / Billion Btu")
plt.plot(az_CLTCB_year, az_CLTCB_data,  label="Coal")
plt.plot(az_NNTCB_year, az_NNTCB_data,  label="Natural gas")
plt.plot(az_PATCB_year, az_PATCB_data,  label="Petroleum products")
plt.plot(az_RETCB_year, az_RETCB_data,  label="Renewable energy")
plt.plot(az_WWTCB_year, az_WWTCB_data,  label="Wood and Waste")
plt.legend(loc='upper left')
plt.savefig("code/preprocess/consumption/energy_source/figures/Energy_Source_Arizona.png")
plt.savefig("code/preprocess/consumption/energy_source/figures/Energy_Source_Arizona.pdf")
