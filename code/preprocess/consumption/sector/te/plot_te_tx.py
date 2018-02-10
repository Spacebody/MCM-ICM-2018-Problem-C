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
from te_tx import teacb_data, teccb_data, teeib_data, teicb_data, tercb_data


#plot
sns.set_style("darkgrid")
fig = plt.figure(figsize=(10, 5))
plt.title("Total Consumption by Sectors of Texas")
plt.xlabel("Year")
plt.ylabel("Data/Billion Btu")
plt.plot(teacb_data["Year"], teacb_data["Data"],  label="Transportation")
plt.plot(teccb_data["Year"], teccb_data["Data"], label="Commercial")
plt.plot(teeib_data["Year"], teeib_data["Data"],  label="Electric power")
plt.plot(teicb_data["Year"], teicb_data["Data"],  label="Industrial")
plt.plot(tercb_data["Year"], tercb_data["Data"],  label="Residential")
plt.legend(loc='upper left')
plt.savefig("code/preprocess/consumption/sector/figures/te/Sectors_Texas.png")
plt.savefig("code/preprocess/consumption/sector/figures/te/Sectors_Texas.pdf")

plt.show()
