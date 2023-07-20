#Exercício14:
#Escreva um programa que leia um valor correspondente ao número de jogadores de um time de vôlei. O programa deverá ler
#uma altura para cada um dos jogadores e, ao final, informar a altura média do time.

def jogadores():
    i = 0
    num = 1
    soma = 0
        #Coletar as alturas:
    for i in range(1,11,1):
        num = float(input('A altura do {}º jogador é: '.format(i)))

        soma += num
    return 'A média do time é: {} '.format(soma/i)










