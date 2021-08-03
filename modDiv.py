from extGCD import extended_gcd
from diophantine import diophantine


# =======================================================
# CORRECTIONS LABELED WITH COMMENTS
# =======================================================


def divide(a, b, n):
    assert n > 1 and a > 0 and extended_gcd(a, n)[0] == 1

    inverse = diophantine(a, n, 1)[0]

    # ================================
    # ORIGINAL: return b * (inverse % n)
    # Correction: return (b * inverse) % n
    # This correction fixes the issue
    #  where the output is greater than n 
    #  by taking mod n at the end
    # ================================
    return (b * inverse) % n

# testing
# 
# inp = ""
# while inp != "eee":
#     inp = input("Enter (a b c): ").split()
#     print(divide(int(inp[0]), int(inp[1]), int(inp[2])))