#Exercício 11:
#Escreva um algoritmo que leia valores inteiros e encontre o maior e o menor deles. Termine a leitura se o usuário
#digitar zero.

def inteiros():
    i = 0
    num = 1
    while (num != 0):
        num = int(input("Informe um número: "))

        if(i == 0):
            maior = num
            menor = num
            i = 1

        if(num>maior):
            maior = num

        if(num<menor):
            menor = num

    return "O maior número é: {} e o menor número é: {}".format(maior, menor)
