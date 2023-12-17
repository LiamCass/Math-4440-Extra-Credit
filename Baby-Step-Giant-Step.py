from math import ceil
from math import sqrt

# Baby step giant step, used to solve discreet logarithm problem.
# Lets say you have a problem in the form...
# g^a = h (mod p)       log_g(h) (mod p) = ?
# Input your base g, the solution h, and your modulus p to solve!
def baby_step_giant_step(g,h,p):
    # N tells us when to stop looking for steps
    N = ceil( sqrt(p-1) )
    n = 1

    # baby steps, [] g, g^2, ... g^(N) ]
    baby_steps  = [ (g**i)%p for i in range(1,N+1) ]
    print(f"Baby steps: {baby_steps}")

    # Calculate giant steps
    k = 1
    while True:
        exponent   = (p - N*k) % p
        giant_step = (h * (g ** exponent)) % p
        print(f"Giant step {k}: {giant_step}")

        # Find where giant steps match, or continue.
        try:
            j = baby_steps.index(giant_step)
            return j + k*N
        except ValueError:
            k += 1
            if k<=p: continue
            else:    return None

a = baby_step_giant_step(2,17,121)
print(f"Discreet log is {a}")
