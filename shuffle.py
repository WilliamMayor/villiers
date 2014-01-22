import time
import random
from shared import test, matches


def encrypt(text, key):
    random.seed(key)
    text = list(text)
    random.shuffle(text)
    l = list(xrange(0, len(text)))
    random.shuffle(l)
    return text


def decrypt(text, key):
    shuffled = encrypt(xrange(0, len(text)), key)
    plaintext = list(xrange(0, len(text)))
    for i in xrange(0, len(shuffled)):
        plaintext[shuffled[i]] = text[i]
    return plaintext


def hack(ciphertext):
    tick = time.time()
    count = 0
    try:
        while True:
            guess = ''.join(decrypt(ciphertext, count))
            count += 1
            m = matches(guess)
            if m > 0:
                print 'Possible:', guess
    except:
        tock = time.time()
        time_taken = int(tock - tick)
        print 'Tried %d guesses in %d seconds, that\'s %d per second' % (count, time_taken, count / time_taken)
        print 'It would take %d years to brute force this key' % (9 ** 157 / ((count / time_taken) * 60 * 60 * 24 * 365),)


if __name__ == '__main__':
    m = raw_input('encrypt/decrypt/hack? ').lower()
    if 'encrypt'.startswith(m):
        text = raw_input('plaintext: ')
        key = int(raw_input('key: '))
        print 'ciphertext:', ''.join(encrypt(text, key))
    elif 'decrypt'.startswith(m):
        text = raw_input('ciphertext: ')
        key = int(raw_input('key: '))
        print 'plaintext:', ''.join(decrypt(text, key))
    elif 'hack'.startswith(m):
        text = raw_input('ciphertext: ')
        hack(text)
    elif 'test'.startswith(m):
        test([0, 1000, 2000, 3000, 4000], encrypt, decrypt, hack)
