#!/usr/bin/env python3

import pandas as pd
import numpy as np
import sys
# read in all our data
# nfl_data = pd.read_csv("../input/nflplaybyplay2009to2016/NFL Play by Play 2009-2017 (v4).csv")

# set seed for reproducibility
#numpy.random.seed(0) 


def showMe(x):
    #missing_values = ["n/a", "na", "-", "--", "N/a", "n/A"]
    data = pd.read_csv(x, engine = 'python')
    print(data.head())
    print(data.info())

    missingCount = data.isnull().sum()
    #print(missingCount[0:10])
    
    # how many total missing values do we have?
    total_cells = np.product(data.shape)
    total_missing = missingCount.sum()

    # percent of data that is missing
    percent_missing = (total_missing/total_cells) * 100
    print("Percent missing: " + str(percent_missing))

    #print(data.head())

    #print('Row count is:',data.shape[0])
    print("Missing count:")
    print(missingCount[0:10])
    
if __name__ == "__main__":

    x = sys.argv[1]
    print(showMe(x))
