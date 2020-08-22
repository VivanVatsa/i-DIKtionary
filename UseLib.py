import difflib
from difflib import SequenceMatcher
print(SequenceMatcher(None, "rainn", "rain"))

print(SequenceMatcher(None, "rainn", "rain").ratio())
print(SequenceMatcher(None, "rain", "rain").ratio())
