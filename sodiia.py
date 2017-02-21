#!/usr/bin/python3
#   ~><< Poorly implemented by Jbies121 >><~
import string
from random import shuffle
def encrypt_sodiia(utup):
    usermessage = utup
    i = 0
    # Create dictionary to translate user input to cipher text
    # Single substitution will be determined randomly
    sodiia_dictionary = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': '', 'h': '', 'i': '', 'j': '', 'k': '', 'l': '', 'm': '', 'n': '', 'o': '', 'p': '', 'q': '', 'r': '', 's': '', 't': '', 'u': '', 'v': '', 'w': '', 'x': '', 'y': '', 'z': '' }
    sodiia_shift_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    shuffle(sodiia_shift_alpha)
    while i < len(sodiia_shift_alpha):
        for x in sodiia_dictionary:
            sodiia_dictionary[x] = sodiia_shift_alpha[i]
            i+=1
    sodiia_dictionary.update({" ": " ", "'": "'", ",": ",", ".": ".", "?": "?", "!": "!", "@": "@", "#": "#", "$": "$", "%": "%", "^": "^", "&": "&", "*": "*", "(": "(", ")": ")", "~": "~", "`": "`", "-": "-", "_": "_", "+": "+", "=": "=", "{": "{", "}": "}", "[": "[", "]": "]", ";": ";", ":": ":"})
    for b in usermessage:
        #look up key from usermessage incrementally
        #return result to encrypted_tup
        encrypted_list.append(sodiia_dictionary[b])

def output_sod(etup):
    etup_tostring = etup
    sodiia = ''.join(etup_tostring)
    print("SODIIA:: {}".format(sodiia))

def letter_swap(encrypted_list):
    swap_list = []

    original = input("Letter to swap: ")
    if(original == '1'):
        output_sod(swap_list)
    else:
        replacement = input("Swap with: ")
        for i in encrypted_list:
            if(i == original):
                swap_list.append(replacement)
            else:
                swap_list.append(i)

        output_sod(swap_list)
        letter_swap(swap_list)


encrypted_list = []
userInput = input("String to encrypt:: ")
input_tup = tuple(userInput.lower())
encrypt_sodiia(input_tup)
output_sod(encrypted_list)
letter_swap(encrypted_list)
