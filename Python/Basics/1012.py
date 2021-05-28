import math as m
A, B, C =[float(x) for x in input("Enter three value: ").split()]

TRIANGULO = (A * C)/2
CIRCULO = (m.pi * pow(C, 2))
TRAPEZIO = ((A + B) * C) / 2
QUADRADO = B * B
RETANGULO = A * B


print("TRIANGULO: %.3f" % TRIANGULO)
print("CIRCULO: %.3f" % CIRCULO)
print("TRAPEZIO: %.3f" % TRAPEZIO)
print("QUADRADO: %.3f" % QUADRADO)
print("RETANGULO: %.3f" % RETANGULO)

