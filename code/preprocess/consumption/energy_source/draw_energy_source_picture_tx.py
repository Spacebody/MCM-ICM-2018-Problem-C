import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


tx_data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\data\\csv\\tx_data.csv", skiprows=None, engine='c', low_memory=True)
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
fig = plt.figure(figsize=(10, 5))
plt.title("Energy Source Total Consumption of Texas")
plt.xlabel("Year")
plt.ylabel("Data/Billion Btu")
sns.set_style("whitegrid")
plt.plot(tx_CLTCB_year, tx_CLTCB_data,  label="Coal")
plt.plot(tx_NNTCB_year, tx_NNTCB_data,  label="Natural gas")
plt.plot(tx_PATCB_year, tx_PATCB_data,  label="Petroleum products")
plt.plot(tx_RETCB_year, tx_RETCB_data,  label="Renewable energy")
plt.legend(loc='upper left')
plt.savefig("Energy_Source_Texas.png")
plt.savefig("Energy_Source_Texas.pdf")
