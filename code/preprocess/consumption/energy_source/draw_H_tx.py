import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


tx_data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\data\\csv\\consumption\\state_data\\tx_data.csv", skiprows=None, engine='c', low_memory=True)
tx_CLTCB_year = []
tx_CLTCB_data = []
tx_NNTCB_year = []
tx_NNTCB_data = []
tx_PATCB_year = []
tx_PATCB_data = []
tx_RETCB_year = []
tx_RETCB_data = []
for i in range(len(tx_data["MSN"])):
    if re.search("CLTCB", tx_data["MSN"][i]):
        tx_CLTCB_year.append(tx_data["Year"][i])
        tx_CLTCB_data.append(tx_data["Data"][i])
    if re.search("NNTCB", tx_data["MSN"][i]):
        tx_NNTCB_year.append(tx_data["Year"][i])
        tx_NNTCB_data.append(tx_data["Data"][i])
    if re.search("PATCB", tx_data["MSN"][i]):
        tx_PATCB_year.append(tx_data["Year"][i])
        tx_PATCB_data.append(tx_data["Data"][i])
    if re.search("RETCB", tx_data["MSN"][i]):
        tx_RETCB_year.append(tx_data["Year"][i])
        tx_RETCB_data.append(tx_data["Data"][i])

h_energy_source = []
for i in range(len(tx_RETCB_year)):
    all_sum = tx_CLTCB_data[i]+tx_RETCB_data[i]+tx_PATCB_data[i]+tx_NNTCB_data[i]
    s1 = tx_CLTCB_data[i]/all_sum
    s2 = tx_RETCB_data[i]/all_sum
    s3 = tx_PATCB_data[i]/all_sum
    s4 = tx_NNTCB_data[i]/all_sum
    hi = -s1*np.log(s1)-s2*np.log(s2)-s3*np.log(s3)-s4*np.log(s4)
    h_energy_source.append(hi)

fig = plt.figure(figsize=(10, 5))
plt.title("Shannon-Weiner Index of Energy Source Total Consumption of Texas")
plt.xlabel("Year")
plt.ylabel("H'")
sns.set_style("whitegrid")
plt.plot(tx_CLTCB_year, h_energy_source)
plt.savefig("H_Energy_Source_Texas.png")
plt.savefig("H_Energy_Source_Texas.pdf")
