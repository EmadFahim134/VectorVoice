# import Modules & Libraries:
import wave as wav
import numpy as np
from Modules import Synth
from colorama import init, Fore, Back, Style

# init colorama:
init ()

# Sturcterd Start:
def save_wav(filename, audio_data, sample_rate=44100):
    """
    Converts floating-point audio data into a standard 16-bit
    PCM WAV file that any media player can read.
    """
    # 1. Scale decimals (-1.0 to 1.0) to 16-bit integers (-32767 to 32767)
    audio_data_int16 = (audio_data * 32767).astype(np.int16)

    # 2. Write the binary data into a WAV file template
    with wav.open(filename, "w") as w:
        w.setnchannels(1)  # Mono (1 channel)
        w.setsampwidth(2)  # 16-bit audio = 2 bytes per sample
        w.setframerate(sample_rate)  # 44,100 frames per second
        w.writeframes(audio_data_int16.tobytes())


def main():
    print(Fore.BLUE, '____VECTORVOICE OPENING____')

    # User Input:
    user_input = ""
    print(f"Processing text: '{user_input}'")

    # Runing text through "Synth.py" module.
    final_audio = Synth.synth_text(user_input)

    if final_audio is not None:
        print(
            f"Success! Generated audio track array with {len(final_audio)} total sound samples."
        )
        output_filename = "output.wav"
        print(f"Exporting sound data to '{output_filename}'...")
        save_wav(output_filename, final_audio)

        print(
            "\n Done! Look at your Zed file tree. Open 'output.wav' to hear your creation!"
        )
    else:
        print(Style.BRIGHT + Fore.RED ,"Fail to generate output.wav")


if __name__ == "__main__":
    main()
