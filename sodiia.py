#!/etc/bin/python
#   ~><< Poorly implemented by Jbies121 >><~
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

def output_sod(etup):
    etup_tostring = etup
    sodiia = ''.join(etup_tostring)
    print("SODIIA:: {}".format(sodiia))

userInput = input("String to encrypt:: ")
input_tup = tuple(userInput)
encrypt_sodiia(input_tup)
output_sod(encrypted_tup)
