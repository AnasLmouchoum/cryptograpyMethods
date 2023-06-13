
import sympy

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += str(ele)
    return str1

def estPremier(n):
    return sympy.isprime(n)

def factor(n):
    p, q = 0, 0 
    i = 1
    while True:
        i += 1
        if estPremier(i):
            s = n / i
            r = n % i  
            if r == 0:
                p, q = int(s), i
                return p, q
        continue

def privateKey(e, p, q):
    z = (p - 1) * (q - 1)
    i = 1
    while True:
        i += 1
        d = (1 + (i * z)) / e
        r = (1 + (i * z)) % e
        if r == 0:
            return int(d)

def encrypt(M, e, n):
    mStr = str(M)
    mTab = []
    encTab = []
    if len(mStr) < 3:
        mTab.append(mStr)
    else:
        for i in range(0, len(mStr), 3):
            mTab.append(mStr[i:i+3])
    for mi in mTab:
        encTab.append((int(mi) ** e) % n)
    return listToString(encTab)

def decrypt(M, d, n):
    return pow(M, d, n)

def fromDecimaleToString(plaintext):
    result = ""
    plaintext=str(plaintext)
    for i in range(0, len(plaintext), 2):
        ascii_char = chr(int(plaintext[i:i+2]))
        result += ascii_char
    return result

def fromStringToDecimale(text):
    M = ""
    for c in text:
        M += str(ord(c))
    return int(M)

n = 1037594094337
e = 7
p, q = factor(n)
d = privateKey(e, p, q)
M = 997593903573

plaintext = decrypt(M, d, n)
result = fromDecimaleToString(plaintext)

print(result)