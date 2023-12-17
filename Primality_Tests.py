import random
# Fermat Primality Test
def fermat_primality(prime, accuracy=5):
    # Corner cases.
    if prime == 1 or prime == 4:   return False
    elif prime == 2 or prime == 3: return True

    # Test.
    for i in range(accuracy):
        a = random.randint(2,prime-2)
        if (a**(prime-1)) % prime != 1: return False
    return True

# Miller Rabin Primality Test
def miller_rabin(prime, accuracy=5):
    d = prime-1
    s = 0
    while True:
        if d % 2 == 0:
            d = int(d/2)
            s += 1
        else: break
    print(f"{prime-1} = 2^{s} * {d}")

    for i in range(accuracy):
        a = random.randint(2, prime-1)

        # compute a ** d % prime without overflow
        x = a
        for i in range(d):
            x = (x * a) % prime

        if x == prime-1: return True
        if x == 1:       return False
    return False

print(fermat_primality(2003))
print(fermat_primality(2001))
print(miller_rabin(90751))