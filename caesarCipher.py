# caesarCipher.py
import pyperclip
from cipher import caesar

function = ''

while function != 'encode' and function != 'decode':

    function = input("Do you want to encrypt or decrypt a message? Answer encode/decode\n")

message = input("What is the message to " + function + "?\n")

key = int(input("What is the " + function + " key?\n"))

if function == 'encode':
    direction = 1
else:
    direction = -1

print(caesar(message, key, direction))
