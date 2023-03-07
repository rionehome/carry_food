from autocorrect import Speller

spell = Speller(lang="en")

def correctSpell(text: str) -> str:
    return spell(text)
