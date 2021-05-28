import math as m
a, b, c =[int(x) for x in input("Enter three value: ").split()]

maior1 = (a + b + abs(a - b))/2

MaiorGeral = (maior1 + c + abs(maior1 - c))/2

print("%d eh o maior" % MaiorGeral)