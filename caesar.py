from shared import alphabet, matches, test


def encrypt(text, key):
    ciphertext = ''
    for c in text:
        i = alphabet.index(c)
        ciphertext += alphabet[(i + key) % len(alphabet)]
    return ciphertext


def decrypt(text, key):
    plaintext = ''
    for c in text:
        i = alphabet.index(c)
        plaintext += alphabet[i - key]
    return plaintext


def hack(text):
    for key in xrange(0, len(alphabet)):
        p = decrypt(text, key)
        m = matches(p)
        if m > 0:
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
        print 'plaintext:', decrypt(text, key)
    elif 'hack'.startswith(m):
        text = raw_input('ciphertext: ')
        for p in hack(text):
            print 'possible:', p
    elif 'test'.startswith(m):
        test(list(xrange(0, 5)), encrypt, decrypt, hack)
