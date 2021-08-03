from RSAencrypt import Encrypt
from RSAdecrypt import *
from modDiv import *

def DecipherSmallPrime(ciphertext, modulo, exponent):
    p = 1

    for n in range(2, 1000000):
        if modulo % n == 0:
            p = n
            break
    
    q = modulo // p

    return Decrypt(ciphertext, p, q, exponent)

# testing
# mod = 101 * 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387
# exp = 239

# cipher = Encrypt("attack", mod, exp)

# print(DecipherSmallPrime(cipher, mod, exp))