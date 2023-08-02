from fft_plot import fft_plot
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
from pydub import AudioSegment

a = "ruido2.wav"
freq, fft_ = fft_plot(a)
