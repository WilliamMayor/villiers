# encoding: utf-8

alphabet = unicode((' !@#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
                    '0123456789'
                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    'abcdefghijklmnopqrstuvwxyz'))

placeholder = unichr(160 + 101 - len(alphabet))

while len(alphabet) != 100:
    alphabet += unichr(160 + 100 - len(alphabet))


def valid(text):
    for c in text:
        if c not in alphabet:
            return False
    return True


def numberify(text):
    return ''.join(['%02d' % (alphabet.index(c), ) for c in text])


def textify(number):
    if len(number) % 2 != 0:
        number = '0' + number
    number = [number[i:i + 2] for i in range(0, len(number), 2)]
    return ''.join([alphabet[int(n)] for n in number])


def matches(text):
    words = text.split(' ')
    count = 0
    with open('words.txt', 'r') as fd:
        dictionary = fd.read().splitlines()
    for w in words:
        if w in dictionary:
            count += 1
    return count


def test(keys, encrypt, decrypt, hack):
    text = 'i am under attack'
    for key in keys:
        print 'key:', key
        e = encrypt(text, key)
        d = decrypt(e, key).replace(placeholder, '')
        h = list(hack(e))
        print ' ', text, '->', e, '->', d
        assert text == d
        print '  hack:'
        for p in h:
            print '   ', p
        assert text in h
    e1 = encrypt(text, keys[-2])
    e2 = encrypt(e1, keys[1])
    d1 = decrypt(e2, keys[-2])
    d2 = decrypt(d1, keys[1])
    print 'key exchange:'
    print ' ', text, '->', e1, '->', e2, '->', d1, '->', d2
    assert text == d2.replace(placeholder, '')

if __name__ == '__main__':
    # simple tests
    assert textify(numberify(alphabet)) == alphabet
