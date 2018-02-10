import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


nm_data = pd.read_csv("data/csv/state_data/nm_data.csv", skiprows=None, engine='c', low_memory=True)
nm_CLTCB_year = []
nm_CLTCB_data = []
nm_NNTCB_year = []
nm_NNTCB_data = []
nm_PATCB_year = []
nm_PATCB_data = []
nm_RETCB_year = []
nm_RETCB_data = []
nm_WWTCB_year = []
nm_WWTCB_data = []
for i in range(len(nm_data["MSN"])):
    if re.search("CLTCB", nm_data["MSN"][i]):
        nm_CLTCB_year.append(nm_data["Year"][i])
        nm_CLTCB_data.append(nm_data["Data"][i])
    if re.search("NNTCB", nm_data["MSN"][i]):
        nm_NNTCB_year.append(nm_data["Year"][i])
        nm_NNTCB_data.append(nm_data["Data"][i])
    if re.search("PATCB", nm_data["MSN"][i]):
        nm_PATCB_year.append(nm_data["Year"][i])
        nm_PATCB_data.append(nm_data["Data"][i])
    if re.search("RETCB", nm_data["MSN"][i]):
        nm_RETCB_year.append(nm_data["Year"][i])
        nm_RETCB_data.append(nm_data["Data"][i])
    if re.search("WWTCB", nm_data["MSN"][i]):
        nm_WWTCB_year.append(nm_data["Year"][i])
        nm_WWTCB_data.append(nm_data["Data"][i])
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Consumption(Energy Source) of New Mexico")
plt.xlabel("Year")
plt.ylabel("Data / Billion Btu")
plt.plot(nm_CLTCB_year, nm_CLTCB_data,  label="Coal")
plt.plot(nm_NNTCB_year, nm_NNTCB_data,  label="Natural gas")
plt.plot(nm_PATCB_year, nm_PATCB_data,  label="Petroleum products")
plt.plot(nm_RETCB_year, nm_RETCB_data,  label="Renewable energy")
plt.plot(nm_WWTCB_year, nm_WWTCB_data,  label="Wood and Waste")
plt.legend(loc='best')
plt.savefig("code/preprocess/consumption/energy_source/figures/Energy_Source_New_Mexico.png")
plt.savefig("code/preprocess/consumption/energy_source/figures/Energy_Source_New_Mexico.pdf")
