import dis
import random

def addPoints(P, Q, a, p):
    if P == Q:
        s = ((3 * pow(P[0], 2) + a) * pow((2 * P[1]), -1, p)) % p
    elif Q[0] - P[0] == 0:
            s = 1
    else:
        s = ((Q[1] - P[1]) * pow((Q[0] - P[0]), -1, p))% p
    x3 = pow((pow(s, 2) - P[0] - Q[0]), 1, p)
    y3 = pow((s * (P[0] - x3) - P[1]), 1, p)
    R = (x3, y3)
    return R

def privateKey(P, T, a, p):
    d = 1
    Q = P
    while True:     
        R = addPoints(P, Q, a, p)
        d += 1
        if d > p:
            return None
        if R == T:
            return d
        else:
            Q = R
            
def scalaireP(k, P, a, p):
    kP = addPoints(P, P, a, p)
    for i in range(k-2):
        kP = addPoints(P, kP, a, p)
    return kP
        
def encrypt(M, P, T, a, p):
    k = 3
    Y1 = scalaireP(k, P, a, p)
    Y2 = addPoints(M, scalaireP(k, T, a, p), a, p)
    return (Y1, Y2)

def decrypt(Y1, Y2, d, a, p):
    tmp = scalaireP(d, Y1, a, p)
    mY1 = (tmp[0], -tmp[1])
    D = addPoints(Y2, mY1, a, p)
    return D

a, b, p, T, P = 2, 2, 17, (13,7), (5, 1)

d = privateKey(P, T, a, p)
print("d = ",d)
print("La somme est: ", addPoints((5,1), (5, 1), a, p))
print("Scalaire: ", scalaireP(3, P, a, p))
enc = encrypt((3,1), (5,1), (13, 7), a, p)
Y1, Y2 = enc[0], enc[1]
print(Y1, Y2)
dec = decrypt(Y1, Y2, 8, a, p)
print(decrypt(Y1, Y2, 8, a, p))
