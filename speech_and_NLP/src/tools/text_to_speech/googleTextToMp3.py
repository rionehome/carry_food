from gtts import gTTS
from speech_and_NLP.src.tools.text_to_speech.verbose import log

def googleTextToMp3(text: str, path: str, verbose: bool):
    log("googleTextToMp3 Function running...", verbose)
    tts = gTTS(text, lang='ja', tld="com")
    log("Variable : tts" + str(tts)  ,verbose)
    log("Saving Audio File ..." ,verbose)
    tts.save(path)
    log("End Function googleTextToMp3" ,verbose)
