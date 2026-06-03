cont = 1
soma = 0

while cont <= 5:
    nota = float(input(f"Digite a {cont}ª nota: "))
    soma += nota #Equivale: soma = soma + nota
    cont += 1 #Equivale: cont = cont + 1
media = soma / 5
print(f"A Media Final da disciplina foi de {media}")