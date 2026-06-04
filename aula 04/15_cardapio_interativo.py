print('-------------------------')
print('|       CARDÁPIO        |')
print('-------------------------')
print('[1] Coxinha......R$5,00 |')
print('[2] Pastel.......R$7,00 |')
print('[3] Café.........R$4,00 |')
print('[4] Suco.........R$6,00 |')
print('[5] SAIR                |')
print('|_______________________|')

total = 0
while True:
    
    op = int(input('Digite o número do item. '))

    if op >= 1 and op <= 4:
        qtd = int(input('Quantas unidades deseja comprar? '))
    elif op == 5:
        print('Saindo do sistema...')
        break
    else:
        print('Produto inválido. Selecione outra opção.')
        
    if op == 1:
        total = total + qtd * 5.00
    elif op == 2:
        total = total + qtd * 7.00
    elif op == 3:
        total = total + qtd * 4.00
    elif op == 4:
        total = total + qtd * 6.00
    
print('.................................................')
print(f'O total a ser gasto neste pedido é de R${total:.2f}.')
print('.................................................')
