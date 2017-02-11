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
    return hex(int(s1, 16) ^ int(s2, 16)).replace('0x','').replace('L', '')
