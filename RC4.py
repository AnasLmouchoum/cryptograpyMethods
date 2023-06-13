
def KeyScheduling(Key):
    S = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + S[i] + Key[i % len(Key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PseudoRandGen(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        KeyStream = S[(S[i] + S[j]) % 256]
        yield KeyStream

def RC4(key, plaintext):
    S = KeyScheduling(key)
    keystream = PseudoRandGen(S)
    ciphertext = []
    for byte in plaintext:
        ciphertext.append(byte ^ next(keystream))
    return bytes(ciphertext)

key = 'kzaj23dzdsqd'
plaintext = 'bonjour'
ciphertext = RC4(key.encode(), plaintext.encode())
print(ciphertext)
decrypted_plaintext = RC4(key.encode(), ciphertext)
print(decrypted_plaintext.decode())