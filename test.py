#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib
import numpy as np
import re

fi = open('data.txt','r')
list_data = fi.readlines()
data_size = len(list_data)
lists = [[0 for x in range(4)] for x in range(data_size)] 
doc_needed = []
def get_data():
    for i in range(data_size):
        temp1 = re.split('\n',list_data[i])
        temp = re.split(' ',temp1[0])
        lists[i][0] = temp[0]
        lists[i][1] = temp[1]
        lists[i][2] = temp[2]

    for i in range(data_size):
        lists[i][3] = str(int(lists[i][1])/2-int(lists[i][2]))
        doc_needed.append(int(lists[i][3]))

    return doc_needed

if __name__=='__main__':
    get_data()
