import pyopenjtalk
import numpy as np
from scipy.io import wavfile
from speech_and_NLP.src.tools.text_to_speech.verbose import log

def textToWav(text: str, path: str, verbose: bool):
    log("textToWav Function running...", verbose)
    log("generating audio from pyopenjtolk...", verbose)
    x, sr = pyopenjtalk.tts(text)
    log("saving audio file...", verbose)
    wavfile.write(path, sr, x.astype(np.int16))
    log("End Function textToWav", verbose)

