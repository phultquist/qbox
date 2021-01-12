import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
import numpy as np
rate, data = wav.read('100hz.wav')
fft_out = np.fft.fft(data)
# %matplotlib inline
plt.plot(data, np.abs(fft_out))
plt.show()