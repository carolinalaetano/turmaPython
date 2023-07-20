from exercicio4 import somarInteiro
from exercicio5 import tabuada
from exercicio5 import coletarPositivo
from exercicio6 import exercicio06
from exercicio7 import exercicio07
from exercicio8 import somarInteiro
from exercicio9 import somaInteiro
from exercicio10 import media
from exercicio11 import inteiros
from exercicio12 import positivoNegativo
from exercicio13 import fatorial
from vetores import preencherVetor
from vetores import consultarVetor
from vetores import apagarPosicao
from exercicio14 import jogadores
from exercicio15 import miss
from exercicio16 import eleicao


def mostrarMenu():
    print('\n\n\nEscolha uma das opções abaixo: ' +
          '\n0. SAIR'         +
          '\n1. Exercício 01' +
          '\n2. Exercício 02' +
          '\n3. Exercício 03' +
          '\n4. Exercício 04' +
          '\n5. Exercício 05' +
          '\n6. Exercício 06' +
          '\n7. Exercício 07' +
          '\n8. Exercício 08' +
          '\n9. Exercício 09' +
          '\n10. Exercício 10' +
          '\n11. Exercício 11' +
          '\n12. Exercício 12' +
          '\n13. Exercício 13' +
          '\n14. Exercício 14' +
          '\n15. Exercício 15' +
          '\n16. Exercício 16' +
          '\n17. Exercício 17' +
          '\n18. Exercício 18' +
          '\n19. Exercício 19' +
          '\n20. Exercício 20' +
          '\n21. Preencher Vetor' +
          '\n22. Consultar Vetor' +
          '\n23. Apagar posição Vetor')

def operacao():
    #Chamar o método de cima (mostrarMenu):
    opcao = 1 #Instanciar = dar o valor inicial
    while(opcao != 0):
        mostrarMenu()
        #Coletar a opção do usuário:
        opcao = int(input('Digite aqui o número da opção escolhida: '))
        #Executar a ação:
        if(opcao == 0):
            #Instruções do exercício 01:
            print("Obrigado!")
        elif(opcao == 1):
            return
        elif(opcao == 2):
            return
        elif (opcao == 3):
            return
        elif (opcao == 4):
            # Exercicio 4:
            print('\nExercício 04')
            print(somarInteiro())
        elif (opcao == 5):
            print('\nExercício 05')
            num = int(input("Informe um número: "))
            n = coletarPositivo()
            # Passar os dois números na função:
            tabuada(num, n)
        elif (opcao == 6):
            # Executando as funcoes:
            print('\nExercício 06')
            inicio = int(input("Informe o início: "))
            fim = int(input("Informe o final: "))
            exercicio06(inicio, fim)  # Chamando o método criado
        elif (opcao == 7):
            print('\nExercício 07')
            exercicio07()
        elif (opcao == 8):
            print('\nExercício 08')
            print(somarInteiro())  # Tem um return, então precisa de um print aqui.
        elif (opcao == 9):
            print('\nExercício 09')
            print(somaInteiro())
        elif (opcao == 10):
            print('\nExercício 10')
            print(media())
        elif (opcao == 11):
            print('\nExercício 11')
            print(inteiros())
        elif (opcao == 12):
            print('\nExercício 12')
            print(positivoNegativo())
        elif (opcao == 13):
            print('\nExercício 13')
            print(fatorial())
        elif (opcao == 14):
            print('\nExercício 14')
            print(jogadores())
        elif (opcao == 15):
            print('\nExercício 15')
            print(miss())
        elif (opcao == 16):
            print('\nExercício 16')
            print(eleicao())
        elif (opcao == 17):
            print('\nExercício 17')

        elif (opcao == 18):
            print('\nExercício 18')

        elif (opcao == 19):
            print('\nExercício 19')

        elif (opcao == 20):
            print('\nExercício 20')

        elif(opcao == 21):
            num = int(input("Informe o tamanho do vetor: "))
            preencherVetor(num)
        elif(opcao == 22):
            num = int(input("Informe o tamanho do vetor: "))
            consultarVetor(num)
        elif(opcao == 23):
            posicao = int(input('Informe a posição que deseja apagar: '))
            apagarPosicao(posicao-1) #para apagar um vetor, sempre vai ser a posição -1.
        else:
            print('Opção escolhida não é válida, digite novamente!')
