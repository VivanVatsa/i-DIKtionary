import json

data = json.load(open("data.json"))


def dict_translate(w):
    return data[w]


user_input = input("enter the word: ")

print(dict_translate(user_input))

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
