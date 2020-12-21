# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 22:49:51 2020

@author: berk
"""

def st_dev():
    from statistics import pstdev, mean,median,mode, pvariance
    from scipy import stats
    from matplotlib import pyplot as plt
    entry=[]
    sizeplt=[]
    count=0
    size =int(input("Enter number of days: "))
    while count<size:
        val = int(input("Please enter {}. day cases: ".format(count+1)))
        entry.append(val)
        count += 1
    print("Mean is: ",(mean(entry)))
    print("Variance is:", (pvariance(entry)))
    print("Standard Deviation is:", (pstdev(entry)))
    print("Mode is:", (mode(entry)))
    print("Coefficient of Variation:",stats.variation(entry))
    print("Z Scores are:",stats.zscore(entry))
    print("Median is:", (median(entry)))
    for z in range(1,len(entry)+1):
        sizeplt.append(z)
    plt.plot(sizeplt,entry)
    plt.title("Turkey Covid-19 Daily Date Information")
    plt.xlabel("Day")
    plt.ylabel("Cases")
    plt.show()
st_dev()
#resources arehttps://docs.python.org/3/library/statistics.html
#https://www.geeksforgeeks.org/scipy-stats-zscore-function-python/
#https://pybilim.wordpress.com/2014/01/01/matplotlib-1-temel-grafikler/


 
