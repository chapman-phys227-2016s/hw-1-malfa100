"""
File: sinesum1.py
Exercise 3.15
Copyright (c) 2016 Andrew Malfavon
License: MIT
Compares an approximation of a sum of sins to a piecewise function.
"""
import math
import numpy as np

#approximation of piecewise function
def S(t, n, T):
    sum = 0
    for i in range(1, n + 1):
        sum += (4 / (math.pi * (2 * i - 1))) * (math.sin((2 * math.pi * t * (2 * i - 1)) / T))
    return sum

#piecwise function
def f(t, T):
    if (0 < t) and (t < T / 2.0):
        return 1
    if (t == T/2):
        return 0
    if (T / 2.0 < t) and (t < T):
        return -1

#calculate the error between f(t,T) and S(t,n,T) for a list of n values and alpha values
def error():
    list_n = [1, 3, 5, 10, 30, 100]
    list_alpha = [0.01, 0.25, 0.49]
    T = 2 * math.pi
    t = np.zeros(len(list_alpha))
    error_a1 = np.zeros(len(list_n))
    error_a2 = np.zeros(len(list_n))
    error_a3 = np.zeros(len(list_n))
    for i in range(len(list_alpha)):
        t[i] = list_alpha[i] * T
    for j in range(len(list_n)):
        error_a1[j] = f(t[0], T) - S(t[0], list_n[j], T)
        error_a2[j] = f(t[1], T) - S(t[1], list_n[j], T)
        error_a3[j] = f(t[2], T) - S(t[2], list_n[j], T)
    return error_a1, error_a2, error_a3

def table():
    #table to display the error for various n and alpha values
    print '                alpha = 0.01    ' + '    alpha = 0.25    ' + '        alpha = 0.49    '
    n1 = 'n = 1:'
    n2 = 'n = 3:'
    n3 = 'n = 5:'
    n4 = 'n = 10:'
    n5 = 'n = 30:'
    n6 = 'n = 100:'
    space = '        '
    #set up the table
    print '{}{}{}{}{}{}{}'.format(n1, space, error()[0][0], space, error()[1][0], space, error()[2][0])
    print '{}{}{}{}{}{}{}'.format(n2, space, error()[0][1], space, error()[1][1], space, error()[2][1])
    print '{}{}{}{}{}{}{}'.format(n3, space, error()[0][2], space, error()[1][2], space, error()[2][2])
    print '{}{}{}{}{}{}{}'.format(n4, space, error()[0][3], space, error()[1][3], space, error()[2][3])
    print '{}{}{}{}{}{}{}'.format(n5, space, error()[0][4], space, error()[1][4], space, error()[2][4])
    print '{}{}{}{}{}{}{}'.format(n6, space, error()[0][5], space, error()[1][5], space, error()[2][5])

def s(t, n, T):
    sum = 0
    for i in range(n):
        sum = sum + ((2 * (i + 1) - 1)**-1) * math.sin((2 * (2 * (i + 1) - 1) * math.pi * t) / float(T))
    return sum*(4/math.pi)

def test_S():
    #test approximation of f(t)
    assert S(1, 1, 1) < 1E-10#a simple test. Should be basically zero
    assert abs(S(1, 2, 2 * math.pi) - (4 / math.pi) * ((math.sin(1)) + ((1 / 3.0) * math.sin(3)))) < 1E-10

def test_f():
    #test the piecewise function
    assert f(2, 2 * math.pi) == 1
    assert f(math.pi, 2 * math.pi) == 0
    assert f(4, 2 * math.pi) == -1