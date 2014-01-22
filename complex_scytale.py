import math
import itertools
import time

from shared import matches, test

placeholder = '$'

KEY = [10, 8, 12, 4, 6, 15, 2, 16, 13, 3, 7, 9, 5, 11, 14, 1]

def encrypt(text, key):
    ciphertext = [placeholder for _ in xrange(len(key))]
    for i in xrange(len(text)):
        ciphertext[key[i] - 1] = text[i]
    return ''.join(ciphertext)


def decrypt(text, key):
    plaintext = [placeholder for _ in xrange(len(key))]
    for i in xrange(len(text)):
        plaintext[i] = text[key[i] - 1]
    return ''.join(plaintext)


def hack(text):
    tick = time.time()
    count = 0
    try:
        key = list(xrange(len(text)))
        for guess in itertools.permutations(key):
            p = decrypt(text, guess).replace(placeholder, '')
            print 'Possible:', p
            count += 1
    except:
        tock = time.time()
        time_taken = int(tock - tick)
        print 'Tried %d guesses in %d seconds, that\'s %d per second' % (count, time_taken, count / time_taken)
        print 'It would take %d years to brute force this key' % (math.factorial(len(key)) / ((count / time_taken) * 60 * 60 * 24 * 365),)

if __name__ == '__main__':
    m = raw_input('encrypt/decrypt/hack? ').lower()
    if 'encrypt'.startswith(m):
        text = raw_input('plaintext: ')
        print 'ciphertext:', encrypt(text, KEY)
    elif 'decrypt'.startswith(m):
        text = raw_input('ciphertext: ')
        p = decrypt(text, KEY)
        print 'plaintext:', p.replace(placeholder, '')
    elif 'hack'.startswith(m):
        text = raw_input('ciphertext: ')
        hack(text)
    elif 'test'.startswith(m):
        test(list(xrange(1, 10)), encrypt, decrypt, hack)
