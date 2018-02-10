import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


nm_data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\data\\csv\\consumption\\state_data\\nm_data.csv", skiprows=None, engine='c', low_memory=True)
nm_CLTCB_year = []
nm_CLTCB_data = []
nm_NNTCB_year = []
nm_NNTCB_data = []
nm_PATCB_year = []
nm_PATCB_data = []
nm_RETCB_year = []
nm_RETCB_data = []
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

h_energy_source = []
for i in range(len(nm_RETCB_year)):
    all_sum = nm_CLTCB_data[i]+nm_RETCB_data[i]+nm_PATCB_data[i]+nm_NNTCB_data[i]
    s1 = nm_CLTCB_data[i]/all_sum
    s2 = nm_RETCB_data[i]/all_sum
    s3 = nm_PATCB_data[i]/all_sum
    s4 = nm_NNTCB_data[i]/all_sum
    hi = -s1*np.log(s1)-s2*np.log(s2)-s3*np.log(s3)-s4*np.log(s4)
    h_energy_source.append(hi)

fig = plt.figure(figsize=(10, 5))
plt.title("Shannon-Weiner Index of Energy Source Total Consumption of New Mexico")
plt.xlabel("Year")
plt.ylabel("H'")
sns.set_style("whitegrid")
plt.plot(nm_CLTCB_year, h_energy_source)
plt.savefig("H_Energy_Source_New_Mexico.png")
plt.savefig("H_Energy_Source_New_Mexico.pdf")
