#Exercício 6:
#Faça um algoritmo que escreva na tela os numeros de um numero inicial a um numero final.Os numeros inicial e final devem
    # ser informados pelo usuario.
def exercicio06(inicio,fim):
    if(inicio > fim):
        for i in range(inicio,fim-1, -1):
            print(i)
    else:
        for i in range(inicio, fim+1):
            print(i)