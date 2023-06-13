import hashlib

charsMin = "qwertyuiopasdfghjklzxcvbnm"
charsMinAndMaj = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
charsAndLetters = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

def hashing(password):
    return hashlib.md5(password.encode()).hexdigest()

def findPassword4min(myPassword):
    for i in charsMin:
        for j in charsMin:
            for k in charsMin:
                for l in charsMin:
                    password = i + j + k + l
                    hash = hashing(password)
                    if myPassword == hash:
                        return password

def findPassword4minAndMaj(myPassword):
    for i in charsMinAndMaj:
        for j in charsMinAndMaj:
            for k in charsMinAndMaj:
                for l in charsMinAndMaj:
                    password = i + j + k + l
                    hash = hashing(password)
                    if myPassword == hash:
                        return password
                    
def findPasswordCharsAndLetters(myPassword):
    for i in charsAndLetters:
        for j in charsAndLetters:
            for k in charsAndLetters:
                for l in charsAndLetters:
                    password = i + j + k + l
                    hash = hashing(password)
                    if myPassword == hash:
                        return password

def findPassword8Chars(myPassword):
    for i in charsAndLetters:
        for j in charsAndLetters:
            for k in charsAndLetters:
                for l in charsAndLetters:
                    for i1 in charsAndLetters:
                        for j1 in charsAndLetters:
                            for k1 in charsAndLetters:
                                for l1 in charsAndLetters:
                                    password = i + j + k + l + i1 + j1 + k1 + l1
                                    hash = hashing(password)
                                    if myPassword == hash:
                                        return password

myPassword4min = "3f57984851b2ebd91e190e953a9aec12"        
password4min = findPassword4min(myPassword4min)   
print(password4min)

myPassword4minAndMaj = "b83d73f7c53bccf55a81db5d63e9ca5a"
password4minAndMaj = findPassword4minAndMaj(myPassword4minAndMaj)
print(password4minAndMaj)

myPasswordCharsAndLetters = "7c65199c1d468a213d060b83bfac1907"
passwordCharsAndLetters = findPasswordCharsAndLetters(myPasswordCharsAndLetters)
print(passwordCharsAndLetters)

myPassword8Chars = "9141c4aec06a1d337550a72c4d4931d0"
password8Chars = findPassword8Chars(myPassword8Chars)
print(password8Chars)