#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

if __name__ == "__main__":
    a = float(input("a: "))
    if a != 0:
        b = float(input("b: "))
        c = float(input("c: "))

        D = b * b - 4 * a * c

        if D > 0:
            t1 = (-b - sqrt(D)) / (2 * a)
            t2 = (-b + sqrt(D)) / (2 * a)
            if t1 != t2:
                print(-sqrt(t1), sqrt(t1), -sqrt(t2), sqrt(t2))
            else:
                print("Roots are equal and their value is ", -sqrt(t1), sqrt(t1))
        elif D == 0:
            t = -b / (2 * a)
            print(-sqrt(t), sqrt(t))
        else:
            print("No roots.")
    else:
        print("a can't be zero.")
