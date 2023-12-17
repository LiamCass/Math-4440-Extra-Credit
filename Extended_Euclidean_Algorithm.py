from math import floor

# Euclidean algorithm (slow)
def slow_gcd(a,b):
    # base case, a zero value!
    if a==0 or b==0: return a+b

    # if a is bigger than b, swap 'em!
    if a > b: a,b = b,a

    # and do it again.
    return slow_gcd(a, b-a)


def division_gcd(a,b):
    # base case, a zero value! (fully reduced)
    if a==0 or b==0: return a+b

    # if a is bigger than b, swap 'em!
    if a > b: a,b = b,a

    # and do it again.
    print(b%a, a)
    return division_gcd(b%a, a)

# Extended Euclidean algorithm (1%)
def extended_gcd(a,b):
    # Base case: fully reduced.
    if a == 0: return b, 0, 1

    gcd, x1, y1 = extended_gcd(b%a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
    print(x, y)
    return gcd, x, y

if __name__ == "__main__":
    # slow_gcd(135,170)
    # division_gcd(244,495)
    print(extended_gcd(244,495))
    "demo the algorithm"