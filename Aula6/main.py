from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 70)
y = np.cos(4*x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, color='red', lw=3, marker='o', linestyle='--')
plt.grid(True)
plt.title('Gráfico do Cosseno')
plt.xlabel('Eixo do Tempo')
plt.ylabel('Eixo de Amplitude') 
plt.savefig('gráfico_cosseno.png')
