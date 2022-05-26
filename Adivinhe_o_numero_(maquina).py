# Acerte o numero gerado pela maquina!
import random
def chute(x):
    random_number = random.randint(1,x)
    chute = 0
    vidas = 3
    while chute != random_number:
        chute = int(input("chute um numero entre 1 e {}: ".format(x)))
        if chute < random_number:
            print("Muito baixo, tente novamente")
            vidas -= 1
            print('Tentativas restantes: {}'.format(vidas))
        if chute > random_number:
            print("Muito alto, tente novamente".format(vidas))
            vidas -= 1
            print('Tentativas restantes: {}')
        if chute == random_number:
            print("Parabens você acertou o número aleatório: '{}'".format(random_number))
        elif vidas == 0:
            print("Você não conseguiu adivinhar o numero :/")
            break
chute(10)
