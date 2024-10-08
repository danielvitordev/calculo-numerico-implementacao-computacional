# Implementação do Método da Falsa Posição:
from prettytable import PrettyTable
import time


# Função que encontrará a raiz por meio do metodo da Falsa Posição:
def falsaPosicao(a, b, precisao, maxIteracoes, f):
    # Medindo o tempo de início do cálculo
    inicioTempo = time.time()

    if f(a) * f(b) >= 0:
        raise ValueError(
            "Os valores de 'a' e 'b' devem ser tais que f(a) * f(b) < 0.")

    # Gerando a tabela
    tabelaResultados = PrettyTable()
    tabelaResultados.field_names = [
        'Iteração', 'a', 'b', 'x', 'f(a)', 'f(b)', 'f(x)', '|f(x)|']
    tabelaResultados.float_format = ".5"  # Limitando para 5 casas decimais

    # Inicializando raizConvergente como None
    raizConvergente = None

    for i in range(maxIteracoes):
        x = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
        tabelaResultados.add_row(
            [i, a, b, "{:.5f}".format(x), f(a), f(b), f(x), abs(f(x))])

        if abs(f(x)) < precisao:
            raizConvergente = x
            break  # Sai do loop quando a precisão é atingida
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x

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
