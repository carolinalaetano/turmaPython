#Exercício 15:
#Em um concurso de miss, os jurados precisam digitar o nome das 16 candidatas e suas respectivas notas(0 a 10). Crie um
#programa que leia essas informações e que, ao final do programa, apresente apenas o nome e a nota da vencedora.

def miss():
    flag = 0

    for i in range(1, 17, 1):
        num = int(input('A nota da {}º candidata é: '.format(i)))
        nome = input('O nome da {}º candidata é: '.format(i))

        if(flag == 0):
            maior = num
            flag = 1

        if (num > maior):
            maior = num
            maiorNome = nome

    return "O nome da candidata vencedora é: {} e a sua nota é: {}".format(maiorNome,maior)

