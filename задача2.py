#!/usr/bin/env python 3
# -*- encoding : utf 8 -*-
from math import pi, sqrt

if __name__ = "__main__" :

S1 = float(input("S of Circle"))
S2 = float(input("S of Triangle"))
a = sqrt(4*S1/Sqrt(3))
r_0 = sqrt(S2/pi)
r = (a * sqrt(3))/6
R = (a * sqrt(3))/3
if r_0 <= r:
print("Окружность может поместиться в треугольник")
else
print("Окружность не может поместиться в треугольник")
if r_0 >= R:
print("Треугольник может поместиться в окружность")
else
print("Треугольник не может поместиться в окружность")

