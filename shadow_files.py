import hashlib
import base64

iterations = 45454
# Salt adds randomness even when the passwords are the same
salt = base64.b64decode("6VuJKkHVTdDelbNMPBxzw7INW2NkYlR/LoW4OL7kVAI=".encode())

password = "password".encode()

value = hashlib.pbkdf2_hmac("sha512", password, salt, iterations, dklen=128)
print(base64.b64decode(value))
