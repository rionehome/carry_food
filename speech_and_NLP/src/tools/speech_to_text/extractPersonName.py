from speech_and_NLP.src.tools.speech_to_text.mecabAnalyzer import mecabAnalyzer

def extractPersonName(text:str, path = "") -> str :
  mecab = mecabAnalyzer(path)
  node = mecab.parseToNode(text)

  names = []
  while node:
      if node.feature.startswith('名詞,固有名詞,人名'):
          names.append(node.surface)
      node = node.next
      name_string = ''.join(names)

  return name_string
