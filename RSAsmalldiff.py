from RSAdecrypt import Decrypt
from RSAencrypt import Encrypt
import math

def IntSqrt(n):
    return math.floor(math.sqrt(n))

def DecipherSmallDiff(ciphertext, modulo, exponent):
    for n in range(2, 5000, 2):
        curr = modulo + ((n/2) ** 2)
        if IntSqrt(curr) ** 2 - curr == 0:
            p = (IntSqrt(curr) + n // 2)
            return Decrypt(ciphertext, p, modulo // p, exponent)

# testing
# p = 1000000007
# q = 1000000009
# n = p * q
# e = 239
# ciphertext = Encrypt("attack", n, e)
# message = DecipherSmallDiff(ciphertext, n, e)
# print(ciphertext)
# print(message)


    




