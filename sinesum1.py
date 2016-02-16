"""
File: sinesum1.py
Copyright (c) 2016 Andrew Malfavon
License: MIT
Compares an approximation of a sum of sins to a piecewise function.
"""
import math

#approximation of piecewise function
def S(t, n, T):
    sum = 0
    for i in range(1, n + 1):
        sum += (4 / (math.pi * (2 * i - 1))) * (math.sin((2 * math.pi * t * (2 * i - 1)) / T))
    return sum

def test_S():
    assert S(1, 1, 4) == 4.0/math.pi

#piecwise function
def f(t, T):
    if (t > 0) and (T/2 > t):
        return 1
    if (t == T/2):
        return 0
    if (t < T/2) and (T < t):
        return -1

#iterates through the 3 possible alphas picking various n's for each and displaying the results
def table():
    list_n = [1, 3, 5, 10, 30, 100]
    list_a = [0.01, 0.25, 0.49]
    mStr = ""
    T = 2 * math.pi
    #Used to set up table format
    for i in range(0, len(list_a)):
        mStr += str(list_a[i]) + "\t|\t"
    print mStr
    for i in range(0, len(list_n)):
        mStr = str(list_n[i]) + "\t|\t"
        for j in range(0, len(list_a) - 1):
            t = list_a[j] * T
            diff = f(t, T) - S(t, list_n[i], T)
            mStr += str(diff) + "\t|\t"
        print mStr
table()