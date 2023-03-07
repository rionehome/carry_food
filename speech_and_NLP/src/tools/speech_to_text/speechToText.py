import vosk
import json
from speech_and_NLP.src.tools.speech_to_text.extractPersonName import extractPersonName
import pyaudio

"""
print_partial 中間テキスト表示非表示設定
use_break 最終テキスト取得後、関数からbreakするかどうか。数字にするとn文字以上でbreak
return_extract_person_name 名前のみ抽出を行うか "array" とすると1つ目に名前、2つ目に最終テキストをreturnする
remove_space 空白を取り除くかどうか
path : mecabのpath

"""


def recognize_speech(print_partial: bool = True, use_break: bool or int = True, return_extract_person_name: bool or str = False, remove_space: bool = True, voskLogLevel: int = -1, path = "") -> str:
    print("VOSK LOADING .....")
    vosk.SetLogLevel(voskLogLevel)
    model = vosk.Model(lang="ja")

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1,
                    rate=16000, input=True, frames_per_buffer=8000)

    recognizer = vosk.KaldiRecognizer(model, 16000)

    text = ""

    while True:
        data = stream.read(8000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_dict = json.loads(result)["text"]
            if (remove_space):
                result_dict = result_dict.replace(" ", "")
            text += result_dict
            print(result_dict)
            if isinstance(use_break, bool) and use_break:
                break
            elif isinstance(use_break, (int, float)):
                if len(result_dict) > use_break:
                    break
        else:
            result = recognizer.PartialResult()
            result_dict = json.loads(result)["partial"]
            if (remove_space):
                result_dict = result_dict.replace(" ", "")
            if (print_partial):
                print(result_dict)

    if (return_extract_person_name == "array"):
        return [extractPersonName(text, path), text]
    elif (return_extract_person_name):
        return extractPersonName(text, path)
    return text

# recognized_text = recognize_speech()
