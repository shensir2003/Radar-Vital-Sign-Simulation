import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import fft, fftfreq

from test.signal_generator import radar_signal, fs

# 计算FFT
N = len(radar_signal)
yf = fft(radar_signal)
xf = fftfreq(N, 1/fs)[:N//2]

# 可视化频谱
plt.figure(figsize=(12, 6))
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.xlim(0, 10)  # 关注0-10Hz范围
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('FFT Analysis of Raw Radar Signal')
plt.grid()
plt.savefig('fft_raw.png', dpi=300)
plt.close()