import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


ca_data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\data\\csv\\ca_data.csv", skiprows=None, engine='c', low_memory=True)
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
fig = plt.figure(figsize=(10, 5))
plt.title("Energy Source Total Consumption of California")
plt.xlabel("Year")
plt.ylabel("Data/Billion Btu")
sns.set_style("whitegrid")
plt.plot(ca_CLTCB_year, ca_CLTCB_data,  label="Coal")
plt.plot(ca_NNTCB_year, ca_NNTCB_data,  label="Natural gas")
plt.plot(ca_PATCB_year, ca_PATCB_data,  label="Petroleum products")
plt.plot(ca_RETCB_year, ca_RETCB_data,  label="Renewable energy")
plt.legend(loc='upper left')
plt.savefig("Energy_Source_California.png")
plt.savefig("Energy_Source_California.pdf")
