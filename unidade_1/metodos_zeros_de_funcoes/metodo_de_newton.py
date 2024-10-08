from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt
import time


# Função que encontrará a raiz por meio do metodo de Newton:
def Newton(a, b, x, f, precisao, maxIteracoes):
    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    # Definindo a função da derivada numérica de f(x)
    def derivadaNumericaDeF(x, h=0.0001):
        # h=0.0001, é um valor muito próximo de zero, para que não ocarra um erro de indeterminação na função e assim pode calcular a derivada númerica
        return (f(x + h) - f(x)) / h

    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = ['Iteração', 'x', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".5"  # Limitando para 5 casas decimais

    raizConvergente = None

    # Palpite inicial para descobrir o valor de x:
    x0 = (a + b) / 2

    # Inicializa o valor de x com o palpite inicial x0
    x = x0

   # Loop para as iterações
    for numIteracoes in range(maxIteracoes):
        valorDef = f(x)

        # Adiciona a iteração atual à tabela
        tabelaResultados.add_row(
            [numIteracoes, x, valorDef, abs(valorDef)])

        # Condição para quando a raiz convergir parar o loop
        if abs(valorDef) < precisao:
            raizConvergente = x
            break

        # Calculando a derivada de numérica de f(x)
        derivadaNumerica = derivadaNumericaDeF(x)
        # Verificando se a derivade numérica é igual a 0, para evitar erros.
        if derivadaNumerica == 0:
            print("Derivada é zero. Escolha outro palpite inicial.")
            return None

        x = x - (valorDef / derivadaNumerica)

        if abs(valorDef) < precisao:
            raizConvergente = "{:.5f}".format(x)
            break

    else:
        print("\nO número máximo de iterações foi atingido.")

    # Imprimindo a tabela de resultados
    print(tabelaResultados)

    # Verificando se a raiz convergente foi encontrada:
    if raizConvergente is not None:
        print(f'\nRaiz convergente encontrada foi: {raizConvergente:.5f}')
    else:
        print('\nNão foi possível encontrar uma raiz convergente dentro do número máximo de iterações.')

    # Medindo o tempo de fim do cálculo
    fimTempo = time.time()

    # Calculando e mostrando o tempo total de cálculo
    tempoTotal = fimTempo - inicioTempo
    print(f'\nO tempo de execução foi de {tempoTotal:.6f} segundos.')

    return tabelaResultados, raizConvergente
