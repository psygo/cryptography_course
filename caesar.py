def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for c in letters:
        key[c] = letters[(cnt + n) % len(letters)]
        cnt += 1
    return key

def get_encryption_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey

def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


# This is done by your enemy
key = generate_key(3)
print(key)
message = "YOU ARE AWESOME"
cipher = encrypt(key, message)
print(cipher)

# dkey = generate_key(26 - 3)
dkey = get_encryption_key(key)
message = encrypt(dkey, cipher)
print(message)

# this is us breaking the cipher
for i in range (26):
    dkey = generate_key(i)
    message = encrypt(dkey, cipher)
    print(message)
