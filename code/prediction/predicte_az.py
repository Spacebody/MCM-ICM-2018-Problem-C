import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict
import copy
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
# parent_path = os.path.realpath(os.pardir)
# if sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
#     seseds_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C\\data\\csv\\seseds.csv')
#     msncodes_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C\\data\\csv\\msncodes.csv')
# elif sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
#     seseds_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C/data/csv/seseds.csv')
#     msncodes_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C/data/csv/msncodes.csv')
# else:
#     pass

x_data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\\PCR\\az_result .csv",
                       skiprows=None, engine='c', low_memory=True)
y_data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\\PCR\\az_Total .csv",
                       skiprows=None, engine='c', low_memory=True)
feature_cols = []
for i in x_data.keys():
    feature_cols.append(i)
data_coef = OrderedDict()
data_inter = OrderedDict()
Year = []
for i in range(1960, 2010):
    Year.append(i)
linreg = LinearRegression()


for i in feature_cols:
    model = linreg.fit(pd.DataFrame(Year), pd.DataFrame(x_data[i]))
    data_coef[i] = linreg.coef_
    data_inter[i] = linreg.intercept_

model = linreg.fit(x_data[feature_cols], y_data)
coef_ = linreg.coef_
inter_ = linreg.intercept_
print(data_coef)
print(data_inter)
print(coef_)
print(inter_)
prediction_az = []
for i in range(2010, 2016):
    prediction = inter_[0]
    k = 0
    for j in feature_cols:
        prediction += coef_[0][k]*(data_coef[j][0]*i+data_inter[j][0])
        k += 1
    prediction_az.append(prediction)
print(prediction_az)



