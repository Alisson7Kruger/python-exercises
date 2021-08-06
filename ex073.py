time = ("Corinthians", "Palmeiras", "Santos", "Grêmio",
        "Cruzeiro", "Flamengo", "Vasco", "Chapecoense",
        "Atlético", "Botafogo", "Atlético-PR", "Bahia",
        "São Paulo", "Fluminense", "Sport Recife",
        "EC Vitória", "Coritiba", "Avaí", "Ponte Preta",
        "Atlético-GO")
print("=-="*10)
print(f"Lista de times do Brasileirão: {time}")
print("=-="*10)
print(f"Os 5 primeiros são {time[:5]}")
print("=-="*10)
print(f"Os últimos 4 são {time[-4:]}")
print("=-="*10)
print(f"Times em ordem alfabética: {sorted(time)}")
print("=-="*10)
print(f'O chapecoense está na {time.index("Chapecoense")+1}ª posicão')

