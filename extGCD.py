def extended_gcd(a, b):
    # gcd(a, b) = ax + by

    assert a >= 0 and b >= 0 and a + b > 0

    if b==0:
        d = a
        x = 1
        y = 0
    else:
        d, p, q = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return d, x, y