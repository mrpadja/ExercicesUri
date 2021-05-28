Valor = int(input(">"))

A = Valor//365
rest = Valor % 365
M = rest // 30
rest = rest% 30


print("{} ano(s)".format(A))
print("{} mes(es)".format(M))
print("{} dia(s)".format(rest))