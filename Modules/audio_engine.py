# import libs:          "Audio Engine of VectorVoice"
import numpy as np

# Audio config:
SAMPLE_RATE = 44100

# Calculations:
def db_to_amplitude(db_value):
    amplitude = 10 ** (db_value / 20)
    return amplitude


def gene_wave(frequency, duration, amplitude):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return wave
