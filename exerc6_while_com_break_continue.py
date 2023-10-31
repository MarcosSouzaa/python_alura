# Iterando com while
i = 1
while (i <= 7):
    print(i)
    i = i + 1
    if (i == 5):
        break
# Saída no console (sai antes de imprimir o 5
# 1
# 2
# 3
# 4

# Iterando com for
for i in range(1, 8):
    if (i == 5):
        continue
    print(i)
# se i for igual a 5 ele para a iteração e volta para o início do laço.
# 1
# 2
# 3
# 4
# 6
# 7
