#! usr/bin/python3

import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict, defaultdict
import matplotlib as mpl
import matplotlib.pyplot as plt
# import seaborn as sns
from scipy import stats, integrate

# sns.set() # switch to seaborn default
# sns.set_style("whitegrid")

#load sector msncodes
msncodes = pd.read_csv("data/csv/price_expenditures/expenditures.csv", engine='c', low_memory=True)

exp_sector = OrderedDict()
msn = []
description = []
unit = []

for i in range(len(msncodes["Description"])):
    if re.search("Total", msncodes["Description"][i]) and re.search("sector", msncodes["Description"][i]):
        msn.append(msncodes["MSN"][i])
        description.append(msncodes["Description"][i])
        unit.append(msncodes["Unit"][i])

exp_sector["MSN"] = msn
exp_sector["Description"] = description
exp_sector["Unit"] = unit
exp_sector_data = pd.DataFrame(exp_sector)
exp_sector_data.to_csv("data/csv/price_expenditures/sector/exp.csv",
                  index=False, index_label=False, sep=',')
