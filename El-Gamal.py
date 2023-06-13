
import math

def encrypt(M, p, g, beta, k):
    Y1 = pow(g, k, p)
    Y2 = M * pow(beta, k) % p
    return (Y1, Y2)

def privateKey(p, g, beta):
    s = 0
    while s <= p:
        beta_1 = pow(g, s, p)
        if beta_1 == beta:
            return s
        s += 1
        
def decrypt(Y1, Y2, p, s):
    return (Y2 * pow(Y1, p-1-s)) % p

p = 809
g = 256
beta = 498
k = 89
M = 100

encryptedMsg = encrypt(M, p, g, beta, k)
print(encryptedMsg)
s= privateKey(p, g, beta)
print(s)
decryptedMessage = decrypt(encryptedMsg[0], encryptedMsg[1], p, s)
print(decryptedMessage)