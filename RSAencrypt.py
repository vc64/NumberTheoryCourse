from FastModExp import PowMod

def ConvertToInt(message):
    # goes through message and returns int as if 
    # it was all one hex number 

    total = 0

    message = message[::-1]

    prev_len = 0

    for x in message:
        curr = ord(x) * (16 ** prev_len)
        total += curr

        prev_len += len(hex(ord((x)))) - 2

    return total


def Encrypt(message, modulo, exponent):
    # c = m^e mod n
    # encrypted text = message ^ exponent mod modulo

    message_int = ConvertToInt(message)

    assert message_int >= 0 and message_int < modulo

    return PowMod(message_int, exponent, modulo)


# testing
# 
# inp = ""
# while inp != "eee":
#     inp = input("Enter (messsage, modulo, exponent): ").split(",")
#     print(inp)
#     print(Encrypt(inp[0], int(inp[1]), int(inp[2])))

# inp = ""
# while inp != "eee":
#     inp = input("Enter (messsage): ")
#     print(ConvertToInt(inp))