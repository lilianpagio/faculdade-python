while True:
    nome = input('Qual o seu nome? ')
    if nome != 'Lilian':
        continue #volta para o inicio do laço

    senha = input('Qual a sua senha? ')
    if (senha == 'Lilian123'):
        break #encerra o laço

print('Acesso concedido.')