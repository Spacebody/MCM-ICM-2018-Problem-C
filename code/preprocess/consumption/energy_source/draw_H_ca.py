import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


ca_data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\data\\csv\\consumption\\state_data\\ca_data.csv", skiprows=None, engine='c', low_memory=True)
ca_CLTCB_year = []
ca_CLTCB_data = []
ca_NNTCB_year = []
ca_NNTCB_data = []
ca_PATCB_year = []
ca_PATCB_data = []
ca_RETCB_year = []
ca_RETCB_data = []
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

h_energy_source = []
for i in range(len(ca_RETCB_year)):
    all_sum = ca_CLTCB_data[i]+ca_RETCB_data[i]+ca_PATCB_data[i]+ca_NNTCB_data[i]
    s1 = ca_CLTCB_data[i]/all_sum
    s2 = ca_RETCB_data[i]/all_sum
    s3 = ca_PATCB_data[i]/all_sum
    s4 = ca_NNTCB_data[i]/all_sum
    hi = -s1*np.log(s1)-s2*np.log(s2)-s3*np.log(s3)-s4*np.log(s4)
    h_energy_source.append(hi)

fig = plt.figure(figsize=(10, 5))
plt.title("Shannon-Weiner Index of Energy Source Total Consumption of California")
plt.xlabel("Year")
plt.ylabel("H'")
sns.set_style("whitegrid")
plt.plot(ca_CLTCB_year, h_energy_source)
plt.savefig("H_Energy_Source_California.png")
plt.savefig("H_Energy_Source_California.pdf")
