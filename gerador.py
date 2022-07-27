from random import randint
from time import sleep
print('-'*40)
print(f'{"PALPITES DA MEGA-SENA":^40}')
print('-'*40)
res = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = []

for c in range(1,res+1):
    for p in range(0,6):
        n = randint(0,60)
        if n in jogos:
            while n in jogos:
                n = randint(0,60)
        jogos.append(n)
    jogos.sort()
    print(f'Jogo {c}: {jogos}')
    jogos.clear()
    sleep(1)
