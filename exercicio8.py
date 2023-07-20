#Exercício 8:
#Escrever um algoritmo que leia 10 números inteiros e, ao final, apresente a soma de todos os números lidos.

def somarInteiro():
    soma = 0      # A soma começa em zero, valor inicial da soma.
    for i in range(1,11,1):
        num = int(input("{}° número: ".format(i)))
        soma += num
    return "A soma dos números digitados foi {}".format(soma)


