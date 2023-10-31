# Usando a formatação normal
print('Tentativa {} de {}'.format(1, 3))  # imprime Tentativa 1 de 3

# Usando a formatação invertendo a ordem através dos índices
print('Tentativa {1} de {0}'.format(1, 3)) # Tentativa 3 de 1

# Formatação de valores financeiros
print('R${}'.format(1.59)) # imprime: R$1.59

# Utilizando a formatação para float
print('R${:f}'.format(1.59)) # imprime: R$1.590000

# depois do ponto, quero apenas dois dígitos
print('R${:.2f}'.format(1.59)) # imprime: R$1.59

# contando 7 caracteres
print('R${:7.2f}'.format(1.59)) # imprime: R$   1.59

# contando 7 caracteres, mas vamos preencher de zeros na frente
print('R${:07.2f}'.format(1.59)) # imprime: R$0001.59

# formatando número inteiro, usa-se o "d"
print('R${:07d}'.format(4)) # imprime: R$0000004

# formatando data
print('Data {:02d}/{:02d}'.format(9, 4)) # Data 09/04

print('R$ {:7.1f}'.format(1000.12))
print('R$ {:07.2f}'.format(4.11))
