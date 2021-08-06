casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = float(input("Quantos anos de financiamento? R$"))
prestação = casa / (anos * 12)
mínimo = salario * 30 / 100
print("Para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f}".format(casa, anos, prestação ))
if prestação <= mínimo:
    print("Empréstimo CONCEDIDO!")
else:
    print("Empréstimo NEGADO")
