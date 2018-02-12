import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


az_data = pd.read_csv("data/csv/state_data/az_data.csv",
                      skiprows=None, engine='c', low_memory=True)
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
az_h_energy_source = []
for i in range(len(az_RETCB_year)):
    all_sum = az_CLTCB_data[i]+az_RETCB_data[i] + \
        az_PATCB_data[i]+az_NNTCB_data[i]+az_WWTCB_data[i]
    s1 = az_CLTCB_data[i]/all_sum
    s2 = az_RETCB_data[i]/all_sum
    s3 = az_PATCB_data[i]/all_sum
    s4 = az_NNTCB_data[i]/all_sum
    s5 = az_WWTCB_data[i]/all_sum
    az_hi = -s1*np.log(s1)-s2*np.log(s2)-s3*np.log(s3)-s4*np.log(s4)-s5*np.log(s5)
    az_h_energy_source.append(az_hi)


ca_data = pd.read_csv("data/csv/state_data/ca_data.csv",
                      skiprows=None, engine='c', low_memory=True)
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
ca_h_energy_source = []
for i in range(len(ca_RETCB_year)):
    all_sum = ca_CLTCB_data[i]+ca_RETCB_data[i] + \
        ca_PATCB_data[i]+ca_NNTCB_data[i]+ca_WWTCB_data[i]
    s1 = ca_CLTCB_data[i]/all_sum
    s2 = ca_RETCB_data[i]/all_sum
    s3 = ca_PATCB_data[i]/all_sum
    s4 = ca_NNTCB_data[i]/all_sum
    s5 = ca_WWTCB_data[i]/all_sum
    ca_hi = -s1*np.log(s1)-s2*np.log(s2)-s3*np.log(s3)-s4*np.log(s4)-s5*np.log(s5)
    ca_h_energy_source.append(ca_hi)

nm_data = pd.read_csv("data/csv/state_data/nm_data.csv",
                      skiprows=None, engine='c', low_memory=True)
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
nm_h_energy_source = []
for i in range(len(nm_RETCB_year)):
    all_sum = nm_CLTCB_data[i]+nm_RETCB_data[i] + \
        nm_PATCB_data[i]+nm_NNTCB_data[i]+nm_WWTCB_data[i]
    s1 = nm_CLTCB_data[i]/all_sum
    s2 = nm_RETCB_data[i]/all_sum
    s3 = nm_PATCB_data[i]/all_sum
    s4 = nm_NNTCB_data[i]/all_sum
    s5 = nm_WWTCB_data[i]/all_sum
    nm_hi = -s1*np.log(s1)-s2*np.log(s2)-s3*np.log(s3)-s4*np.log(s4)-s5*np.log(s5)
    nm_h_energy_source.append(nm_hi)

tx_data = pd.read_csv("data/csv/state_data/tx_data.csv",
                      skiprows=None, engine='c', low_memory=True)
tx_CLTCB_year = []
tx_CLTCB_data = []
tx_NNTCB_year = []
tx_NNTCB_data = []
tx_PATCB_year = []
tx_PATCB_data = []
tx_RETCB_year = []
tx_RETCB_data = []
tx_WWTCB_year = []
tx_WWTCB_data = []
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
    if re.search("WWTCB", tx_data["MSN"][i]):
        tx_WWTCB_year.append(tx_data["Year"][i])
        tx_WWTCB_data.append(tx_data["Data"][i])
tx_h_energy_source = []
for i in range(len(tx_RETCB_year)):
    all_sum = tx_CLTCB_data[i]+tx_RETCB_data[i] + \
        tx_PATCB_data[i]+tx_NNTCB_data[i]+tx_WWTCB_data[i]
    s1 = tx_CLTCB_data[i]/all_sum
    s2 = tx_RETCB_data[i]/all_sum
    s3 = tx_PATCB_data[i]/all_sum
    s4 = tx_NNTCB_data[i]/all_sum
    s5 = tx_WWTCB_data[i]/all_sum
    tx_hi = -s1*np.log(s1)-s2*np.log(s2)-s3*np.log(s3)-s4*np.log(s4)-s5*np.log(s5)
    tx_h_energy_source.append(tx_hi)


sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Shannon-Weiner Index of Total Energy Consumption(Energy Source) of Four States")
plt.xlabel("Year")
plt.ylabel("H'")
plt.plot(az_CLTCB_year, az_h_energy_source, label="Arizona")
plt.plot(ca_CLTCB_year, ca_h_energy_source, label="California")
plt.plot(nm_CLTCB_year, nm_h_energy_source, label="New Mexico")
plt.plot(tx_CLTCB_year, tx_h_energy_source, label="Texas")
plt.legend(loc='best')
plt.savefig(
    "code/preprocess/consumption/energy_source/figures/H_Energy_Source.png")
plt.savefig(
    "code/preprocess/consumption/energy_source/figures/H_Energy_Source.pdf")




