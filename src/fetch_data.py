import os
import sys
import logging as log
import requests

url = "https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv"

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
    # TODO   Add url in a yaml file and read it

    fetch_data(url)