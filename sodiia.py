#!/etc/bin/python
#   ~><< Poorly implemented by Jbies121 >><~
def encrypt_sodiia(utup, ukey):
    usermessage = utup
    users_key = ukey
    # Create dictionary to translate user input to cipher text
    # Shift will be determined by key
def output_sod(etup):
    etup_tostring = etup
    sodiia = ''.join(etup_tostring)
    print("SODIIA:: {}".format(sodiia))

userInput = input("String to encrypt:: ")
userKey = input("Key to encrypt:: ")
input_tup = tuple(userInput)
encrypt_sodiia(input_tup)
output_sod(encrypted_tup)
