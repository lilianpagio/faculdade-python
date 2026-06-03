nome = input('Escreva o seu nome: ')
idade = int(input('Diga sua idade: '))

if nome == 'vinicius':
    print('Vinicius')

elif idade < 18:
    print (f'{nome} é menor de idade')

elif idade > 100:
    print ('Essa pessoa possivelmente não existe.')