# importing Modules & Libs:
import numpy as np
import pandas as pd

from audio_engine import gene_wave

# Reading Data:
df = pd.read_csv("data.csv", index_col="Character")


# Main code
def synth_text(text):
    audio_chunks = []
    for char in text.lower():
        if char in df.index:
            row = df.loc[char]
            freq = row["Frequency"]
            duration = row["Duration"]
            db = row["Decibels"]
            wave_chunk = gene_wave(freq, duration, db)
            audio_chunks.append(wave_chunk)
        else:
            print(f"Warning Charater '{char}' not found in 'data.csv' ")
    if audio_chunks:
        return np.concatenate(audio_chunks)
    return None
