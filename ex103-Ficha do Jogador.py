def ficha(jog='Desconhecido', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

#Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número do Jogador: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=0)
else:
    ficha(n, g)
