import random

'''Diffie-Hellman Key Exchange:
Used to create a shared secret.'''
def diffie_hellman(g, p):
    "g = primitive root for Z/pZ"
    "p = a large prime"
    print(f"Diffie-Hellman key exchange demo, using prime number {p} and primitive root {g}")
    print('')

    # Alice's Information
    secret_key_alice = random.randint(0,p-1)
    print("Alice generates her private key a, a random integer between 0 and p")

    # Bob's Information
    secret_key_bob   = random.randint(0,p-1)
    print("Bob   generates his private key b, a random integer between 0 and p")

    # Public Information (Eve's info)
    print('')
    message_alice    = (g ** secret_key_alice) % p
    message_bob      = (g ** secret_key_bob) % p
    print(f"Alice shares her public key: g^a (mod p)  = {message_alice}")
    print(f"Bob   shares his public key: g^b (mod p)  = {message_bob}")

    # Encoding private shared keys
    recieved_key_Alice = (message_bob ** secret_key_alice) % p
    recieved_key_Bob   = (message_alice ** secret_key_bob) % p
    shared_key = recieved_key_Alice if recieved_key_Alice==recieved_key_Bob else None
    print(f"Congrats! The shared key is: g^ab (mod p) = {shared_key}")

if __name__ == "__main__":
    primitive_root = 2
    large_prime = 349
    diffie_hellman(primitive_root, large_prime)