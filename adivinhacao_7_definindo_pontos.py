# Jogo de Adivinhação Definindo pontos por rodada

from random import randint

print("********************************************")
print('Jogo de advinhação!')
print("********************************************")

numero_secreto = randint(0, 100)
print('O NÚMERO "{}" É O NÚMERO SECRETO!'.format(numero_secreto))
total_de_tentativas = 0
pontos = 1000

print('\nQual o nível de dificuldade?')
print('\n(1) Fácil, (2) Médio, (3 )Difícil\n')

nivel = int(input('Defina o nível: '))
if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))

    chute = int(input('\nDigite um número de 0 a 100: '))
    print('\nVocê digitou o número ', chute)

    if chute < 0 or chute > 100:
        print('\n"VOCÊ DEVE DIGITAR UM NÚMERO DE 0 a 10!"')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('\nParabéns! Você acertou e fez {} pontos!'.format(pontos))
        print('Seu valor máximo de pontos é 1000.')
        break
    else:
        if maior:
            print('\nVocê errou, Seu número é maior que o Número secreto!!!')

        elif menor:
            print('\nVocê errou! Seu número é menor que o Número secreto!!!')

        # Aqui uso a função abs() valor absoluto para considerar as diferenças entre -X e +X
        # ou seja, se meu nº secreto for menor que o chute ex: 20-60 = -40 vou considerar 40
        pontos_perdidos = abs(numero_secreto-chute)
        pontos = pontos - pontos_perdidos

print('')
print('O NÚMERO "{}" É O NÚMERO SECRETO!'.format(numero_secreto))
print('\nFim de jogo!')
