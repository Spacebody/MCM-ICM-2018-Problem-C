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

sns.set() # switch to seaborn default

az_data = pd.read_csv("data/csv/az_data.csv")


print(az_data)







