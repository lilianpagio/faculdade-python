print('Escolha o que deseja compra: ')
print('1 | Maçã')
print('2 | Laranja')
print('3 | Banana')

produto = int(input('Qual a sua escolha? '))
qtde = int(input('Quantas unidades? '))

if (produto == 1): #maçã
    valor = float(qtde * 2.30)
    print (f'Você escolheu {qtde} unidades de maçã. Total a pagar será de R${valor: .2f}.')

else:
    if (produto == 2): #laranja
        valor = float(qtde * 3.60)
        print(f'Você escolheu {qtde} unidades de laranja. Total a pagar será de R${valor: . 2f}.')
    
    else:
        if (produto == 3): #banana
            valor = float(qtde * 1.85)
            print (f'Você escolheu {qtde} unidades de banana. Total a pagar será de R${valor: .2f}.')

        else:
            print('Produto inexistente.')