print('R - Residencial')
print('C - Comercial')
print('I - Industrial')

kwh = float(input('Quantos kWh? '))
inst = input('Qual o tipo de instalaçao? (R, C, I) ')

if inst == 'R':
    if kwh <= 500:
        preco = 0.40
        print(f'VALOR A PAGAR = {kwh * preco}')
    else:
        preco = 0.65
        print(f'VALOR A PAGAR = {kwh * preco}')

elif inst == 'C':
    if kwh <= 1000:
        preco = 0.55
        print(f'VALOR A PAGAR = {kwh * preco}')
    else:
        preco = 0.60
        print(f'VALOR A PAGAR = {kwh * preco}')

elif inst == 'I':
    if kwh <= 5000:
        preco = 0.55
        print(f'VALOR A PAGAR = {kwh * preco}')
    else:
        preco = 0.60
        print(f'VALOR A PAGAR = {kwh * preco}')

else:
    print('Instalação inváda. Encerrando...')