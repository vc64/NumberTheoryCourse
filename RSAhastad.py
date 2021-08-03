from RSAencrypt import Encrypt
from RSAdecrypt import ConvertToStr
from ChRem import ChineseRemainderTheorem
# from diophantine import diophantine


def DecipherHastad(ciphertext1, modulo1, ciphertext2, modulo2):
    # problem states that message1 == message2 and exponent1 == exponent2 = 2

    # x, y = diophantine(modulo1, modulo2, 1)

    # m = ciphertext2 * modulo1 * x + ciphertext1 * modulo2 * y

    m = ChineseRemainderTheorem(modulo1, ciphertext1, modulo2, ciphertext2)

    return ConvertToStr(int(m ** 0.5))


# p1 = 790383132652258876190399065097
# q1 = 662503581792812531719955475509
# p2 = 656917682542437675078478868539
# q2 = 1263581691331332127259083713503
# n1 = p1 * q1
# n2 = p2 * q2
# ciphertext1 = Encrypt("attack", n1, 2)
# ciphertext2 = Encrypt("attack", n2, 2)
# message = DecipherHastad(ciphertext1, n1, ciphertext2, n2)
# print(message)


