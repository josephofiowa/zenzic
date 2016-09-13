# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 23:08:15 2016

@author: JosephNelson
"""
# generate two random samples of 10k normally distributed points
import numpy as np
rand1 = np.random.normal(0,1,10000)
rand2 = np.random.normal(0,1,10000)

# multipythem (or rand_squared)
rand_sq = rand1 * rand2

# plot it on distribution plot
import seaborn as sns
sns.distplot(rand_sq)

# conduct normality test, reject if p<0.05
import scipy as sp
sp.stats.mstats.normaltest(rand_sq)
