#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x = float(input("x: "))
    y = float(input("y: "))

    s = x * y

    if a * c <= s or a * b <= c or b * c <= s:
        print("Кирпич пройдёт")
    else:
        print("Кирпич не пройдёт")
