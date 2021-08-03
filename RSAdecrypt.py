from extGCD import extended_gcd
from diophantine import diophantine
from FastModExp import PowMod
from modDiv import divide

def ConvertToStr(m):
    hexa = hex(m)[2:]

    word = []

    for i in range(0, len(hexa), 2):
        word.append(hexa[i:i+2])
    
    letters = [chr(int(x, 16)) for x in word]
    
    return "".join(letters)


def InvertModulo(a, n):
    return divide(a, 1, n)


def Decrypt(ciphertext, p, q, exponent):
    inverse_e = InvertModulo(exponent, (p-1)*(q-1))

    return ConvertToStr(PowMod(ciphertext, inverse_e, p*q))

# testing
# 
# inp = ""
# while inp != "eee":
#     inp = [int(x) for x in input("Enter (ciphertext, p, q, exponent): ").split()]
#     print(Decrypt(inp[0], inp[1], inp[2], inp[3]))

# inp = ""
# while inp != "eee":
#     inp = [int(x) for x in input("Enter (int): ").split()]
#     print(ConvertToStr(inp[0]))