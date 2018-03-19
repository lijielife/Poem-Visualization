import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.artist import Artist
from matplotlib.mlab import dist_point_to_segment
import os
import wave
import struct
import sys

clipdir = '/Users/CorbanSwain/Google Drive'
clipname = 'test2'

clipname += '.wav'
clipfile = os.path.join(clipdir, clipname) 

def wav_to_float(wavefile):
    audio = wave.open(wavefile, 'r')
    tstep = 1 / audio.getframerate()
    amplitude = []
    time = []
    frame_counter = range(audio.getnframes())
    for iFrame in frame_counter:
        wave_data = audio.readframes(1)
        data = struct.unpack('<i', wave_data)
        amplitude.append(data[0])
        if time:
            time.append(time[-1] + tstep)
        else:
            time.append(0)
    max_val = max(amplitude)
    amplitude = [v / max_val for v in amplitude]
    audio.close()
    return (time, amplitude)

t, a = np.array(wav_to_float(clipfile))
plt.plot(t, a)

numel = len(t)
a_rect = np.multiply(a, a)
window_size = round(numel * 0.05)
smooth_fxn = np.ones((window_size,)) / window_size
a_smooth = np.convolve(a_rect, smooth_fxn, mode='same')
a_smooth = a_smooth / max(a_smooth)
plt.plot(t, a_smooth)
plt.show()
