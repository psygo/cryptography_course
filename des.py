from pyDes import *

def modify(cipher):
    mod = [0] * len(cipher)
    mod[10] = ord(' ') ^ ord('1')
    mod[11] = ord(' ') ^ ord('0')
    mod[12] = ord(' ') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])


message = "0123456701234567"
key = "DESCRYPT"
iv = bytes([0] * 8)
k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)

cipher = k.encrypt(message)
print("Length of cipher plain:", len(message))
print("Length of cipher text:", len(cipher))
print("Encrypted:", cipher)

print("Encrypted:", cipher[0:8])
print("Encrypted:", cipher[8:16])
print("Encrypted:", cipher[16:])
message = k.decrypt(cipher)
print("Decrypted:", message)
