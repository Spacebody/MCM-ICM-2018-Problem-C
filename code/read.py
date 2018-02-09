#! usr/bin/python3

import pandas as pd 

seseds = pd.read_csv('../data/csv/seseds.csv', skiprows=None)
msncodes = pd.read_csv('../data/csv/msncodes.csv', skiprows=None)
print(seseds) 
print(msncodes)
