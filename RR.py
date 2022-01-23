import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib
from ecgdetectors import Detectors
import traceback

current_dir = pathlib.Path(__file__).resolve()

df = pd.read_csv (r'e104.csv')

unfiltered_ecg = df['v4'].to_numpy()

time = df['time'].to_numpy()

fs = 250
detectors = Detectors(fs)

r_peaks = detectors.engzee_detector(unfiltered_ecg)

print("mulai")

i = 0
for peak in r_peaks:
    if(i<len(r_peaks)-1):
        i=i+1

        plt.plot(unfiltered_ecg[peak:r_peaks[i]])
        plt.axis('off')

        print(time[peak])

        plt.savefig('img/'+time[peak].replace(':', '.')+'.png')
        plt.clf()
        
plt.figure()
plt.plot(unfiltered_ecg)
plt.plot(r_peaks, unfiltered_ecg[r_peaks], 'ro')

input('Selesai')