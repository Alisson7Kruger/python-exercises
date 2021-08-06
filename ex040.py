nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1+nota2) / 2
print("Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}".format(nota1, nota2, media))
if media < 5.0:
    print("O aluno está REPROVADO!")
elif media > 7.0:
    print("O aluno está APROVADO!")
else:
    print("O aluno está em RECUPERAÇÃO!")
