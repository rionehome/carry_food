import MeCab

def mecabAnalyzer(model_path:str = "-r /dev/null -d /usr/lib/mecab/dic/ipadic") -> str:
    m = MeCab.Tagger(model_path)
    return m
