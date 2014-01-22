import math

from shared import matches, test

placeholder = '$'

def encrypt(text, key):
    ncols = int(math.ceil(len(text) / float(key)))
    ciphertext = ''
    for i in xrange(0, ncols):
        for j in xrange(0, ncols * key, ncols):
            try:
                ciphertext += text[i + j]
            except IndexError:
                ciphertext += placeholder
    return ciphertext


def decrypt(text, key):
    plaintext = ''
    for i in xrange(0, key):
        for j in xrange(0, len(text), key):
            try:
                c = text[i + j]
                plaintext += c
            except:
                pass
    return plaintext


def hack(text):
    for key in xrange(1, len(text)):
        p = decrypt(text, key).replace(placeholder, '')
        yield p

if __name__ == '__main__':
    m = raw_input('encrypt/decrypt/hack? ').lower()
    if 'encrypt'.startswith(m):
        text = raw_input('plaintext: ')
        key = int(raw_input('key: '))
        print 'ciphertext:', encrypt(text, key)
    elif 'decrypt'.startswith(m):
        text = raw_input('ciphertext: ')
        key = int(raw_input('key: '))
        p = decrypt(text, key)
        print 'plaintext:', p.replace(placeholder, '')
    elif 'hack'.startswith(m):
        text = raw_input('ciphertext: ')
        for p in hack(text):
            print 'possible:', p
    elif 'test'.startswith(m):
        test(list(xrange(1, 10)), encrypt, decrypt, hack)
