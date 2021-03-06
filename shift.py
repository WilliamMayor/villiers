import time
import random
import math
from shared import alphabet, test, matches


def encrypt(text, key):
    random.seed(key)
    table = list(alphabet)
    random.shuffle(table)
    ciphertext = ''
    for c in text:
        i = alphabet.index(c)
        ciphertext += table[i]
    return ciphertext


def decrypt(text, key):
    random.seed(key)
    table = list(alphabet)
    random.shuffle(table)
    plaintext = ''
    for c in text:
        i = table.index(c)
        plaintext += alphabet[i]
    return plaintext


def hack(ciphertext):
    tick = time.time()
    count = 0
    try:
        while True:
            guess = decrypt(ciphertext, count)
            count += 1
            print 'Possible:', guess
    except:
        tock = time.time()
        time_taken = int(tock - tick)
        print 'Tried %d guesses in %d seconds, that\'s %d per second' % (count, time_taken, count / time_taken)
        years = math.factorial(len(alphabet)) / ((count / time_taken) * 60 * 60 * 24 * 365)
        print 'It would take %d years to brute force this key' % (years,)


if __name__ == '__main__':
    m = raw_input('encrypt/decrypt/hack? ').lower()
    if 'encrypt'.startswith(m):
        text = raw_input('plaintext: ')
        key = int(raw_input('key: '))
        print 'ciphertext:', encrypt(text, key)
    elif 'decrypt'.startswith(m):
        text = raw_input('ciphertext: ')
        key = int(raw_input('key: '))
        print 'plaintext:', decrypt(text, key)
    elif 'hack'.startswith(m):
        text = raw_input('ciphertext: ')
        hack(text)
    elif 'test'.startswith(m):
        test([0, 1000, 2000, 3000, 4000], encrypt, decrypt, hack)
