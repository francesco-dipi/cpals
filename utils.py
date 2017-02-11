def str2bytes(s):
    '''
    Take a string s and return a list of two-char strings representing hex bytes.
    '''
    return [s[i:i+2] for i in xrange(0, len(s), 2)]

def hex2chr(s):
    '''
    Take a string s which represent a list of bytes in hexadecimal format
    and return a list of characters built from pairs of bytes.
    '''
    return [chr(int(x, 16)) for x in str2bytes(s)]

def hex2bin64(s):
    '''
    Take a string s which represent a list of bytes in hexadecimal format
    and return the corresponding string encoded in base64.
    '''
    return ''.join(hex2chr(s)).encode('base64')

def strXor(s1, s2):
    '''
    Take two equal-length buffers and produces their XOR combination
    '''
    return hex(int(s1, 16) ^ int(s2, 16)).replace('0x', '').replace('L', '')

def singleByteXor(s, c):
    '''
    Take an hex encoded string s and return its XOR against a single character c.
    '''
    return ''.join([chr(int(byte, 16) ^ ord(c)) for byte in str2bytes(s)])

def scoreEnglish(s):
    '''
    Take a plaintext string s as input and return a score indicating its
    probability to be an english sentence.
    '''
    import re # Now i have two problems...
    return len(re.findall('[ETAOIN SHRDLU]', s, re.IGNORECASE)) / float(len(s))

def computeScoresXorAgainstAllChars(s):
    '''
    Take an hex encoded string s, XORes it against bytes from 00 to FF
    and return an ordered list of tuples containing its english score
    and the decoded string.
    '''
    return [(scoreEnglish(xored), xored) for xored in [singleByteXor(s, c) for c in [chr(x) for x in range(256)]]]

def bestResultFor(scores):
    '''
    Return the result with the highest score
    '''
    return sorted(scores, reverse=True)[0][1]
