"""
File: centered_diff.py
Exercise 3.18
Copyright (c) 2016 Andrew Malfavon
License: MIT
Approximate differentiation.
"""

import math

def diff(f, x, h=1.0E-5):
    df = (f(x+h) - f(x-h)) / (2*h)
    return df

def func_one(x):
    return x**2

def func_two(x):
    return math.exp(x)

def func_three(x):
    return math.exp(-2 * x**2)

def func_four(x):
    return math.cos(x)

def func_five(x):
    return math.log(x)

#Collects the errors between the expected results and the approximated.
def application():
    app1 = 1 - diff(func_two, 0, 0.01)
    app2 = 0 - diff(func_three, 0, 0.01)
    app3 = 0 - diff(func_four, 2 * math.pi, 0.01)
    app4 = 1 - diff(func_five, 1, 0.01)
    return app1, app2, app3, app4

def table():
    print 'Function        ' + '            Error'
    func1 = 'exp(x) at x=0'
    func2 = 'exp(-2x^2) at x=0'
    func3 = 'cos(x) at x=2*pi'
    func4 = 'ln(x) at x=1'
    space = '    '
    print '{}{}{}{}{}'.format(func1, space, space, space, application()[0])
    print '{}{}{}{}{}'.format(func2, space, space, space, application()[1])
    print '{}{}{}{}{}'.format(func3, space, space, space, application()[2])
    print '{}{}{}{}{}'.format(func4, space, space, space, application()[3])

#Needed to round due to floating point not dropping exceeding decimals.
def test_one():
    assert diff(func_one, 5.0, 0.01) - 10.0 < 1E-10