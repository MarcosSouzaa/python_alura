# Jogo de Adivinhação
print("********************************************")
print('Jogo de advinhação!')
print("********************************************")

numero_secreto = 5

chute = int(input('Digite um número de 0 a 10: '))

print('\nNossa!! Você digitou o número ', chute)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto


if acertou:
    print('\nParabéns! Você acertou! Seu dia será ótimo!')
else:
    if maior:
        print('\nVocê errou feio! Seu número é maior que o Número secreto!!!')

    elif menor:
        print('\nVocê errou feio! Seu número é menor que o Número secreto!!!')

print('\nFim de jogo!')
