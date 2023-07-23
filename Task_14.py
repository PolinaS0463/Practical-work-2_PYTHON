# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

border = int(input("Введите границу вывода степеней двойки: "))
base = 2
exponent = 1

# I. Способ (циклом):

while(base <= border):
    print(base)
    for i in range(1, exponent+1, 1):
        base*=2

# II. Способ (рекурсией):

base = 2
exponent = 1

def Exponentiate(base, exponent, border):
    if(base > border):
        return
    print(base)
    Exponentiate(base*2, exponent, border)

Exponentiate(base, exponent, border)