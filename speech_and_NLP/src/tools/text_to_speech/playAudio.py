from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import time
from speech_and_NLP.src.tools.text_to_speech.verbose import log

def playAudio(path: str, playTime: int, verbose: bool):
  log("platAudio Function running...", verbose)
  log("pygame.mizer.init()", verbose)
  pygame.mixer.init()
  log("pygame.mizer.load from path : " + str(path), verbose)
  pygame.mixer.music.load(path)
  log("playing audio file...", verbose)
  pygame.mixer.music.play()
  log("waiting end of audio file...", verbose)
  time.sleep(playTime)
  log("stopping audio file...",verbose)
  pygame.mixer.music.stop()
  log("End Function playAudio", verbose)
