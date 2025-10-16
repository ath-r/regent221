import numpy as np
import pandas as pd
import soundfile as sf

CSV = 'preamp/output'
IN = 'input.wav'
OUT = 'output.wav'

data_in, samplerate = sf.read(IN)
SIZE = data_in.size
TIME = SIZE / samplerate

csv = pd.read_csv(CSV, header = 0, names = ['t', 'v'], sep = '\\s+')

x_csv = csv['t'].to_numpy()
y_csv = csv['v'].to_numpy()

from scipy.interpolate import interp1d 
f = interp1d(x_csv, y_csv, kind = 'cubic')

x_out = np.linspace(0, TIME, SIZE)
y_out = f(x_out)

vrms_in = np.sqrt(np.sum(data_in ** 2) / SIZE)
vrms_out = np.sqrt(np.sum(y_out ** 2) / SIZE)

y_out *= vrms_in / vrms_out

sf.write(OUT, y_out, samplerate, 'FLOAT')