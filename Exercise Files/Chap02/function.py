#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# def function(n=1):
#     print(n)
#     return n

# x = function(42)
# print(x)

def isPrime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def list_prime():
    for i in range(100):
        if isPrime(i):
            print(i, end = ' ', flush=True)
    print()

list_prime()