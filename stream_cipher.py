import random

class KeyStream:
    def __init__(self, key = 1):
        self.next = key

    def rand(self):
        self.next = (1103515245 * self.next + 12345) % 2 ** 31
        return self.next

    def get_key_byte(self):
        return (self.rand() // 2**31) % 256


def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])


def transmit(cipher, likely):
    b = []
    for c in cipher:
        if random.randrange(0, likely) == 0:
            c = c ^ 2 ** random.randrange(0, 8)
        b.append(c)
    return bytes(b)


def modification(cipher):
    mod = [0] * len(cipher)
    mod[10] = ord(' ') ^ ord('1')
    mod[11] = ord(' ') ^ ord('0')
    mod[12] = ord('1') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

def get_key(message, cipher):
    return bytes([message[i] ^ cipher[i] for i in range(len(cipher))])

def crack(key_stream, cipher):
    length = min(len(key_stream), len(cipher))
    return bytes([key_stream[i] ^ cipher[i] for i in range(length)])

def brute_force(plain, cipher):
    for k in range(2 ** 31):
        bf_key = KeyStream(k)
        for i in range(len(plain)):
            xor_value = plain[i] ^ cipher[i]

            if xor_value != bf_key.get_key_byte():
                break

        else: return k

    return false



eves_message = "This is Eve's most valued secrets of all her life".encode()

key = KeyStream(10)
#for i in range(10):
#    print(key.get_key_byte())
message = "Send Bob:   10$".encode()
cipher = encrypt(key, message)
print(cipher)

# This is Eve (alone) all evil
eves_key_stream = get_key(eves_message, cipher)

# This is Bob
cipher = modification(cipher)

#cipher = transmit(cipher, 5)

key = KeyStream(10)
message = encrypt(key, cipher)
print(message)


# Alice again
message = "Hi Bob, let's meet and plan our world domination".encode()
key = KeyStream(10)
cipher = encrypt(key, message)
print(cipher)

# Bob again
key = KeyStream(10)
message = encrypt(key, cipher)
print(message)


# Eve again (more evil than ever)
print(crack(eves_key_stream, cipher))


# This is Eve
bf_key = brute_force(header.encode(), cipher)
key = KeyStream(bf_key)
message = encrypt(key, cipher)
