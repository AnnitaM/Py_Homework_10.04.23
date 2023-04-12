# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

k = int(input("Enter tne number "))
i = 1
a = 2
list = [] * k
while i < k:
    n = a ** i
    list.append(n)
    i += 1
print(list)