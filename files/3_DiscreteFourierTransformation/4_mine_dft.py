import numpy as np
import matplotlib.pyplot as plt
from mylib import my_stem_plot

SAMPLE_NR = 10
SIN_FREQ = 1 

t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)

samples =  np.cos(t*SIN_FREQ)
my_stem_plot(samples,f'samples, f_sig={SIN_FREQ}')

real = list()
imag=list()
for f in range(SAMPLE_NR):
    real.append(np.dot(np.cos(f*t),samples))
    imag.append(np.dot(-np.sin(f*t),samples))

my_stem_plot(real,'my DFT real',y_range=(-6,7))
my_stem_plot(imag,'my DFT imag',y_range=(-6,7))


def myDFT(samples):
    t = np.linspace(0, 2*np.pi, len(samples), endpoint=False)
    real = list()
    imag=list()
    for f in range(len(samples)):
        real.append(np.dot(np.cos(f*t),samples))
        imag.append(np.dot(-np.sin(f*t),samples))
