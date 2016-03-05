#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib
import numpy as np
import re

fi = open('data.txt','r')
list_data = fi.readlines()
data_size = len(list_data)
lists = [[0 for x in range(3)] for x in range(data_size)] 

for i in range(data_size):
    temp1 = re.split('\n',list_data[i])
    temp = re.split(' ',temp1[0])
    lists[i][0] = temp[0]
    lists[i][1] = temp[1]
    lists[i][2] = temp[2]

for i in range(data_size):
    lists[i].append(int(lists[i][1])/2-int(lists[i][2]))

print(lists)
