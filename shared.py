# encoding: utf-8

alphabet = u' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{£}~0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzϕϴΩβε'
placeholder = unichr(ord(alphabet[-1]) + 1)


def valid(text):
    for c in text:
        if c not in alphabet:
            return False
    return True


def numberify(text):
    return ''.join(['%02d' % (alphabet.index(c), ) for c in text])


def textify(number):
    number = [number[i:i + 2] for i in range(0, len(number), 2)]
    return ''.join([alphabet[int(n)] for n in number])

if __name__ == '__main__':
    # simple tests
    assert textify(numberify(alphabet)) == alphabet