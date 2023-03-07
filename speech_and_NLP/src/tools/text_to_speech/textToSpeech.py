from speech_and_NLP.src.tools.text_to_speech.textToWav import textToWav
from speech_and_NLP.src.tools.text_to_speech.getAudioLength import getAudioLength
from speech_and_NLP.src.tools.text_to_speech.playAudio import playAudio
from speech_and_NLP.src.tools.text_to_speech.googleTextToMp3 import googleTextToMp3
from speech_and_NLP.src.tools.text_to_speech.verbose import log 
import os

"""

If use_gTTS is set to True, internet environment is required.

"""

PATH = "audio.wav"

def textToSpeech(text: str, path: str = PATH, remove: bool = True, use_gTTS: bool = False, verbose: bool = False):
    log("speech_and_NLP is running...",verbose)
    log("textToSpeech Function running...",verbose)
    log("argument : text , " + str(text) + " path , " + str(path) + " remove , " + str(remove) + " use_gTTS , " + str(use_gTTS) + " verbose , " + str(verbose),verbose)
    if (use_gTTS):
      log("use_gTTS is True", verbose)
      convertPath = path.split(".")[0]
      log("Variable : convertPath " + str(convertPath), verbose)
      path = convertPath + ".mp3"
      log("Variable : path " + str(path), verbose)
      log("Run googleTextToMp3...", verbose)
      try:
        googleTextToMp3(text, path, verbose=verbose)
        log("End googleTextToMp3...", verbose)
      except:   
        log("Run textToWav... (EXCEPT)", verbose)
        textToWav(text=text, path=path, verbose=verbose)
        log("End textToWav...", verbose)
        

    else:
      log("Run textToWav...", verbose)
      textToWav(text=text, path=path, verbose=verbose)
      log("End textToWav...", verbose)

    
    log("Run getAudioLength..", verbose)
    audio_length = getAudioLength(path=path, verbose=verbose)
    log("End getAudioLength..", verbose)
    log("Variable : audio_length " + str(audio_length), verbose)

    log("Run playAudio...", verbose)
    playAudio(path=path, playTime=audio_length, verbose=verbose)
    log("End playAudio...", verbose)

    if (remove):
      log("remove file...", verbose)
      os.remove(path)

    log("END OF textToSpeech Function.", verbose)

