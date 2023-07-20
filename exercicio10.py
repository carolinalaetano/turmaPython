#Exercício 10:
#Escreva um algoritmo que calcule a média dos números digitados pelo usuário, se eles forem pares. Termine a leitura se
#o usuário digitar zero.

def media():
    num = 2
    soma = 0
    i = 0
    while (num != 0):
        num = int(input("Informe um número: "))
        if(num % 2 == 0):
            soma += num
            i += 1
    return soma / i


