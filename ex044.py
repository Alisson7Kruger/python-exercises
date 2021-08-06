print("="*10, "LOJAS KRUGER", "="*10)
preço = int(input("Preço das compras: R$"))
print("""FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
opção = int(input("Qual é a opção?"))
if opção == 1:
    print("Sua compra de {:.2f} vai custar {:.2f} no final.".format(preço, preço-(preço*10/100)))
elif opção == 2:
    print("Sua compra de {:.2f} vai custar {:.2f} no final.".format(preço, preço-(preço*5/100)))
elif opção == 3:
    print("Sua compra de {:.2f} vai custar {:.2f} no final.".format(preço, preço))
elif opção == 4:
    parcelas = int(input("Quantas parcelas? "))
    mensalidade = preço / parcelas
    print("Sua compra será parcelada em {}x de {:.2f} COM JUROS".format(parcelas, mensalidade+(mensalidade*20/100)))
    print("Sua compra de {} vai custar {} no final".format(preço, preço+(preço*20/100)))
else:
    total = 0
    print("Opção inválida de pagamento. Tente novamente")

