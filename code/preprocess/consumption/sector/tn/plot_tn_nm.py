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
from tn_nm import tnacb_data, tnccb_data, tnicb_data, tnrcb_data


#plot
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title(
    "Total Consumption(Excluding electrical system energy losses) (Sectors) of New Mexico")
plt.xlabel("Year")
plt.ylabel("Data / Billion Btu")
plt.plot(tnacb_data["Year"], tnacb_data["Data"],  label="Transportation")
plt.plot(tnccb_data["Year"], tnccb_data["Data"], label="Commercial")
plt.plot(tnicb_data["Year"], tnicb_data["Data"],  label="Industrial")
plt.plot(tnrcb_data["Year"], tnrcb_data["Data"],  label="Residential")
plt.legend(loc='upper left')
plt.savefig("code/preprocess/consumption/sector/figures/tn/Sectors_New_Mexico.png")
plt.savefig("code/preprocess/consumption/sector/figures/tn/Sectors_New_Mexico.pdf")

# plt.show()
