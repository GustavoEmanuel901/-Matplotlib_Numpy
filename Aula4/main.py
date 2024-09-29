import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)
c = np.cos(x)
s = np.sin(x)

plt.figure('Graficos', figsize=(8, 4))
plt.subplots_adjust(
    left=0.152,
    right=0.943,
    top=0.92,
    bottom=0.122,
    hspace=0.4,
    wspace=0.438,
)

ax1 = plt.subplot(1, 2, 1)
ax1.set_title('Cosseno')
ax1.set_xlabel('Tempo')
ax1.set_ylabel('Amplitude') 
ax1.grid() 
plt.plot(x, c)

ax2 = plt.subplot(1, 2, 2)
ax2.set_title('Seno')
ax2.set_xlabel('Tempo')
ax2.grid()
ax2.set_ylabel('Amplitude')
plt.plot(x, s)

plt.savefig('gráfico_sen_cos.png')