#Exercício 12:
#Escreva um algoritmo que leia 20 valores inteiros e ao final exiba:
#a) a soma dos números positivos;
#b) a quantidade de valores negativos
def positivoNegativo():
    soma = 0
    quantidade = 0
    i = 0
    for i in range(1, 21, 1):
        if(i > 0):
            num = int(input("{}° número: ".format(i)))
            soma += num
        else:
            num = int(input("{}° número: ".format(i)))
            quantidade += 1

    return "A soma é: {} e o número é: {}".format(soma,num)
