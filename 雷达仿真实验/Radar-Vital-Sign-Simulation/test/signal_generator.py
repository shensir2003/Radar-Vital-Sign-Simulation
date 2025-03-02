import numpy as np
import matplotlib.pyplot as plt

# 参数设置
fs = 1000          # 采样率 1000Hz (模拟雷达常用范围)
t = np.arange(0, 10, 1/fs)  # 10秒信号时长

# 生成呼吸信号（0.1-0.5Hz）
f_breath = 0.2     # 0.2Hz呼吸频率 (12次/分钟)
amp_breath = 1.2   # 呼吸幅度
breath_signal = amp_breath * np.sin(2 * np.pi * f_breath * t)

# 生成心跳信号（0.8-2Hz）
f_heart = 1.2      # 1.2Hz心跳频率 (72次/分钟)
amp_heart = 0.3    # 心跳幅度（通常比呼吸弱）
heart_signal = amp_heart * np.sin(2 * np.pi * f_heart * t)

# 生成运动干扰（突发性高频噪声）
motion_noise = 0.5 * np.random.normal(size=len(t))  # 高斯白噪声
motion_noise[3000:4000] += 2.0 * np.sin(2 * np.pi * 5 * t[3000:4000])  # 5Hz肢体运动

# 合成雷达信号
radar_signal = breath_signal + heart_signal + motion_noise

# 添加系统噪声
radar_signal += 0.2 * np.random.normal(size=len(t))  # 模拟雷达热噪声

# 可视化
plt.figure(figsize=(12, 6))
plt.plot(t, radar_signal, label='Raw Radar Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Synthetic Radar Signal with Motion Artifact')
plt.legend()
plt.savefig('radar_signal.png', dpi=300)
plt.close()