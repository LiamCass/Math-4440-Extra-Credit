from Extended_Euclidean_Algorithm import extended_gcd as gcd
from functools import reduce
# # Function to check if all the
# # pairs of the array are coprime
# # with each other or not
# # credit: https://www.geeksforgeeks.org/
# def allCoprime(A):
#     all_coprime = True
#     n = len(A)
#     for i in range(n):
#         for j in range(i + 1, n):
#             # Check if GCD of the
#             # pair is not equal to 1
#             if gcd(A[i], A[j])[0] != 1:

#                 # All pairs are non-coprime
#                 # Return false
#                 all_coprime = False; break
#     return all_coprime

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(m, a):
    sum = 0
    prod = reduce(lambda acc, b: acc*b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

# Solves a modular system
# https://o365coloradoedu-my.sharepoint.com/personal/kast5807_colorado_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fkast5807%5Fcolorado%5Fedu%2FDocuments%2FMath%204440%2D54440%20Fall%202023%2Flecturenotes%2F2023%2D09%2D25%2DNote%2D11%2D31%5Fannotated%2Epdf&parent=%2Fpersonal%2Fkast5807%5Fcolorado%5Fedu%2FDocuments%2FMath%204440%2D54440%20Fall%202023%2Flecturenotes&ga=1
def chinese_remainder_theorem(a, m, b, n):
    coprime_check, s, t = gcd(m,n)
    print(f"x mod {m*n} = s:{s} t:{t}")
    # x = a (mod m)
    # x = b (mod n)

    if coprime_check != 1: return "not coprime! CRT does not apply"
    # ns + mt = 1, .:
    # ns = 1 (mod m)
    # mt = 1 (mod n)

    answer_mod_m = (a * n * s)
    answer_mod_n = (b * m * t)
    # x = ans + bmt, .:
    # x = ans (mod m)
    # x = bmt (mod n)

    x = (answer_mod_m + answer_mod_n) % (m*n)
    return x, (m*n)

print(chinese_remainder_theorem(a=5,m=11,b=2,n=7))
print(chinese_remainder([11,7],[5,2]))
