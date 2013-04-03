#!/usr/bin/env python
# -*- coding:utf-8 -*-

#################################################
# Perfect number is a number which              #
# the addition of its divider (except itself)   #
# equals itself                                 #
# e.g 6 is a perfect number                     #
# because 6 = 1+2+3 = 6                         #
# 1,2,3 are the dividers of 6                   #
# e.g of this code                              #
# ./isPerfectNo.py [noTested]                   #
#################################################

import sys

no_query = int(sys.argv[1])
no_list = range(1,no_query)
no_test = sum([no_list[i-1] for i in no_list if (no_query%i)==0])

if no_query == no_test:
  print "%s is a perfect number"%(no_query)
else:
  print "%s is NOT a perfect number"%(no_query)
