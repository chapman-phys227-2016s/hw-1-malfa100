import math

def trapezint(f, a, b, n):
    sum = 0
    h = (b - a)/float(n)
    for i in range(1, n - 2):
        sum += (h / 2) * (f(a + i * h) + f(a + (i + 1) * h));
    return sum

def double_prime(f, x, h=1.0E-5):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)

def max_double_prime(f, a, b, n):
    

def adaptive_trapezint(f, a, b, eps=1E-5):
    h = math.sqrt((12 * eps) / ((b - a) * max_double_prime))
    n = (b - a) / h
    return trapezint(f, a, b, n)