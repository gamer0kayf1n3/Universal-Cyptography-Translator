#initizlizing
import os
import base64
from datetime import datetime

morse_dictionary = {
    'T':'-',
    'E':'.',
    'M':'--',
    'N':'-.',
    'I':'..',
    'A':'.-',
    'O':'---',
    'G':'--.',
    'K':'-.-',
    'D':'-..',
    'W':'.--',
    'R':'.-.',
    'U':'..-',
    'S':'...',
    'Q':'--.-',
    'Z':'--..',
    'Y':'-.--',
    'C':'-.-.',
    'X':'-..-',
    'B':'-...',
    'J':'.---',
    'P':'.--.',
    'L':'.-..',
    'F':'..-.',
    'V':'...-',
    'H':'....',
    '0':'-----',
    '9':'----.',
    '8':'---..',
    '7':'--...',
    '6':'-....',
    '5':'.....',
    '4':'....-',
    '3':'...--',
    '2':'..---',
    '1':'.----',
    '.':'.-.-.-',
    '?':'..--..',
    ',':'--..--',
    '(':'-.--.',
    ')':'-.--.-',
    '!':'-.-.--',
    '-':'-....-',
    ' ':'/',
    }
#find path
"""
os.chdir(os.path.dirname(os.path.realpath(__file__)))
for x in os.listdir():
    if 'log' in x:
        pass
    else:
        os.mkdir('/log')
"""
#logging
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#encoders
def encode_base64(msg):
    #msg must be your input
    message = msg
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)
    encode()

def encode_rot13(s):
    #s must be your input
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)
    print("".join([d.get(c, c) for c in s]))
    encode()

def encode_caesar_cipher(word, shiftc):
    new = ''
    shiftc = shift
    for x in word:
        up = x.upper()
        if up == ' ':
            sp = ord(up) - shift
            spch = chr(sp)
            shifted = ord(spch) + shift

            chrshifted = chr(shifted)
            new = new + str(chrshifted)
        else:
            shifted = ord(up) + shift
            chrshifted = chr(shifted)
            new = new + str(chrshifted)
    print(new)
    encode()

def encode_affine(word, val1, val2):
    new = ''
    for x in word:
        ordn = ord(x)
        alph = ordn - 65
        conv = val1 * alph + val2
        mod = conv % 26
        modref = mod + 65
        outref = chr(modref)
        new  = new + outref
    print(new)
    encode()

#start of vigenere cipher
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + 
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
      
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - 
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - 
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))
    
#end of vigenere cipher     

def vigenere_cipher(string, keyword):
    key = generateKey(string, keyword)
    cipher_text = cipherText(string,key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :", 
           originalText(cipher_text, key))
    encode()


def binary_encoder(bin):
    output = ''
    for x in bin:
        asci = ord(x)
        binval = bin(asci)
        binval = binval.replace('0b','')
        chars = len(binval)
        while chars != 8:
            binval = '0' + binval  #adds 0 to output
            chars = len(binval)
        output = output + str(binval)
    print(output)
def split(word):
            out = [char for char in word]
            return out
def morse_encoder(inp):
    try:
        output = ''
        word = inp
        for x in split(word.upper()):
            get = morse_dictionary[x]
            output = output + ' ' + get + ' '
        print(output)
    except:
        print('Error')
   
#decoders
#still blank :(


#e/d
def encode():
    print('Entered encode mode.')
    print('Press "x" to go back, or:')
    print("""
    0 - base64
    1 - rot13
    2 - caesar cipher
    3 - affine cipher
    4 - vigenere cipher
    5 - binary
    6 - morse
    """)
    print('This time, confirm your answer by pressing Enter.')
    user = input()
    if user == '0':
        encode_base64(input('Base64 Message: '))
    elif user == '1':
        encode_rot13(input('Rot13 Message: '))
    elif user == '2':
        encode_caesar_cipher(input('Caesar Cipher Message: '), input('Shifts: '))
    elif user == '3':
        affine_cipher(input('Affine Cipher Message: '), input('Key 1: '), input('Key 2:'))
    elif user == '4':
        vigenere_cipher(input('Vigenere Cipher Message: '), input('Key: '))
    elif user == '5':
        binary_encoder(input('Binary Message: '))
    elif user == '6':
        morse_encoder(input('Morse: '))
    elif user == 'x':
        restart()
    
    else:
        print('not from 1 - 5')
        restart()

def decode():
    print('Decode mode is unavailable yet. Sorry! We are restarting for you.')
    restart()
#the script
print('Universal Cryptography Translator')
def restart():
    print('Encode or Decode? [y/n]')
    print('Press a key.')
    import keyboard  # using module keyboard
    while True:
        try:  
            if keyboard.is_pressed('y'):
                encode()
                break
            elif keyboard.is_pressed('n'):
                decode()
                break
        except:
            break
restart()


