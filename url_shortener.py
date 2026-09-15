CHARACTERS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def base62_encode(number):
    if number == 0 :
        return CHARACTERS[0];

    result=[]

    while number:
        remainder = number % 62
        result.append(CHARACTERS[remainder])
        number = number//62
    
    return ''.join(reversed(result))

print(base62_encode(0))
print(base62_encode(10))
print(base62_encode(61))
print(base62_encode(62))
print(base62_encode(63))