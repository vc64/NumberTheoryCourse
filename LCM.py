def gcd(a, b):
    # continuously finds remainders in the following kind of process
    # i.e. a = 7 b = 5
    # 7 = 5 * 1 + 2
    # 5 = 2 * 2 + 1
    # 2 = 1 * 2 + 0
    # now that b = 0, we know the gcd is 1

    assert a >= 0 and b >= 0 and a + b > 0

    while (b > 0 and a > 0):
        if (a <= b):
            b = b % a
        elif (b < a):
            a = a % b
    return a+b

def lcm(a, b):
    # a * b = gcd(a, b) * lcm(a, b)

    assert a > 0 and b > 0
    
    d = gcd(a, b)

    return a * b // d


# testing
# 
# inp = ""
# while inp != "eee":
#     inp = input("Enter (a b): ").split()
#     print(lcm(int(inp[0]), int(inp[1])))

