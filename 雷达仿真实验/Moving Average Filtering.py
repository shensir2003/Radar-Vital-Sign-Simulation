import numpy as np
from matplotlib import pyplot as plt

from 雷达仿真实验.test import radar_signal, t


def moving_average_filter(signal, window_size=50):
    window = np.ones(window_size) / window_size
    return np.convolve(signal, window, mode='same')


# 应用滤波
filtered_signal = moving_average_filter(radar_signal)

# 可视化对比
plt.figure(figsize=(12, 6))
plt.plot(t, radar_signal, alpha=0.5, label='Raw')
plt.plot(t, filtered_signal, 'r', label='Filtered')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Moving Average Filter (Window Size=50)')
plt.legend()
plt.savefig('filter_ma.png', dpi=300)
plt.close()
