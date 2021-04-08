#initizlizing
import os
import base64
from datetime import datetime

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

#encoder yn
print('Selected Encoder')
    
#encoders
def encode_base64(msg):
    #msg must be your input
    message = msg
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

def encode_rot13():
    #s must be your input
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)
    print("".join([d.get(c, c) for c in s]))

def encode_caesar_cipher():
    word = 'BIEBER SUCKS'
    shift = 3
    new = ''
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

def encode_affine():
    word = 'noob'
    val1 = 5
    val2 = 8
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

def vigenere_cipher():
    string = "GEEKSFORGEEKS"
    keyword = "AYUSH"
    key = generateKey(string, keyword)
    cipher_text = cipherText(string,key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :", 
           originalText(cipher_text, key))


def binary_encoder():
    string = 
    string = string.upper()
    reverse_mode = 0
    output = ''
    for x in string:
        asci = ord(x)
        binval = bin(asci)
        binval = binval.replace('0b','')
        chars = len(binval)
        while chars != 8:
            binval = '0' + binval  #adds 0 to output
            chars = len(binval)
            print(chars)  #the length of character
        output = output + str(binval)
    print(output)
    if reverse_mode == 1:
        output = 0 if output else 1
    else:
        pass
    if len(output) % 8 == 0:
        print('sucess')
    else:
        pass
    x = 8
    conv = [output[i: i + x] for i in range(0, len(output), x)]
    for y in conv:
        print(y)

def base32_encode():
    string = 'BIEBER SUCKS'
    output = ''
    for x in string:
        asci = ord(x)
        binval = bin(asci)
        binval = binval.replace('0b','')
        chars = len(binval)
        while chars != 8:
            binval = '0' + binval  #adds 0 to output
            chars = len(binval)
            print(chars)  #the length of character
        output = output + str(binval)
    print(output)
    if len(output) % 8 == 0:
        print('sucess')
    else:
        pass
    x = 5
    outputforrealz = ''
    outputforrealzrealz = ''
    conv = [output[i: i + x] for i in range(0, len(output), x)]
    for y in conv:
        print(y)
        charcount = len(y)
        print(charcount)
        y = '000' + y
        charcount = len(y)
        print(y)
        print(charcount)
        outputforrealz = outputforrealz + y
        x = 8
        conv = [output[i: i + x] for i in range(0, len(output), x)]
        for y in conv:
            add = '0b' + y
            isint = int(add, 2)
            char = chr(isint)
            outputforrealzrealz = outputforrealzrealz + char
            
    print(outputforrealzrealz)
    
        

        

#decoders
#still blank :(
"""
#the script
print('Universal Cryptography Translator')
print('Encode or Decode?')
ed = input('Y/N')
#if ed == 'y' or 'Y':
"""
