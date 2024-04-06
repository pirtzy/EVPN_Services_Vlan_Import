# Created By 
# Shai Perretz 5.4.2024
#
# Input:  vlanlist.csv - CSV format with two columns: vlanId, name
# Output: vlanlist.yaml - yaml format to use as import for the EVPN_Services studios on CloudVision
# Output yaml file formatted without indentation (using braces)

import yaml
import csv

VLAN_LIST_CSV = 'vlanlist.csv'
OUTPUT_VLAN_LIST_YAML = 'vlanlist.yaml'
CONFIG_EXAMPLE_YANL = 'config.yml'


def printVlans(tenant):
    for tenant in config_dict['inputs']['tenants']:
        for vlan in tenant['vlans']:
            print(vlan['vlanId'])
            print(vlan['name'])

def openConfigEample(filename):
    with open(filename, 'r') as file:
        config_example = yaml.safe_load(file)
    return config_example


def createVlansFromCSV(config_dict):
    # get list of vlans from csv
    with open(VLAN_LIST_CSV, 'r') as file:
        csv_reader = csv.DictReader(file)
        myvlans = [row for row in csv_reader]

    # take one vlan from the config to use for the syntax
    for tenant in config_dict['inputs']['tenants']:
        for vlan in tenant['vlans']:
            tempateVlan = vlan
            break

    # go over the vlans in csv (myvlans) and add them to the existing tenant
    for tenant in config_dict['inputs']['tenants']:
        for vlan in myvlans:
            newVlan = tempateVlan.copy()
            newVlan['vlanId'] = vlan['vlanId']
            newVlan['name'] = vlan['name']
            tenant['vlans'].append(newVlan)
    return config_dict

 
if __name__ == '__main__':
    config_dict = openConfigEample(CONFIG_EXAMPLE_YANL)
    output = createVlansFromCSV(config_dict)

    text_file = open(OUTPUT_VLAN_LIST_YAML, "w")
    text_file.write(str(output))
    text_file.close()
 