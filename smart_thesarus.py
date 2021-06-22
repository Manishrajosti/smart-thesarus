import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

def meaning(w):
    w = w.lower()
    x= SequenceMatcher(None, w, get_close_matches(w, data.keys())[0])
    if w in data:
        return data[w]
    elif x.ratio() > 0.6:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist."

word = input("Enter word: ")
output = meaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
