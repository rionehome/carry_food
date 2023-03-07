import re
from typing import Dict

import json

DICTIONARY_PATH = "src/config/dictionary.json"

dictionary = json.load(open(DICTIONARY_PATH))

def replaces(text: str, trdict: Dict[str, str]) -> str:
    return re.sub(
        "|".join(trdict.keys()), lambda m: next(
            (re.sub(pattern, trdict[pattern], m.group(0)) for pattern in trdict
            if re.fullmatch(pattern, m.group(0)))), text)