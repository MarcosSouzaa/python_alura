# Jogo de Adivinhação utilizando FOR e usando a biblioteca random/radint

from random import randint

print("********************************************")
print('Jogo de advinhação!')
print("********************************************")

numero_secreto = randint(0, 10)
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('\nDigite um número de 0 a 10: '))
    print('\nVocê digitou o número ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('\nParabéns! Você acertou! Seu dia será ótimo!')
        break
    else:
        if maior:
            print('\nVocê errou, Seu número é maior que o Número secreto!!!')

        elif menor:
            print('\nVocê errou! Seu número é menor que o Número secreto!!!')

print('')
print('O NÚMERO "{}" É O NÚMERO SECRETO!'.format(numero_secreto))
print('\nFim de jogo!')
