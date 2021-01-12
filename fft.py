import index

from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np

output = index.stabilized
data = index.data

fftd = fft(output)

plt.plot(np.abs(fftd))
# >>> plt.grid()
plt.show()