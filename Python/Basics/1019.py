Valor = int(input(">"))

H = int (Valor/3600)
rest = Valor % 3600
M = int(rest/60)
rest = rest % 60
print("{}:{}:{}".format(H, M, rest))