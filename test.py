#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib
import numpy as np
import re

fi = open('data.txt','r')
list_data = fi.readlines()
lists = [[]]

for i in range(len(list_data)):
    temp1 = re.split('\n',list_data[i])
    temp = re.split(' ',temp1[0])
    #lists[i].append(temp[0])
    #lists[i].append(temp[1])
    #lists[i].append(temp[2])

print(temp[0])

print(temp[1])
print(temp[2])
