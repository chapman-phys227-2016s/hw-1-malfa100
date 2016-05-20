"""
File: adaptive_trapezint.py
Exercise 3.8
Copyright (c) 2016 Andrew Malfavon
License: MIT
Computes an approximation of an integral.
"""

import numpy as np

#Approximate integral using n number of trapazoids.
def trapezint(f, a, b, n):
    sum = 0
    h = (b - a) / float(n)
    for i in range(n):
        sum += (h / 2) * (f(a + i * h) + f(a + (i + 1) * h))
    return sum

#Approximate the second derivative of a function.
def double_prime(f, x, h=1.0E-5):
    return (f(x - h) - 2 * f(x) + f(x + h)) / float(h**2)

#Find the maximum second derivative between two values by using n iterations.
def max_double_prime(f, a, b, n=10000):
    maximum = abs(double_prime(f, a))
    for i in range(1, n):
        new_maximum = abs(double_prime(f, a + i  * ((b-a)/float((n)))))
        if new_maximum > maximum:
            maximum = new_maximum
    return maximum

def adaptive_trapezint(f, a, b, eps=1.0E-5):
    h = np.sqrt((12 * eps) / ((b - a) * max_double_prime(f, a, b)))
    n = (b - a) / h
    intn = int(n)#make calculated n an integer
    return trapezint(f, a, b, intn), intn

#Functions to test the maximum second derivative.
def func_x_cubed(x):
    return x**3

def func_sin(x):
    return np.sin(x)

def func_cos(x):
    return np.cos(x)

#Test chain rule.
def func_e_sin(x):
    return np.exp(np.sin(x))

def test_max():
    assert abs(max_double_prime(func_x_cubed, 1, 5) - 30) < 0.01
    assert abs(max_double_prime(func_sin, 0, 2 * np.pi) - 1) < 0.01
    assert abs(max_double_prime(func_cos, 0, (3 * np.pi) / float(2)) - 1) < 0.01

def table():
    #display the function and interval with the error and estimate n
    print '    Function' + '                    ' + 'Error' +  '            ' + 'Estimated n'
    #labels for the table
    cos = adaptive_trapezint(func_cos, 0, np.pi)#functions from the book
    sin1 = adaptive_trapezint(func_sin, 0, np.pi)
    sin2 = adaptive_trapezint(func_sin, 0, np.pi / 2.0)
    cos_phrase = 'cos(x) from 0 to pi'#labels for the functions
    sin1_phrase = 'sin(x) from 0 to pi'
    sin2_phrase = 'sin(x) from 0 to pi/2'
    space = '        '#blank spaces for formatting the table
    space2 = '      '
    print '{}{}{}{}{}'.format(cos_phrase, space, cos[0], space, cos[1])#puts the table together
    print '{}{}{}{}{}'.format(sin1_phrase, space, abs(sin1[0] - 2), space, sin1[1])
    print '{}{}{}{}{}'.format(sin2_phrase, space2, abs(sin2[0] - 1), space, sin2[1])