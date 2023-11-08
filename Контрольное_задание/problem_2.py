import scipy
from scipy.signal import butter, filtfilt
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# Создание сигнала
t = np.arange(0,1,0.001)

fs = 1000
fc = 100
Ts = 1/fs
A = 5
w = 14 * np.pi * fc
x = A * np.cos(w * t)
plt.figure(1)
plt.title("Исходный сигнал")  
plt.plot(x)

# Получение набора отчетов размерами 64, 128, 256
n_64 = np.arange(0,64,1)
n_128 = np.arange(0,128,1)
n_256 = np.arange(0,256,1)

plt.figure(2, figsize = (12,8))
plt.suptitle("Дискретизация сигнала")
x_64 = A * np.cos(w*n_64*Ts)
plt.subplot(1,3,1)
plt.title("Кол-во отсчетов: 64")
plt.stem(n_64,x_64)

x_128 = A * np.cos(w*n_128*Ts)
plt.subplot(1,3,2)
plt.title("Кол-во отсчетов: 128")
plt.stem(n_128,x_128)

x_256 = A * np.cos(w*n_256*Ts)
plt.subplot(1,3,3)
plt.title("Кол-во отсчетов: 256")
plt.stem(n_256,x_256)

Q = 0.1 * np.pi
x_Q_01 = np.cos(Q *fs) / (2*np.pi)

Q = 0.3 * np.pi
x_Q_03 = np.cos(Q *fs) / (2*np.pi)


# ДПФ сигнал для наборов отчетов для n = 64, 128, 256
plt.figure(3,figsize = (12,8))
fft_64 = abs(np.fft.fft(x_64))
plt.subplot(1,3,1)
plt.plot(fft_64)
fft_128 = abs(np.fft.fft(x_128))
plt.subplot(1,3,2)
plt.plot(fft_128)
fft_256 = abs(np.fft.fft(x_256))
plt.subplot(1,3,3)
plt.plot(fft_256)


# Цифровая фильтрация

fs = 10000

t = np.arange(0, 1, 1/fs)

fc1 = 185
fc2 = 45

x1 = np.cos(50*np.pi*fc1*t)
x2 = np.cos(9*np.pi*fc2*t)
plt.figure(7)
plt.plot(x1[:100])
plt.figure(8)
plt.plot(x2[:100])
signal_2cos = x1+x2
plt.figure(4)
plt.plot(t[:100], signal_2cos[:100])
plt.suptitle("Сигнал суммы cos:")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')


# Compute the DFT of the signal
fft_2cos = np.fft.fft(x)

# Compute the frequency vector
plt.figure(5)
freq = np.fft.fft(fft_2cos)
plt.stem(freq, np.abs(fft_2cos))
plt.suptitle("Спектр суммы cos")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')



# Plot the filtered signal
plt.figure(6)
filt = 2 * np.pi *fc2 /fs
filt_arr = filt * t
y = signal.convolve(fft_2cos,x2)
plt.plot(y[:100])
plt.suptitle("Фильтрованный сигнал")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.show()

 
