peso = float(input("Qual é o seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (m) "))
imc = peso / (altura**2)
if imc < 18.5:
    print("Abaixo do peso.")
elif 18.5 <= imc <25:
    print("Peso normal.")
elif 25 <= imc < 30:
    print("Sobrepeso.")
elif 30 <= imc < 40:
    print("Obesidade.")
else:
    print("Obesidade Mórbida.")



