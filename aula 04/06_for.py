soma = 0
qtde = 0
for i in range(1, 101):
    if (i % 2 == 0):
        soma += i
        qtde =+ i
    media = soma / qtde
    print(f'A media dos pares de 0 a 100 é: {media}')
