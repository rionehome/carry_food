from pydub import AudioSegment
from speech_and_NLP.src.tools.text_to_speech.verbose import log

def getAudioLength(path: str, verbose: bool):
    log("getAudioLength Function running...", verbose)
    log("Variable : path " + str(path), verbose)
    sound = AudioSegment.from_file(path)
    log("Variable : sound " + str(sound), verbose)
    time = sound.duration_seconds
    log("Variable : time " + str(time), verbose)

    return time