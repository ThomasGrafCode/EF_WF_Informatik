import numpy as np
from matplotlib import pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.subplot(2, 1, 1)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.xlabel('time (s)')
plt.ylabel('$e^{-t}\cos(2\pi t)$')
plt.title('Subplot 1')
plt.text(3., .3, '$e^{-t}\cos(2\pi t)$')

plt.subplot(2, 1, 2)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.xlabel('x-label subplot 2')
plt.ylabel('y-label subplot 2')
plt.title('Subplot 2')

plt.tight_layout()
plt.show()