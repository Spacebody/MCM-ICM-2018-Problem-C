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
h_energy_source = []
for i in range(len(az_RETCB_year)):
    all_sum = az_CLTCB_data[i]+az_RETCB_data[i]+az_PATCB_data[i]+az_NNTCB_data[i]+az_WWTCB_data[i]
    s1 = az_CLTCB_data[i]/all_sum
    s2 = az_RETCB_data[i]/all_sum
    s3 = az_PATCB_data[i]/all_sum
    s4 = az_NNTCB_data[i]/all_sum
    s5 = az_WWTCB_data[i]/all_sum
    hi = -s1*np.log(s1)-s2*np.log(s2)-s3*np.log(s3)-s4*np.log(s4)-s5*np.log(s5)
    h_energy_source.append(hi)
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Shannon-Weiner Index of Total Energy Consumption(Energy Source) of Arizona")
plt.xlabel("Year")
plt.ylabel("H'")
plt.plot(az_CLTCB_year, h_energy_source)
plt.savefig("code/preprocess/consumption/energy_source/figures/H_Energy_Source_Arizona.png")
plt.savefig("code/preprocess/consumption/energy_source/figures/H_Energy_Source_Arizona.pdf")
