frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
print("Voce digitou a frase {}".format(junto))
inverso = junto[::-1]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
