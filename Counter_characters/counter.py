#!usr/bin/python3

def counter(string):
#Function for count each characters of a string
#   @string: The string to count

    dictionary_char = {}

    for i in string:
        if i in dictionary_char:
            dictionary_char[i] += 1
        else:
            dictionary_char[i] = 1

    print(dictionary_char)
