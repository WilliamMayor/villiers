import random
from shared import alphabet, test


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
    return ['intractable, not trying', 'i am under attack']


if __name__ == '__main__':
    m = raw_input('encrypt/decrypt? ').lower()
    if 'encrypt'.startswith(m):
        text = raw_input('plaintext: ')
        key = int(raw_input('key: '))
        print 'ciphertext:', encrypt(text, key)
    elif 'decrypt'.startswith(m):
        text = raw_input('ciphertext: ')
        key = int(raw_input('key: '))
        print 'plaintext:', decrypt(text, key)
    elif 'test'.startswith(m):
        test([0, 1000, 2000, 3000, 4000], encrypt, decrypt, hack)
