# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:46:13 2020

@author: Tyler
"""
#import module

from urllib import request

#url of txt file to download

my_url = 'https://www2.census.gov/geo/docs/maps-data/data/rel/zcta_tract_rel_10.txt'

#function NOTE CHANGE des_url line with name of csv
def download(t_url):
    response = request.urlopen(t_url)
    data = response.read()
    txt_str = str(data)
    lines = txt_str.split("\\n")
    des_url = r'census_tract.csv'
    fx = open(des_url,"w")
    for line in lines:
        fx.write(line+ "\n")
    fx.close()

#downloads to C:\Users\Tyler
    
download(my_url)