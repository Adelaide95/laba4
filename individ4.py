#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Value of x? "))
    n = float(input("Value of n? "))
a = x / 4
S, n = a, 1

while math.fabs(a) > EPS:
    a *= 1 / (n + 1)
    S += a
    n += 1
print (f"L({x})=", S)