import pytest
import numpy as np
from src.filters.butterworth import butterworth_bandpass


def test_butterworth_filter():
    # 生成测试信号：10Hz正弦波 + 噪声
    fs = 1000
    t = np.arange(0, 1, 1 / fs)
    signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.random.randn(len(t))

    # 应用8-12Hz带通滤波
    filtered = butterworth_bandpass(signal, lowcut=8, highcut=12, fs=fs)

    # 验证滤波后信号能量集中在通带
    fft_raw = np.abs(np.fft.fft(signal))
    fft_filt = np.abs(np.fft.fft(filtered))
    assert np.sum(fft_filt[8:13]) > 0.8 * np.sum(fft_raw[8:13])