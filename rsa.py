import sys
import fractions

from shared import numberify, textify


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]


def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return b, x, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


def generate(p, q, verbose=False):
    n = p * q
    t = (p - 1) * (q - 1)
    for e in xrange(2, t):
        if fractions.gcd(e, t) == 1:
            d = modinv(e, t)
            if d is not None:
                return n, e, d


def raw_encrypt(number, n, e, verbose=False):
    bs = max(len(str(n)) - 1, 1)
    parts = [int(number[i:i + bs]) for i in xrange(0, len(number), bs)]
    if verbose:
        print parts
    parts = [pow(p, e, n) for p in parts]
    if verbose:
        print parts
    c = ''.join([str(p).zfill(len(str(n))) for p in parts])
    if verbose:
        print c
    return c


def encrypt(text, n, e, verbose=False):
    if verbose:
        print text
    number = numberify(text)
    if verbose:
        print number
    return raw_encrypt(number, n, e, verbose)


def raw_decrypt(number, n, d, verbose):
    bs = len(str(n))
    parts = [number[i:i + bs] for i in xrange(0, len(number), bs)]
    if verbose:
        print parts
    parts = [pow(int(p), d, n) for p in parts]
    if verbose:
        print parts
    p = ''.join([str(p).zfill(max(len(str(n)) - 1, 1)) for p in parts[:-1]])
    p += str(parts[-1])
    if verbose:
        print p
    return p


def decrypt(number, n, d, verbose=False):
    if verbose:
        print number
    number = raw_decrypt(number, n, d, verbose)
    return textify(number)


def hack(ciphertext):
    return []


if __name__ == '__main__':
    m = raw_input('generate/encrypt/decrypt? ').lower()
    v = '-v' in sys.argv or '--verbose' in sys.argv
    if 'generate'.startswith(m):
        p = int(raw_input('p: '))
        q = int(raw_input('q: '))
        n, e, d = generate(p, q, v)
        print 'public key: n =', n, 'e =', e
        print 'private key: n =', n, 'd =', d
    elif 'encrypt'.startswith(m):
        text = raw_input('plaintext: ')
        n = int(raw_input('n: '))
        e = int(raw_input('e: '))
        c = encrypt(text, n, e, v)
        print 'ciphertext:', c
    elif 'decrypt'.startswith(m):
        text = raw_input('ciphertext: ')
        n = int(raw_input('n: '))
        d = int(raw_input('d: '))
        print 'plaintext:', decrypt(text, n, d, v)
    elif 'rencrypt'.startswith(m):
        raw = raw_input('raw: ')
        n = int(raw_input('n: '))
        e = int(raw_input('e: '))
        c = raw_encrypt(raw, n, e, v)
        print 'ciphertext:', c
    elif 'rdecrypt'.startswith(m):
        raw = raw_input('raw: ')
        n = int(raw_input('n: '))
        e = int(raw_input('d: '))
        p = raw_decrypt(raw, n, e, v)
        print 'plaintext:', p
    elif 'test'.startswith(m):
        text = 'i am under attack'
        prms = primes(1000)
        for i in xrange(5, len(prms), 2):
            n, e, d = generate(prms[i], prms[i - 1], v)
            print 'public key: n =', n, 'e =', e
            print 'private key: n =', n, 'd =', d
            c = encrypt(text, n, e, v)
            p = decrypt(c, n, d, v)
            print ' ', text, '->', c, '->', p
            assert text == p
