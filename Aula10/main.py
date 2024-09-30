import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

x = np.linspace(1, 5, 500)
y = np.log10(x)

fig, axe = plt.subplots(figsize=(7,4))
axe.text(2.9, 0.35, 'P(2.5, 0,4)')
axe.text(3, 0.42, 'Logaritmo $ y = log_{10}x$', fontsize='10', bbox=dict(facecolor='red', alpha=0.5))
axe.annotate('P(2.5; 0.4) ', xy=(2.5,0.4), fontsize='16', xytext=(0.5,0.5), arrowprops=dict(facecolor='red'), color='red')
axe.plot(x, y, lw=1.2)
axe.plot([0, 2.5], [0.4, 0.4], color='gray', linestyle='--', lw=0.8)
axe.plot([2.5, 2.5], [0,0.4], color='gray', linestyle='--', lw=0.8)
axe.plot(2.5, 0.4, marker='o', color='gray')
axe.set_xticks(np.arange(1, 5.5, 0.5))
axe.set_title('Gráfico do Logaritmo Natural', fontsize=16)
axe.set_xlabel('Eixo X', fontsize=12)
axe.set_ylabel('Eixo Y', fontsize=12)
plt.savefig('gráfico_logaritmo.png')
 