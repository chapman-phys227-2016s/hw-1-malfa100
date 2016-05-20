"""
File: find_primes.py
Exercise 3.34
Copyright (c) 2016 Andrew Malfavon
License: MIT
Displays all prime numbers less than or equal to a given N number.
"""

#Creates a list of N numbers, removes the non-prime numbers, and returns a list of primes.
def find_primes(N):
    N_list = list(range(2, N + 1))
    for i in range(2, N + 1):
        for j in range(1, N + 1):
            non_prime = i + (i * j)
            if non_prime in N_list:
                N_list.remove(non_prime)
    return N_list

#Test for N = 50
def test_find_primesOne():
    assert find_primes(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

#Test to make sure it checks the last number in the list.
def test_find_primesTwo():
    assert find_primes(47) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

#Test for N = 100
def test_find_primesThree():
    assert find_primes(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]