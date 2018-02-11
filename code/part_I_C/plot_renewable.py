import re
import numpy as np
import os
import sys
from collections import OrderedDict, defaultdict
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats, integrate
from renewable import az_reprb, az_retcb, az_roprb, az_tpopp, \
    ca_reprb, ca_retcb, ca_roprb, ca_tpopp, \
    nm_reprb, nm_retcb, nm_roprb, nm_tpopp, \
    tx_reprb, tx_retcb, tx_roprb, tx_tpopp

#plot

#reprb and roprb
sns.set_style("darkgrid")
fig = plt.figure(figsize=(7, 5))
ind = np.arange(4)    # the x locations for the groups
width = 0.3

p1 = plt.bar(ind, (az_reprb, ca_reprb, nm_reprb, tx_reprb), width)
p2 = plt.bar(ind+width, (az_roprb, ca_roprb, nm_roprb, tx_roprb), width)

plt.title("Renewable Energy Production of Four States")
plt.xlabel("States")
plt.ylabel("Data / Billion Btu")
plt.xticks(ind+0.5*width, ('Arizona', 'California', 'New Mexico', 'Taxes'))
plt.legend((p1[0], p2[0]), ('Include fuel ethanol', 'Exclude fuel ethanol'), loc='best')
plt.savefig("code/part_I_C/figures/production.png")
plt.savefig("code/part_I_C/figures/production.pdf")
# plt.show()

#retcb
sns.set_style("darkgrid")
fig = plt.figure(figsize=(7, 5))
ind = np.arange(4)    # the x locations for the groups
width = 0.3

p1 = plt.bar(ind, (az_retcb, ca_retcb, nm_retcb, tx_retcb), width)

plt.title("Renewable Energy Consumption of Four States")
plt.xlabel("States")
plt.ylabel("Data / Billion Btu")
plt.xticks(ind, ('Arizona', 'California', 'New Mexico', 'Taxes'))
plt.savefig("code/part_I_C/figures/consumption.png")
plt.savefig("code/part_I_C/figures/consumption.pdf")

#retcb/tpopp
sns.set_style("darkgrid")
fig = plt.figure(figsize=(7, 5))
ind = np.arange(4)    # the x locations for the groups
width = 0.3

p1 = plt.bar(ind, (az_retcb/az_tpopp, ca_retcb/ca_tpopp, nm_retcb/nm_tpopp, tx_retcb/tx_tpopp), width)

plt.title("Renewable Energy Consumption Per Capita of Four States")
plt.xlabel("States")
plt.ylabel("Data / Billion Btu/Thousand")
plt.xticks(ind, ('Arizona', 'California', 'New Mexico', 'Taxes'))
plt.savefig("code/part_I_C/figures/consumption_pop.png")
plt.savefig("code/part_I_C/figures/consumption_pop.pdf")

#reprb/tpopp
sns.set_style("darkgrid")
fig = plt.figure(figsize=(7, 5))
ind = np.arange(4)    # the x locations for the groups
width = 0.3

p1 = plt.bar(ind, (az_reprb/az_tpopp, ca_reprb/ca_tpopp, nm_reprb/nm_tpopp, tx_reprb/tx_tpopp), width)

plt.title("Renewable Energy Production Per Captita of Four States")
plt.xlabel("States")
plt.ylabel("Data / Billion Btu/Thousand")
plt.xticks(ind, ('Arizona', 'California', 'New Mexico', 'Taxes'))
plt.savefig("code/part_I_C/figures/production_pop.png")
plt.savefig("code/part_I_C/figures/production_pop.pdf")
# plt.show()
