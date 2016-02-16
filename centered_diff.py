import math

def diff(f, x, h=1.0E-5):
    df = (f(x+h) - f(x-h)) / (2*h)
    return df

def func_one(x):
    return x**2

#Needed to round due to floating point not dropping exceeding decimals.
def test_one():
    assert (round(diff(quadratic, 5.0, 0.01)) == 10.0)

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
    print 1 - diff(func_two, 0, 0.01)
    print 0 - diff(func_three, 0, 0.01)
    print 0 - diff(func_four, 2*math.pi, 0.01)
    print 1 - diff(func_five, 1, 0.01)