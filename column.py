from shared import placeholder

#       T E A C H    W I N
KEY = ([5,3,1,2,4], [3,1,2])


def encrypt(text, key):
    ciphertext = ['' for _ in xrange(len(key))]
    for i in xrange(len(key)):
        for j in xrange(i, len(text), len(key)):
            print j
            ciphertext[key[i]-1] += text[j]
    return ''.join(ciphertext)

'EVLNE ACDTK ESEAQ ROFOJ DEECU WIREE'
encrypt('WEAREDISCOVEREDFLEEATONCE', [6,3,2,4,1,5])
encrypt(encrypt('WEAREDISCOVEREDFLEEATONCE', [6,3,2,4,1,5]), [5,6,4,2,3,1])