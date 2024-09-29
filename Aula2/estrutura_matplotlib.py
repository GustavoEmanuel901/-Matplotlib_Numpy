#matplotlib

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, np.pi, 500)
y = np.cos(4*t)
y1 = np.sin(4*t)

plt.figure('cosseno', figsize=(5,4))
plt.plot(t, y)
plt.title('Gráfico do cosseno')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.savefig('grafico_cos.png') 

plt.figure('seno', figsize=(5,4))
plt.plot(t, y1)
plt.title('Gráfico do Seno')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.savefig('grafico_sen.png') 