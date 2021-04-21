#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys
EPS = 1e-5

if __name__ == '__main__':
    x = float(input("Value of x? "))
    n = int(input("Value of n? "))
    if n < 0:
        print("Недопустимое значение N", file=sys.stderr)
        exit(1)

    k = 0
    a = x
    S = 0
    b = math.pow(x/2, n)

    while math.fabs(a) > EPS:
        a *= math.pow(1, k) / (math.pow(2, n + 2 * k) * math.factorial(k)*math.factorial(n + k))
        S += a
        n += 1
print (f" J{n} ({x}) = {(b * S)}")