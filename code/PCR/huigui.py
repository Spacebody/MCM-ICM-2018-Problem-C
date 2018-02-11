import pandas as pd
import re
import numpy as np
import os
import sys
from collections import OrderedDict
import copy
from sklearn.linear_model import LinearRegression

# parent_path = os.path.realpath(os.pardir)
# if sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
#     seseds_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C\\data\\csv\\seseds.csv')
#     msncodes_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C\\data\\csv\\msncodes.csv')
# elif sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
#     seseds_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C/data/csv/seseds.csv')
#     msncodes_path = os.path.join(parent_path, 'MCM-ICM-2018-Problem-C/data/csv/msncodes.csv')
# else:
#     pass
data_test = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\\PCR\\az_result_test.csv",
                   skiprows=None, engine='c', low_memory=True)
data_train = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\\PCR\\az_result_train.csv",
                   skiprows=None, engine='c', low_memory=True)
variable_data = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\code\PCR\\variables.csv",
                       skiprows=None, engine='c', low_memory=True)
variable1 = variable_data["MSN"]
variable = []
for i in variable1:
    if i not in variable:
        variable.append(i)
feature_cols = ["CLTCV", "CLCCV", "CLACB", "ESCCV",	"ESRCV","ESTCB","ESTCV","GETCB","GERCB","LOTCB","NGCCB","NGICB",
                "NGRCB","NNACB"]

X = data_train[feature_cols]
y = data_train["TEGDS"]
linreg = LinearRegression()
model = linreg.fit(X, y)
print(model)
print(linreg.intercept_)
print(linreg.coef_)





