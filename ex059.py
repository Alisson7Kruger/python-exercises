from time import sleep
n1 = int(input("1º valor: "))
n2 = int(input("2º valor: "))
opção = 0
while opção != 5:
    print("[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa")
    opção = int(input(">>>>>Qual é a sua opção? "))
    if opção == 1:
        soma = n1 + n2
        print("A soma entre {} + {} é {}".format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print("O resultado de {} x {} é {}".format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("Entre {} e {} o maior valor é {}".format(n1, n2, maior))
    elif opção == 4:
        print("Informe os números novamente: ")
        n1 = int(input("1º valor: "))
        n2 = int(input("2º valor: "))
    elif opção == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente.")
    print("=-=" * 10)
    sleep(2)
print("Fim do programa! Volte sempre!")


