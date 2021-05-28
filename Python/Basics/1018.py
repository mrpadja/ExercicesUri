Valor = int(input(">"))

print (Valor)
cedulas = [100, 50, 20, 10, 5, 2, 1]

for cedula in cedulas:
    qtd_cedulas = int (Valor / cedula)
    print("{} nota(s) de R$ {},00".format(qtd_cedulas, cedula))
    Valor -= qtd_cedulas * cedula