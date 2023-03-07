from speech_and_NLP.src.tools.speech_to_text.mecabAnalyzer import mecabAnalyzer


def katakana_to_hiragana(word):
    return word.translate(str.maketrans("カタカナ", "ひらがな"))


"""


text : 検索される文字列
word_list : 配列で検索する文字列を渡す。時間がないので、ひらがな、カタカナ、漢字を用意しておくと良いと思う。
["袋", "取る","持って","運んで"] NG
["ふくろ", "フクロ", "袋", "はこぶ","とる","もつ", "とって" .....] OK
多ければ多いほどゆるくなるのでTrueを返しやすい。
path : mecabのpath


"""

def is_meaning(text, word_list, path = ""):
    """日本語のテキストが、指定された単語リストの中に含まれる単語を持つかどうかを判定する関数"""
    mecab = mecabAnalyzer(path)
    words = mecab.parse(text).split()
    for word in words:
        analyzed_words = word.split(",")
        for analyzed_word in analyzed_words:
            hiragana_analyzed_word = katakana_to_hiragana(analyzed_word)
            for search in filter(None, word_list):
                if hiragana_analyzed_word == search:
                    return True
    return False


# text = "袋をとってきてください"
# verbs = ["ふくろ", "はこぶ","とる","もつ", "とって"]
# result = is_meaning(text, verbs)
# print(result) # True
