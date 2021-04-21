#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = int(input('Введите первую сторону '))
b = int(input('Введите вторую сторону '))
c = int(input('Введите третью сторону '))
if a != b and a!= c and b!= c:
    print("Разносторонний треугольник")
elif a == b == c:
    print("Равносторонний треугольник")
elif a + b <= c or a + c <= b or b + c <= a:
    print ("Такого треугольника не существует")
else:
    print("Равнобедренный треугольник")
