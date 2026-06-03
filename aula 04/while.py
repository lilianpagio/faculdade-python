inicio = int(input("Qual valor deseja iniciar a contagem? "))
fim = int(input("Qual valor deseja encerrar a contagem? "))
intervalo = int(input("De quanto em quanto você deseja contar? "))

cont = inicio

while cont <= fim:
    #verificar se o numero é par
    if cont % 2 == 0:
        print(cont)
    cont = cont + intervalo