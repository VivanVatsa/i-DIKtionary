import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))


def dict_translate(w):
    # check = w
    w = w.lower()
    if w in data:
        # if(not check.upper() or not check.lower()):
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y for YES & N for NO:  " %
                   get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "This Entered word in Wrong. Come Back Again"
        else:
            return "This is a non-existent word. You need to die now \nJust fucking type 'Y' or 'N'"
    else:
        return "Word is Invalid. Double check and try again..."


user_input = input("enter the word: ")

# print(dict_translate(user_input))
output = dict_translate(user_input)

if type(output) == list:
    for item in output:
        print(item)

#
# PowerShell 7.0.3
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# https://aka.ms/powershell
# Type 'help' to get help.
#
# enter the word: car
# ['A four-wheeled motor vehicle used for land transport.']
# enter the word: name
# ['Any word or phrase which designates a particular person, place, class or thing.', 'To refer briefly to; to make reference to.', 'To designate for a role.', 'To give a name to.', 'Word or phrase used to designate an object.', 'To identify as in botany or biology, for example.', 'To give the name or identifying characteristics of; to refer to by name or some other identifying characteristic property.']
#
# I: The term 'I' is not recognized as the name of a cmdlet, function, script file, or operable program.
# Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
#
# I: The term 'I' is not recognized as the name of a cmdlet, function, script file, or operable program.
# Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
#
# enter the word: I
# ['The speaker or writer referring to himself or herself alone.', 'The capitalized version of the ninth letter of the Latin alphabet.']
#
# enter the word: asdf
# Traceback (most recent call last):
#   File ".\DIK.py", line 12, in <module>
#     print(dict_translate(user_input))
#   File ".\DIK.py", line 7, in dict_translate
#     return data[w]
# KeyError: 'asdf'
#
#
#
