from extGCD import extended_gcd

def ChineseRemainderTheorem(n1, r1, n2, r2):
   (d, x, y) = extended_gcd(n1, n2)
   
   out = r2 * n1 * x + r1 * n2 * y

   if (out < 0):
       return out % (n1 * n2)

   return out


# testing
# 
# inp = ""
# while inp != "eee":
#     inp = input("Enter (n1 r1 n2 r2): ").split()
#     print(ChineseRemainderTheorem(int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3])))