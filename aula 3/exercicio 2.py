print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('pressione qualquer outra tecla para sair.')

op = input('Qual operação deseja realizar? ')
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))

if op == '+':
    print(f'{x} + {y} = {x + y}')
elif op == '-':
    print(f'{x} - {y} = {x - y}')
elif op == '*':
    print(f'{x} * {y} = {x * y}')
elif op == '/':
    print(f'{x} / {y} = {x / y}')
else:
    print('Encerrando o programa...')