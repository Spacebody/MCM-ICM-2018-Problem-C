#! usr/bin/python3

import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict, defaultdict
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats, integrate
from prod import az_clprb, az_hytcb, az_paprb, az_ngmpb, az_reprb, \
    ca_clprb, ca_hytcb, ca_paprb, ca_ngmpb, ca_reprb,  \
    nm_clprb, nm_hytcb, nm_paprb, nm_ngmpb, nm_reprb,  \
    tx_clprb, tx_hytcb, tx_paprb, tx_ngmpb, tx_reprb
    
#calculate H  
az_h_energy_source = []
for i in range(len(az_clprb["Year"])):
    all_sum = az_clprb["Data"][i] + az_hytcb["Data"][i] + az_paprb["Data"][i] + az_ngmpb["Data"][i] + az_reprb["Data"][i]
    s1 = az_clprb["Data"][i]/all_sum
    s2 = az_hytcb["Data"][i]/all_sum
    s3 = az_paprb["Data"][i]/all_sum
    s4 = az_ngmpb["Data"][i]/all_sum
    s5 = az_reprb["Data"][i]/all_sum
    if s1 == 0.0:
        s1 = 1
    if s2 == 0.0:
        s2 = 1
    if s3 == 0.0:
        s3 = 1
    if s4 == 0.0:
        s4 = 1
    if s5 == 0.0:
        s5 = 1
    az_hi = -s1*np.log(s1)-s2*np.log(s2)-s3*np.log(s3)-s4*np.log(s4)-s5*np.log(s5)
    az_h_energy_source.append(az_hi)

ca_h_energy_source = []
for i in range(len(ca_clprb["Year"])):
    all_sum = ca_clprb["Data"][i] + ca_hytcb["Data"][i] + \
        ca_paprb["Data"][i] + ca_ngmpb["Data"][i] + ca_reprb["Data"][i]
    s1 = ca_clprb["Data"][i]/all_sum
    s2 = ca_hytcb["Data"][i]/all_sum
    s3 = ca_paprb["Data"][i]/all_sum
    s4 = ca_ngmpb["Data"][i]/all_sum
    s5 = ca_reprb["Data"][i]/all_sum
    if s1 == 0.0:
        s1 = 1
    if s2 == 0.0:
        s2 = 1
    if s3 == 0.0:
        s3 = 1
    if s4 == 0.0:
        s4 = 1
    if s5 == 0.0:
        s5 = 1
    ca_hi = -s1*np.log(s1)-s2*np.log(s2)-s3*np.log(s3) - s4*np.log(s4)-s5*np.log(s5)
    ca_h_energy_source.append(ca_hi)


nm_h_energy_source = []
for i in range(len(nm_clprb["Year"])):
    all_sum = nm_clprb["Data"][i] + nm_hytcb["Data"][i] + \
        nm_paprb["Data"][i] + nm_ngmpb["Data"][i] + nm_reprb["Data"][i]
    s1 = nm_clprb["Data"][i]/all_sum
    s2 = nm_hytcb["Data"][i]/all_sum
    s3 = nm_paprb["Data"][i]/all_sum
    s4 = nm_ngmpb["Data"][i]/all_sum
    s5 = nm_reprb["Data"][i]/all_sum
    if s1 == 0.0:
        s1 = 1
    if s2 == 0.0:
        s2 = 1
    if s3 == 0.0:
        s3 = 1
    if s4 == 0.0:
        s4 = 1
    if s5 == 0.0:
        s5 = 1
    nm_hi = -s1*np.log(s1)-s2*np.log(s2)-s3*np.log(s3) - \
        s4*np.log(s4)-s5*np.log(s5)
    nm_h_energy_source.append(nm_hi)

tx_h_energy_source = []
for i in range(len(tx_clprb["Year"])):
    all_sum = tx_clprb["Data"][i]+ tx_hytcb["Data"][i] + tx_paprb["Data"][i] + tx_ngmpb["Data"][i] + tx_reprb["Data"][i]
    s1 = tx_clprb["Data"][i]/all_sum
    s2 = tx_hytcb["Data"][i]/all_sum
    s3 = tx_paprb["Data"][i]/all_sum
    s4 = tx_ngmpb["Data"][i]/all_sum
    s5 = tx_reprb["Data"][i]/all_sum
    if s1 == 0.0:
        s1 = 1
    if s2 == 0.0:
        s2 = 1
    if s3 == 0.0:
        s3 = 1
    if s4 == 0.0:
        s4 = 1
    if s5 == 0.0:
        s5 = 1
    tx_hi = -s1*np.log(s1)-s2*np.log(s2)-s3*np.log(s3)-s4*np.log(s4)-s5*np.log(s5)
    tx_h_energy_source.append(tx_hi)

sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title(
    "Shannon-Weiner Index of Total Energy Production(Energy Source) of Four States")
plt.xlabel("Year")
plt.ylabel("H'")
plt.plot(az_clprb["Year"], az_h_energy_source, label="Arizona")
plt.plot(ca_clprb["Year"], ca_h_energy_source, label="California")
plt.plot(nm_clprb["Year"], nm_h_energy_source, label="New Mexico")
plt.plot(tx_clprb["Year"], tx_h_energy_source, label="Texas")
plt.legend(loc='best')
plt.savefig(
    "code/preprocess/production/energy_source/figures/H_Energy_Source.png")
plt.savefig(
    "code/preprocess/production/energy_source/figures/H_Energy_Source.pdf")

