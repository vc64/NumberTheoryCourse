from FastModExp import PowMod
from RSAencrypt import ConvertToInt, Encrypt

def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
    for x in potential_messages:
        if ciphertext == Encrypt(x, modulo, exponent):
            return x


# testing
modulo = 29329
exponent = 211
ciphertext = Encrypt("d", modulo, exponent)
print(ciphertext)
print(DecipherSimple(ciphertext, modulo, exponent, ["a", "d", "w"]))
