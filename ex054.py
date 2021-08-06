from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for ano in range(0,7):
    ano += 1
    nasc = int(input("Em que ano a {}º nasceu? ".format(ano)))
    idade = atual - nasc
    if idade >=21:
        totmaior += 1
    else:
        totmenor += 1
print("Ao todo tivemos {} pessoas maiores de idade".format(totmaior))
print("E também tivemps tivemos {} pessoas menores de idade".format(totmenor))


