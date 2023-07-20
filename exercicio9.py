#Exercício 09:
#Faça o mesmo que antes, porém, ao invés de ler 10 números, o programa deverá ler e somar números até que o valor
#digitado seja zero.

def somaInteiro():
    soma = 0
    num = 1
    while(num != 0):
        num = int(input("Informe um número: "))
        soma += num
    return soma 

