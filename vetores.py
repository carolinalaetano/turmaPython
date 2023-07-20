notas = []  #Vetor global = todas as funções podem visualizar/usar esse vetor

def preencherVetor(fim):
    for i in range(fim):
        num = int(input("Informe a {}ª nota: ".format(i+1)))
        notas.append(num) #Adicionando notas no vetor

def consultarVetor(fim): #O usuário precisa digitar o fim.
    for i in range(fim):
        print('{}ª Posiçaõ: {}'.format(i+1,notas[i]))


def apagarPosicao(posicao): #O usuário precisa digitar a posição.
    if (len(notas) < posicao):
        print("Impossível remover, pois o tamanho é menor que a posição.")
    else:
        del(notas[posicao]) #Excluindo um dado do vetor
        print("Removido com sucesso!")
