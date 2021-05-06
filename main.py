def lavarCarro(posicao):
    print(f'Lavando carro na posição {posicao}')

def verificarTemCarroNaFila(posicao):
    if(posicao > 5):
        return False
    else:
        return True

if __name__ == '__main__':
    '''#Estrutura de repetição com intervalo de valores

    ##For Crescente
    print('For crescente')
    for n in range(0, 5):
        print(n)

    ##For decrescente
    print('For decescente')
    for n in range(5, 0, -1):
        print(n)
    print('For decescente')
    palavra ='Devaria'
    for p in palavra:
        print(p)

    ##Estrutura de repetição while crescente
    print('while crescente')
    n = 0
    while n <5:
        print(n)
        n = n+1
        '''
    #Estrutura de repetição com While
    temCarroNaFila = True
    posicao = 1
    while temCarroNaFila:
        lavarCarro(posicao)
        posicao = posicao + 1
        temCarroNaFila = verificarTemCarroNaFila(posicao)
    else:
        print('Terminou de lavar o carro')
