import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict



# parent_path = os.path.realpath(os.pardir)
# if sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
#     seseds_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C\\data\\csv\\seseds.csv')
#     msncodes_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C\\data\\csv\\msncodes.csv')
# elif sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
#     seseds_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C/data/csv/seseds.csv')
#     msncodes_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C/data/csv/msncodes.csv')
# else:
#     pass
data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\\PCR\\nm_data.csv",
                   skiprows=None, engine='c', low_memory=True)
variable_data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\PCR\\variables.csv",
                       skiprows=None, engine='c', low_memory=True)
variable1 = variable_data["MSN"]
variable = []
for i in variable1:
    if i not in variable:
        variable.append(i)
nm_data = OrderedDict()
for i in range(0, len(variable)):
    nm_data[variable[i]] = np.zeros(50)
for i in range(0, 50):
    for j in range(len(data)):
        if int(data["Year"][j])-1960 == i:
            if data["MSN"][j] in variable:
                nm_data[data["MSN"][j]][i] = data["Data"][j]
year = []
for i in range(1960, 2010):
    year.append(i)
nm_data["Year"] = year
for i in variable:
    if i != "TEGDS" and i != "Year":
        mean = np.mean(nm_data[i])
        std = np.std(nm_data[i])
        if std != 0:
            for j in range(len(nm_data[i])):
                nm_data[i][j] = (nm_data[i][j]-mean)/std
nm_comp_data = OrderedDict()
nm_comp_data = pd.DataFrame(nm_data)
nm_comp_data.to_csv("nm_data_by_year.csv", index=False, index_label=False, sep=',')




