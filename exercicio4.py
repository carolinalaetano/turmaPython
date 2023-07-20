#Exercício 4:
#Faça um algoritmo que calcule a soma dos números inteiros de 1 a 100
def somarInteiro():
    soma = 0
    for i in range(101):
        print(i)
        soma += i

    return 'A soma dos elementos entre 1 e 100 é: {}.format(soma)'