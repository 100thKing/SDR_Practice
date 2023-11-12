from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

fig_count = 0
#Построение аналогового сигнала с частотой fc = 50 [Hz]
t = np.arange(0,1,0.001)
fs = 1000
fc = 100
Ts = 1/fs
A = 5
w = 14 * np.pi * fc
x = A * np.cos(w * t)

# Получение набора отчетов размерами 64, 128, 256
n_64 = np.arange(0,64,1)
n_128 = np.arange(0,128,1)
n_256 = np.arange(0,256,1)

x_64 = A * np.cos(w * n_64 * Ts)
x_128 = A * np.cos(w * n_128 * Ts)
x_256 = A * np.cos(w * n_256 * Ts)


#Рассчёт значения аналоговой частоты, которая соответствует нормированной
#частоте Ω = 0.1Pi рад, Ω = 0.3Pi рад
Q = 0.1 * np.pi
x_Q_01 = (Q *fs) / (2*np.pi)

Q = 0.3 * np.pi
x_Q_03 = (Q *fs) / (2*np.pi)


#Построение модуля спектра для дискретных сигналов с 
#n = 64, 128, 256
spectre64 = abs(np.fft.fft(x_64))
spectre128 = abs(np.fft.fft(x_128))
spectre256 = abs(np.fft.fft(x_256))

fspec64 = np.arange(-len(spectre64)/2, len(spectre64)/2, 1) * fs/64
fspec128 = np.arange(-len(spectre128)/2, len(spectre128)/2, 1) * fs/128
fspec256 = np.arange(-len(spectre256)/2, len(spectre256)/2, 1) * fs/256


# Цифровая фильтрация

fs = 256

t = np.arange(0, 1, 1/fs)

fc1 = 185
fc2 = 45

x1 = np.cos(50*np.pi*fc1*t)
x2 = np.cos(9*np.pi*fc2*t)

signal_2cos = x1+x2

#Нормированная частота среза
fc = 5/fs 
N = 50
n = np.arange(0, N)
h = np.sinc(2 * fc * (n - (N - 1) / 2))

spectre_2cos = np.fft.fft(signal_2cos)
freq_2cos = np.fft.fftfreq(len(signal_2cos), 1/fs)

filtred_signal = np.convolve (signal_2cos, h, mode='same')
filtred_spectre = np.fft.fft(filtred_signal)
freq_filt = np.fft.fftfreq(len(filtred_spectre), 1/fs)



# Вывод графиков
    ## Модуль спектра для n = 64, 128, 256
fig_count+=1
plt.figure(fig_count, figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.stem(fspec64, spectre64)
plt.title('Колчиество отсчётов n = 64')
plt.xlabel('Частота [Гц]')
plt.subplot(1, 3, 2)
plt.stem(fspec128, spectre128)
plt.title('Колчиество отсчётов n = 128')
plt.xlabel('Частота [Гц]')
plt.subplot(1, 3, 3)
plt.xlabel('Частота [Гц]')
plt.title('Колчиество отсчётов n = 256')
plt.stem(fspec256, spectre256)
#plt.savefig('Модуль_спектра.jpeg')

    ## Исходный сигнал
fig_count+=1
plt.figure(fig_count, figsize=(12, 6))
plt.xlabel('Время [c]')
plt.title('Исходный сигнал\nx(t) = A * cos(w * t)')
t = np.arange(0,1,0.001)
plt.plot(t, x)
#plt.savefig('Исходный_сигнал.jpeg')

    ## Дискретизированный сигал для n = 64, 128, 256
fig_count+=1
plt.figure(fig_count, figsize=(12, 6))
plt.suptitle('Дискретизированный сигнал\nx(n) = A * cos(w * n * Ts)')
plt.subplot(1, 3, 1)
plt.xlabel('Количество отсчётов')
plt.title('Колчиество отсчётов n = 64')
plt.stem(n_64, x_64)
plt.subplot(1, 3, 2)
plt.xlabel('Количество отсчётов')
plt.title('Колчиество отсчётов n = 128')
plt.stem(n_128, x_128)
plt.subplot(1, 3, 3)
plt.xlabel('Количество отсчётов')
plt.title('Колчиество отсчётов n = 256')
plt.stem(n_256, x_256)
#plt.savefig('Дискретизированный_сигнал.jpeg')


    ## Состовляющие сигнала суммы cos
fig_count+=1
plt.figure(fig_count)
plt.suptitle("Состовляющие сигнала")
plt.subplot(1,2,1)
plt.plot(x1[:100])

plt.subplot(1,2,2)
plt.plot(x2[:100])
#plt.savefig('Состовляющие_сигнала.jpeg')

    ## Графики суммы cos
fig_count+=1
plt.figure(fig_count)
plt.subplot(1, 2, 1)
plt.title('Сумма cos')
plt.stem(freq_2cos, abs(spectre_2cos))
plt.xlim(-25, 25)

plt.subplot(1, 2, 2)
plt.title('Отфильтрованный сигнал')
plt.stem(freq_filt, abs(filtred_spectre))
plt.xlim(-25, 25)
#plt.savefig('Сумма_cos.jpeg')

plt.show()
