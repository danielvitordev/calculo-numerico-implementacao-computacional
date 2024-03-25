# Implementação do método de Eliminação de Gauss
import numpy as np
from prettytable import PrettyTable


def eliminacaoDeGauss(A, b):
    # Determina a ordem da matriz contando o número de linhas
    n = A.shape[0]

    # Concatena a matriz A com o vetor b
    Ab = np.column_stack((A, b))

    # Contador para o número de iterações
    NumeroIteracoes = 0

    # Eliminação de Gauss
    for i in range(n):
        # Pivô é o elemento da diagonal principal
        pivo = Ab[i, i]
        # Se o pivô for zero, então vai ocorrer uma divisão por zero, encerrando a execução
        if pivo == 0:
            print('Erro: divisão por zero!')
            exit()

        # Zera os elementos abaixo do pivô na coluna i
        for j in range(i+1, n):
            multiplicador = Ab[j, i] / pivo
            Ab[j, i:] = Ab[j, i:] - multiplicador * Ab[i, i:]

        # Incrementa o contador de iterações
        NumeroIteracoes += 1

    # Fase de Retrosubstituição
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:])) / Ab[i, i]

    # Calcula o vetor de resíduos
    r = np.dot(A, x) - b

    # Calcula o resíduo por distância relativa
    residuo_relativo = np.linalg.norm(r) / np.linalg.norm(b)

    # Exibição da solução
    print('A solução do sistema é: ')
    table = PrettyTable()
    table.field_names = ['xi', 'x']
    for i in range(len(x)):
        table.add_row([f'x{i+1}', f'{x[i]:.2f}'])
    print(table)

    # Exibir o número de iterações
    print(f'Número de iterações: {NumeroIteracoes}')

    # Exibir o resíduo por distância relativa
    print(f'Resíduo: {residuo_relativo}')

    return x, residuo_relativo
