# Pense em um numero e veja a maquina acertar!
import random

print("Pense em um numero entre 1 e 10")
def Chute_computador (x):
    menor = 1
    maior = x
    retorno = ''
    vidas = 3
    while retorno != 'c'and menor != maior :
        chute = random.randint(menor, maior)
        retorno = input('Se o Chute: {}, for muito alto digite (A), se for muito baixo digite (B), caso esteja correto (C)'.format(chute)).lower()
        if retorno == 'a':
            maior = chute -1
            vidas -= 1
            print('Tentativas restantes: {}'.format(vidas))
        if retorno == 'b':
            menor = chute +1
            vidas -= 1
            print('Tentativas restantes: {}'.format(vidas))
        if retorno == 'c':
            print('O computador conseguiu acertar seu Numero!!')
        elif vidas == 0:
            print('O computador não conseguiu acertar seu numero :c ')
            break
Chute_computador(10)

