def squares(n, m):
    assert n >= 0 and m >= 0 and n + m > 0

    a = n
    b = m

    while (b > 0 and a > 0):
        if (a <= b):
            b = b % a
        elif (b < a):
            a = a % b
    return (n * m) // ((a + b) ** 2)

# testing
# 
# inp = ""
# while inp != "eee":
#     inp = input("Enter dimensions of floor (n m): ").split()
#     print(squares(int(inp[0]), int(inp[1])))
