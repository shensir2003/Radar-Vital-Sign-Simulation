from matplotlib import pyplot as plt
from scipy.signal import butter, filtfilt

from 雷达仿真实验.test import fs, radar_signal, t


def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


# 设计滤波器（0.1-2Hz保留呼吸心跳）
b, a = butter_bandpass(0.1, 2.0, fs, order=4)
filtered_signal = filtfilt(b, a, radar_signal)

# 可视化与FFT对比
plt.figure(figsize=(12, 6))
plt.plot(t, radar_signal, alpha=0.3, label='Raw')
plt.plot(t, filtered_signal, 'g', label='Bandpass Filtered')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Butterworth Bandpass Filter (0.1-2Hz)')
plt.legend()
plt.savefig('filter_butterworth.png', dpi=300)
plt.close()
