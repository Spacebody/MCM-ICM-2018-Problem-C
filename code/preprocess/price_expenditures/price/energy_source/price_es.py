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
msncodes = pd.read_csv(
    "data/csv/price_expenditures/price.csv", engine='c')

price_sector = OrderedDict()
msn = []
description = []
unit = []

for i in range(len(msncodes["MSN"])):
    if re.search("CLTCD", msncodes["MSN"][i]) or \
        re.search("ESTCD", msncodes["MSN"][i]) or \
        re.search("NGTCD", msncodes["MSN"][i]) or \
        re.search("NUETD", msncodes["MSN"][i]) or \
        re.search("PATCD", msncodes["MSN"][i]) or \
        re.search("WWTCD", msncodes["MSN"][i]):
        msn.append(msncodes["MSN"][i])
        description.append(msncodes["Description"][i])
        unit.append(msncodes["Unit"][i])

price_sector["MSN"] = msn
price_sector["Description"] = description
price_sector["Unit"] = unit
price_sector_data = pd.DataFrame(price_sector)
price_sector_data.to_csv("data/csv/price_expenditures/energy_source/price_es.csv",
                         index=False, index_label=False, sep=',')
