#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73
a = 112
if x > y:
    a = 112
    print('x < y: x is {} and y is {}'.format(x, y))
elif x < y:
    print(f'a: {a}, x: {x}, y: {y}')
else:
    print('do something else')

print(f'a is {a}')
print('a value is {}'.format(a))