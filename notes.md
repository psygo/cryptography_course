# Notes

- The biggest lesson in Crypto is apparently that we should absolutely not keep the algorithm secret.
    - In crypto, making the algorithm public and not being cracked is the highest badge of security there is.

## Caesar Cipher

The simplest version of the caesar cipher is through shifting the alphabet. The *key* is the amount by which you've shifted the alphabet.

If Eve knows the algorithm, she can break it:

Crypto Rule #1, **Kerckhoff's Principle**:

> Eve should not be able to break the ciphers even when she knows the cipher. (cipher = algorithm)

Even with all that, Caesar Cipher's key space is too small.

The *substitution cipher* is a predecessor of the caesar cipher, but it has a way bigger key space, since its keys are permutations of the alphabet, not only shifts, that is 26! != 26.
