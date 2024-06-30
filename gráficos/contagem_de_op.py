import matplotlib.pyplot as plt
import math

# Definindo os dados
x = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
y = [284, 1043, 5980, 23628, 92633, 566504, 2265431, 9042733, 56459551, 225547121]

# Plotando os dados
plt.style.use('fivethirtyeight')
plt.plot(x, y, color='r')

# Adicionando títulos e labels
plt.title('Contagem de Operações')
plt.xlabel('Catálogos')
plt.ylabel('Operações')

# Exibindo o gráfico
plt.show()