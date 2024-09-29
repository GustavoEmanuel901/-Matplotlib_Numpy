import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 500)
y = np.cos(t)
y1 = np.sin(t)

plt.figure('Gráfico', figsize=(6, 4))
plt.plot(t, y)
plt.plot(t, y1)
plt.title('Cosseno e Seno')
plt.xlabel('Eixo de Tempo (s)')
plt.ylabel('Eixo da Amplitude')
plt.grid()
plt.savefig('gráfico_sen_cos.png')