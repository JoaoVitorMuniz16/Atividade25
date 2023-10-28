soma = 0
for x in range(0, 6):
    n = int(input('Número: '))
    if n % 2 == 0:
        soma += n
print(soma)