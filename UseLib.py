import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

print(SequenceMatcher(None, "rainn", "rain"))

print(SequenceMatcher(None, "rainn", "rain").ratio())
print(SequenceMatcher(None, "rain", "rain").ratio())
print(get_close_matches("raiin", ["help", "pyramid", "rain"]))

# print(data.keys())
