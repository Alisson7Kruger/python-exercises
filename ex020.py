from random import shuffle
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segunfo Aluno: "))
n3 = str(input("Terceiro Aluno: "))
n4 = str(input("Quarto Aluno: "))
lista = [n1, n2, n3, n4]
shuffle(lista)
print("A ordem de apresentação será {}")
print(lista)
