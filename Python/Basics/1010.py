a1, a2, a3 = [float(x) for x in input("Enter three value: ").split()]
b1, b2, b3 = [float(x) for x in input("Enter three value: ").split()]

val = (a2 * a3) + (b2 * b3)

print("VALOR A PAGAR: R$ %.2f" % val)
