# Implementação de Função para o Isolamento de Raízes
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt

# variável para determinar qual vai ser a função.
nomeDaFuncao = '5x^3 + x^2 - e^(1-2x) + cos(x) + 20'
print(f'Isolamento das raízes da função f(x) = {nomeDaFuncao}')
# a = Início do intervalo.
a = int(-5)
# b = Final do intervalo.
b = int(5)
# h = Amplitude do intervalo.
amplitude = float(0.5)
print(f'I=[{a},{b}] e Amplitude={amplitude}.')


def f(x):  # Função para isolamento das Raízes:
    return 5 * x**3 + x**2 - np.exp(1-2*x) + np.cos(x) + 20


# Valores de x:
valoresDeX = np.arange(a, b + amplitude, amplitude)

# Valores de y:
valoresDeY = [f(x) for x in valoresDeX]

# Criando a tabela com PrettyTable
tabela = PrettyTable()
tabela.field_names = ['x', 'f(x)']
tabela.float_format = ".4"  # Limitando para 4 casas decimais

for x, y in zip(valoresDeX, valoresDeY):
    tabela.add_row([x, y])

print(tabela)

# Criação do gráfico:
x = np.linspace(a, b, 100)
y = f(x)

plt.plot(x, y)
plt.scatter(valoresDeX, valoresDeY, color='red', label='Pontos para isolamento de raízes')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(
    f'Função f(x) = {nomeDaFuncao} no I=[{a}, {b}] e h={amplitude}')
plt.legend()
plt.grid(True)

# Exibir o gráfico interativamente na tela
plt.show()