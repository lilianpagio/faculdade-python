v1 = float(input('Digite o lado A: '))
v2 = float(input('Digite o lado B: '))
v3 = float(input('Digite o lado C: '))

if (v1 > 0 and v2 > 0 and v3 > 0) and (v1 + v2 > v3 and v1 + v3 > v2 and v2 + v3 > v1):
    #se chegou ate aqui é porque o triangulo é válido!
    if v1 != v2 and v1 != v3 and v2 != v3:
        print('TRIANGULO ESCALENO')

    else:
        if v1 == v2 and v2 == v3:
            print('TRANGULO EQUILÁTERO')
        
        else:
            print('TRIANGULO ISOSCELES')
else:
    print('Ao menos um dos valores indicados não servem para formar um trianglo.')