#!/usr/bin/env python3
#coding: utf-8

import math
import soundfile as sf
import numpy as np

WAV = 'input.wav'
OUT = 'preamp/inputvalues'

data, samplerate = sf.read('input.wav')
	
vrms = math.sqrt(np.sum(data ** 2) / data.size)
print('RMS voltage: %s' % vrms)

with open(OUT, 'w') as f:
		for i in range(data.size):
			time = i / samplerate
			value = data[i]

			f.write("{:.6e} {:.10f}\n".format(time, value))
