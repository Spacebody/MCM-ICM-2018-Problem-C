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
seseds = pd.read_csv("C:\\Users\\THINKPAD\\PycharmProjects\\MCM-ICM-2018-Problem-C\\data\\csv\\seseds.csv", skiprows=None, engine='c', low_memory=True)
az_msn = []
az_state_code = []
az_year = []
az_data = []
ca_msn = []
ca_state_code = []
ca_year = []
ca_data = []
nm_msn = []
nm_state_code = []
nm_year = []
nm_data = []
tx_msn = []
tx_state_code = []
tx_year = []
tx_data = []
for i in range(len(seseds["MSN"])):
    if re.search("AZ", seseds["StateCode"][i]):
        az_msn.append(seseds["MSN"][i])
        az_state_code.append(seseds["StateCode"][i])
        az_year.append(seseds["Year"][i])
        az_data.append(seseds["Data"][i])
    if re.search("CA", seseds["StateCode"][i]):
        ca_msn.append(seseds["MSN"][i])
        ca_state_code.append(seseds["StateCode"][i])
        ca_year.append(seseds["Year"][i])
        ca_data.append(seseds["Data"][i])
    if re.search("NM", seseds["StateCode"][i]):
        nm_msn.append(seseds["MSN"][i])
        nm_state_code.append(seseds["StateCode"][i])
        nm_year.append(seseds["Year"][i])
        nm_data.append(seseds["Data"][i])
    if re.search("TX", seseds["StateCode"][i]):
        tx_msn.append(seseds["MSN"][i])
        tx_state_code.append(seseds["StateCode"][i])
        tx_year.append(seseds["Year"][i])
        tx_data.append(seseds["Data"][i])
az_comp_data = OrderedDict()
ca_comp_data = OrderedDict()
nm_comp_data = OrderedDict()
tx_comp_data = OrderedDict()
item_dict = OrderedDict()
item_dict["MSN"] = az_msn
item_dict["StateCode"] = az_state_code
item_dict["Year"] = az_year
item_dict["Data"] = az_data
az_comp_data = pd.DataFrame(item_dict)
az_comp_data.to_csv("C:/Users/THINKPAD/PycharmProjects/MCM-ICM-2018-Problem-C/data/csv/az_data.csv", index=False, index_label=False, sep=',')
item_dict["MSN"] = ca_msn
item_dict["StateCode"] = ca_state_code
item_dict["Year"] = ca_year
item_dict["Data"] = ca_data
ca_comp_data = pd.DataFrame(item_dict)
ca_comp_data.to_csv("C:/Users/THINKPAD/PycharmProjects/MCM-ICM-2018-Problem-C/data/csv/ca_data.csv", index=False, index_label=False, sep=',')
item_dict["MSN"] = nm_msn
item_dict["StateCode"] = nm_state_code
item_dict["Year"] = nm_year
item_dict["Data"] = nm_data
nm_comp_data = pd.DataFrame(item_dict)
nm_comp_data.to_csv("C:/Users/THINKPAD/PycharmProjects/MCM-ICM-2018-Problem-C/data/csv/nm_data.csv", index=False, index_label=False, sep=',')
item_dict["MSN"] = tx_msn
item_dict["StateCode"] = tx_state_code
item_dict["Year"] = tx_year
item_dict["Data"] = tx_data
tx_comp_data = pd.DataFrame(item_dict)
tx_comp_data.to_csv("C:/Users/THINKPAD/PycharmProjects/MCM-ICM-2018-Problem-C/data/csv/tx_data.csv", index=False, index_label=False, sep=',')