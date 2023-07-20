#Exercício 13:
#Escreva um programa que lido um número, calcule e informe o seu fatorial.Ex.: 5!=5*4*3*2*1=120.
def fatorial():
    i = 0
    num = int(input('Informe um número: '))
    for i in range(num,1,-1):
        print('{} * {} = {}'.format(num,i-1,num *(i - 1)))
        num *= i - 1


