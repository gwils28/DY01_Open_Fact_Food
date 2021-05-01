import os
import sys
import logging as log
import requests
import yaml

path = "/home/wils/Data_Project/DY01_Open_Fact_Food/etc/conf/properties.yaml"

def get_url(path):
    with open(path,"r") as file:
        ylist = yaml.load(file, Loader=yaml.FullLoader)
        return ylist["url"]

def fetch_data(url):
    """
    :param arg1:
    :param arg2:
    :return:
    """
    r = requests.get(url, allow_redirects=True)
    with open("/home/wils/Data_Project/DY01_Open_Fact_Food/etc/data/raw_data.csv","wb") as f:
        f.write(r.content)

if __name__ =='__main__':

    # TODO   if raw data exist  then don't lunch this function.
    # TODO   Add logger

    # fetch_data(get_url(path))

    print(get_url(path))