from read import *

#industrial
ind_msn = []
ind_description = []
ind_unit = []

#end-use
es_msn = []
es_description = []
es_unit = []

#transportation
tran_msn = []
tran_description = []
tran_unit = []

#commercial
com_msn = []
com_description = []
com_unit = []

#electric_power
elec_msn = []
elec_description = []
elec_unit = []

#residential
res_msn = []
res_description = []
res_unit = []

for i in range(len(comp_data["Description"])):
    if re.search("industrial sector", comp_data["Description"][i]) :
        ind_msn.append(comp_data["MSN"][i])
        ind_description.append(comp_data["Description"][i])
        ind_unit.append(comp_data["Unit"][i])
    elif re.search("end-use", comp_data["Description"][i]):
        es_msn.append(comp_data["MSN"][i])
        es_description.append(comp_data["Description"][i])
        es_unit.append(comp_data["Unit"][i])
    elif re.search("transportation sector", comp_data["Description"][i]) or re.search("vehicle fuel", comp_data["Description"][i]):
        tran_msn.append(comp_data["MSN"][i])
        tran_description.append(comp_data["Description"][i])
        tran_unit.append(comp_data["Unit"][i])
    elif re.search("commercial sector", comp_data["Description"][i]):
        com_msn.append(comp_data["MSN"][i])
        com_description.append(comp_data["Description"][i])
        com_unit.append(comp_data["Unit"][i])
    elif re.search("electric power sector", comp_data["Description"][i]):
        elec_msn.append(comp_data["MSN"][i])
        elec_description.append(comp_data["Description"][i])
        elec_unit.append(comp_data["Unit"][i])
    elif re.search("residential sector", comp_data["Description"][i]):
        res_msn.append(comp_data["MSN"][i])
        res_description.append(comp_data["Description"][i])
        res_unit.append(comp_data["Unit"][i])
    else:
        pass

# print(comp_data)
industrial = OrderedDict()
end_use = OrderedDict()
transportation = OrderedDict()
commercial = OrderedDict()
electric_power = OrderedDict()
residential = OrderedDict()

industrial = OrderedDict()
item_dict = OrderedDict()
item_dict["MSN"] = ind_msn
item_dict["Description"] = ind_description
item_dict["Unit"] = ind_unit
industrial = pd.DataFrame(item_dict)

end_use = OrderedDict()
item_dict["MSN"] = es_msn
item_dict["Description"] = es_description
item_dict["Unit"] = es_unit
end_use = pd.DataFrame(item_dict)

transportation = OrderedDict()
item_dict["MSN"] = tran_msn
item_dict["Description"] = tran_description
item_dict["Unit"] = tran_unit
transportation = pd.DataFrame(item_dict)

commercial = OrderedDict()
item_dict["MSN"] = com_msn
item_dict["Description"] = com_description
item_dict["Unit"] = com_unit
commercial = pd.DataFrame(item_dict)

electric_power = OrderedDict()
item_dict["MSN"] = elec_msn
item_dict["Description"] = elec_description
item_dict["Unit"] = elec_unit
electric_power = pd.DataFrame(item_dict)

residential = OrderedDict()
item_dict["MSN"] = res_msn
item_dict["Description"] = res_description
item_dict["Unit"] = res_unit
residential = pd.DataFrame(item_dict)

print(industrial)
print(commercial)
print(transportation)
print(electric_power)
print(residential)
print(end_use)
