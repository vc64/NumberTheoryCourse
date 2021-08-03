def FastModularExponentiation(b, k, m):
    # only if exponent k is a power of 2
    # b ^ k mod m
    i = 1
    prev = b

    while i <= k:
        prev = (prev % m) ** 2
        i += 1

    return prev % m


def PowMod(a, n, modulo):
    # a ^ n mod modulo

    # Fermat's little theorem (a^n congruent to a^(n mod p-1) mod p)
    n = n % (modulo - 1)

    # fast modular exponentiation
    # uses binary representation of exponent to split 
    # exponent into powers of two and then squaring the 
    # remainder, reducing the size of the numbers in use
    binary = bin(n)

    i = 1
    a = a % modulo
    prev = a
    total = 1

    while i <= len(binary) - 2:
        if (binary[-i] == "1"):
            total *= prev
            total = total % modulo
        
        prev = (prev ** 2) % modulo
        i += 1
    
    return total


# testing
# 
# inp = ""
# while inp != "eee":
#     inp = input("Enter (b k m): ").split()
#     print(FastModularExponentiation1(int(inp[0]), int(inp[1]), int(inp[2])))
#     inp = input("Enter (b e m): ").split()
#     print(PowMod(int(inp[0]), int(inp[1]), int(inp[2])))