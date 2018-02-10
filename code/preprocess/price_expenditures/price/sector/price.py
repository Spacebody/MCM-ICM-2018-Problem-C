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
msncodes = pd.read_csv("data/csv/price_expenditures/price.csv", engine='c')

price_sector = OrderedDict()
msn = []
description = []
unit = []

for i in range(len(msncodes["Description"])):
    if re.search("sector", msncodes["Description"][i]) and re.search("[T|t]otal", msncodes["Description"][i]):
        msn.append(msncodes["MSN"][i])
        description.append(msncodes["Description"][i])
        unit.append(msncodes["Unit"][i])

price_sector["MSN"] = msn
price_sector["Description"] = description
price_sector["Unit"] = unit
price_sector_data = pd.DataFrame(price_sector)
price_sector_data.to_csv("data/csv/price_expenditures/sector/price_sector.csv",
                       index=False, index_label=False, sep=',')
