import time

import adi
import matplotlib.pyplot as plt
import numpy as np
##%matplolib


# Create radio
sdr = adi.Pluto("ip:192.168.2.1")

# Configure properties
sdr.rx_lo = 2462000000

# Collect data
for r in range(30):
    rx = sdr.rx()
    plt.clf()
    plt.xlabel("Время")
    plt.ylabel("Амплитуда")
    plt.legend({"real","imaginary"}, loc = 'upper left')
    plt.plot(rx.real)
    plt.plot(rx.imag)
    plt.savefig(f'saved_figure_{r}.png')
    plt.draw()
    plt.pause(0.05)
    time.sleep(0.1)


plt.show()