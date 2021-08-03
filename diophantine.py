from extGCD import extended_gcd

def diophantine(a, b, c):
    # c = t * (ax + by)
    # c = t * gcd(a,b)

    d, x, y = extended_gcd(a, b)

    assert c % d == 0

    t = c // d
    x *= t
    y *= t

    return (x, y)

# testing
# 
# inp = ""
# while inp != "eee":
#     inp = input("Enter (a b c): ").split()
#     print(diophantine(int(inp[0]), int(inp[1]), int(inp[2])))