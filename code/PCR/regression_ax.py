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

x_data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\\PCR\\az_result.csv",
                       skiprows=None, engine='c', low_memory=True)
y_data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\\PCR\\az_Total.csv",
                       skiprows=None, engine='c', low_memory=True)
original_data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\\PCR\\az_data_by_year_original.csv",
                       skiprows=None, engine='c', low_memory=True)
feature_cols = ['CLTCV', 'CLCCV', 'CLACB', 'ESCCV', 'ESRCV', 'ESTCB', 'ESTCV', 'GECCB',
       'NGACB', 'NGCCV', 'NGTCV', 'NNCCB', 'PAACV', 'SOEGB']
data_x = OrderedDict()
data_y = OrderedDict()
coef_ = OrderedDict()
intercept_ = OrderedDict()
linreg = LinearRegression()
for j in feature_cols:
    coef_[j] = []
for i in range(1962, 2008):
    for j in feature_cols:
        data_x[j] = []
        for k in range(-2, 3):
            data_x[j].append(x_data[j][i-1960+k])
    data_y["TETCB"] = []
    for k in range(-2, 3):
        data_y["TETCB"].append(y_data["TETCB"][i-1960+k])
    data = pd.DataFrame(data_x)
    data.to_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\PCR\\az_regression_x.csv",
                index=False, index_label=False, sep=',')
    data = pd.DataFrame(data_y)
    data.to_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\PCR\\az_regression_y.csv",
                index=False, index_label=False, sep=',')
    data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\PCR\\az_regression_x.csv",
                       skiprows=None, engine='c', low_memory=True)
    X = data[feature_cols]
    data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\PCR\\az_regression_y.csv",
                       skiprows=None, engine='c', low_memory=True)
    y = data["TETCB"]
    model = linreg.fit(X, y)
    k = 0
    for j in feature_cols:
        if original_data[j][i-1960] > 0:
            coef_[j].append(linreg.coef_[k])
        else:
            coef_[j].append(0)
        k += 1
    intercept_[i] = linreg.intercept_

data = pd.DataFrame(coef_)
data.to_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\PCR\\az_regression_coef.csv",
                index=False, index_label=False, sep=',')

az_Year = []
for i in range(1962, 2008):
    az_Year.append(i)
fig = plt.figure(figsize=(20, 10))
k = 1
for i in feature_cols:
    plt.subplot(4, 4, k)
    plt.plot(az_Year, coef_[i],  label=i)
    plt.legend(loc='upper left')

    k += 1
plt.savefig("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\\PCR\\az.png")
plt.savefig("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\\PCR\\az.pdf")



