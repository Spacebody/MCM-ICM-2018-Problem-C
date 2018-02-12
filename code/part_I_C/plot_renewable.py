import re
import numpy as np
import os
import sys
from collections import OrderedDict, defaultdict
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats, integrate
from renewable import az_reprb, az_retcb, az_roprb, az_tpopp, az_tetcb, az_teprb, \
    ca_reprb, ca_retcb, ca_roprb, ca_tpopp, ca_tetcb, ca_teprb, \
    nm_reprb, nm_retcb, nm_roprb, nm_tpopp, nm_tetcb, nm_teprb, \
    tx_reprb, tx_retcb, tx_roprb, tx_tpopp, tx_tetcb, tx_teprb

#plot

#reprb and roprb
# sns.set_style("darkgrid")
# fig = plt.figure(figsize=(7, 5))
# ind = np.arange(4)    # the x locations for the groups
# width = 0.3

# p1 = plt.bar(ind, (az_reprb, ca_reprb, nm_reprb, tx_reprb), width)
# p2 = plt.bar(ind+width, (az_roprb, ca_roprb, nm_roprb, tx_roprb), width)

# plt.title("Renewable Energy Production of Four States")
# plt.xlabel("States")
# plt.ylabel("Data / Billion Btu")
# plt.xticks(ind+0.5*width, ('Arizona', 'California', 'New Mexico', 'Taxes'))
# plt.legend((p1[0], p2[0]), ('Include fuel ethanol', 'Exclude fuel ethanol'), loc='best')
# plt.savefig("code/part_I_C/figures/production.png")
# plt.savefig("code/part_I_C/figures/production.pdf")
# # plt.show()

# #retcb
# sns.set_style("darkgrid")
# fig = plt.figure(figsize=(7, 5))
# ind = np.arange(4)    # the x locations for the groups
# width = 0.4

# p1 = plt.bar(ind, (az_retcb, ca_retcb, nm_retcb, tx_retcb), width)

# plt.title("Renewable Energy Consumption of Four States")
# plt.xlabel("States")
# plt.ylabel("Data / Billion Btu")
# plt.xticks(ind, ('Arizona', 'California', 'New Mexico', 'Taxes'))
# plt.savefig("code/part_I_C/figures/consumption.png")
# plt.savefig("code/part_I_C/figures/consumption.pdf")


t_az = 0.0
t_ca = 0.0
t_nm = 0.0
t_tx = 0.0

#retcb/tpopp
sns.set_style("darkgrid")
fig = plt.figure(figsize=(14, 10))
colors = ['#624ea7', 'g', 'r', 'b']
plt.subplot(2, 2, 1)
ind = np.arange(4)    # the x locations for the groups
width = 0.4
max_value = ca_retcb/ca_tpopp
p1 = plt.bar(ind, (az_retcb/az_tpopp/max_value, ca_retcb/ca_tpopp/max_value,
                   nm_retcb/nm_tpopp/max_value, tx_retcb/tx_tpopp/max_value), width, color=colors)

t_az += az_retcb/az_tpopp/max_value
t_ca += ca_retcb/ca_tpopp/max_value
t_nm += nm_retcb/nm_tpopp/max_value
t_tx += tx_retcb/tx_tpopp/max_value

plt.title("Renewable Energy Consumption Per Capita of Four States")
plt.xlabel("States")
plt.ylabel("Data / Score")
plt.xticks(ind, ('Arizona', 'California', 'New Mexico', 'Taxes'))
# plt.savefig("code/part_I_C/figures/consumption_pop.png")
# plt.savefig("code/part_I_C/figures/consumption_pop.pdf")

#reprb/tpopp
# sns.set_style("darkgrid")
# fig = plt.figure(figsize=(7, 5))
plt.subplot(2, 2, 2)
# ind = np.arange(4)    # the x locations for the groups
# width = 0.4
max_value = ca_reprb/ca_tpopp
p2 = plt.bar(ind, (az_reprb/az_tpopp/max_value, ca_reprb/ca_tpopp/max_value,
                   nm_reprb/nm_tpopp/max_value, tx_reprb/tx_tpopp/max_value), width, color=colors)

t_az += az_reprb/az_tpopp/max_value
t_ca += ca_reprb/ca_tpopp/max_value
t_nm += nm_reprb/nm_tpopp/max_value
t_tx += tx_reprb/tx_tpopp/max_value

plt.title("Renewable Energy Production Per Captita of Four States")
plt.xlabel("States")
plt.ylabel("Data / Score")
plt.xticks(ind, ('Arizona', 'California', 'New Mexico', 'Taxes'))
# plt.savefig("code/part_I_C/figures/production_pop.png")
# plt.savefig("code/part_I_C/figures/production_pop.pdf")
# plt.show()

# retcb/tetcb
# sns.set_style("darkgrid")
# fig = plt.figure(figsize=(7, 5))
plt.subplot(2, 2, 3)
# ind = np.arange(4)    # the x locations for the groups
# width = 0.4
max_value = ca_retcb/ca_tetcb*100
# p1 = plt.bar(ind, (100, 100, 100, 100), width)
p3 = plt.bar(ind, (az_retcb/az_tetcb*100/max_value, ca_retcb/ca_tetcb*100/max_value,
                   nm_retcb/nm_tetcb*100/max_value, tx_retcb/tx_tetcb*100/max_value), width, color=colors)

t_az += az_retcb/az_tetcb*100/max_value
t_ca += ca_retcb/ca_tetcb*100/max_value
t_nm += nm_retcb/nm_tetcb*100/max_value
t_tx += tx_retcb/tx_tetcb*100/max_value

plt.title("Renewable Energy Consumption Percentage of Four States")
plt.xlabel("States")
plt.ylabel("Data / Score")
plt.xticks(ind, ('Arizona', 'California', 'New Mexico', 'Taxes'))
# plt.savefig("code/part_I_C/figures/consumption_per.png")
# plt.savefig("code/part_I_C/figures/consumption_per.pdf")
# plt.show()


# reprb/teprb
# sns.set_style("darkgrid")
# fig = plt.figure(figsize=(7, 5))
plt.subplot(2, 2, 4)
# ind = np.arange(4)    # the x locations for the groups
# width = 0.4

# p1 = plt.bar(ind, (100, 100, 100, 100), width)
max_value = ca_reprb/ca_teprb*100
p4 = plt.bar(ind, (az_reprb/az_teprb*100/max_value, ca_reprb/ca_teprb*100/max_value,
                   nm_reprb/nm_teprb*100/max_value, tx_reprb/tx_teprb*100/max_value), width, color=colors)

t_az += az_reprb/az_teprb*100/max_value
t_ca += ca_reprb/ca_teprb*100/max_value
t_nm += nm_reprb/nm_teprb*100/max_value
t_tx += tx_reprb/tx_teprb*100/max_value

plt.title("Renewable Energy Production Percentage of Four States")
plt.xlabel("States")
plt.ylabel("Data / Score")
plt.xticks(ind, ('Arizona', 'California', 'New Mexico', 'Taxes'))
plt.savefig("code/part_I_C/figures/renewable_estimation.png")
plt.savefig("code/part_I_C/figures/renewable_estimation.pdf")

plt.legend([p1, p2, p3, p4], [
           ('Arizona', 'California', 'New Mexico', 'Taxes')])
# plt.show()
print(t_az, t_ca, t_nm, t_tx)






