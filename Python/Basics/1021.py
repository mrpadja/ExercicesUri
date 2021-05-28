Valor = float(input(">"))
L1 = [100, 50, 20, 10, 5, 2]
L2 = [1, 0.50, 0.25, 0.10, 0.05, 0.01]


print("NOTAS:")

for nota in L1:
    qtd = int(Valor // nota)
    print("{} nota(s) de R$ {}.00".format(qtd, nota))
    Valor -= qtd * nota

print("MOEDAS:")
for moeda in L2:
    qtd = int(Valor // moeda)
    print("{} moeda(s) de R$ %.2f".format(qtd) % moeda)
    Valor -= qtd * moeda