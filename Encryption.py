# Define the latin alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

''' BACK-END IMPLEMENTATION '''
class Cypher():
    def __init__(self) -> None:
        self.alphabet = alphabet
        self.E        = lambda x: x
        self.D        = lambda x: x

    "Applies Encryption using function E(x)"
    def encrypt(self, phrase):
        # change yall's letters into math
        encoded_phrase = self.encode(phrase)

        # goes letter by number and applies your E(x)
        # If stuff isn't in the alphabet it ignores that thing.
        for i in range(len(phrase)):
            if type(encoded_phrase[i]) == int:
                encoded_phrase[i] = self.E(encoded_phrase[i])
            elif type(encoded_phrase[i]) == str: continue
            else: raise TypeError

        # Back to letters and spit out result
        return self.decode(encoded_phrase)

    "Applies Decryption using function D(x)"
    def decrypt(self, phrase):
        # change yall's letters into math
        encoded_phrase = self.encode(phrase)

        # goes letter by number and applies your E(x)
        # If stuff isn't in the alphabet it ignores that thing.
        for i in range(len(phrase)):
            if type(encoded_phrase[i]) == int:
                encoded_phrase[i] = self.D(encoded_phrase[i])
            elif type(encoded_phrase[i]) == str: continue
            else: raise TypeError

        # Back to letters and spit out result
        return self.decode(encoded_phrase)

    # Changes letters to numbers
    def encode(self, phrase):
        encoded_str = []
        for char in phrase.lower():
            if char in self.alphabet: encoded_str.append(self.alphabet.find(char))
            else: encoded_str.append(char)
        return encoded_str

    # Changes numbers to letters
    def decode(self, phrase):
        decoded_str = ''
        for i in range(len(phrase)):
            if type(phrase[i]) == int: decoded_str += self.alphabet[phrase[i]]
            elif type(phrase[i]) == str: decoded_str += phrase[i]
            else: raise TypeError
        return decoded_str

'''Ceaser Cypher
encryption: E(x) = (x+a) mod 26
decryption: D(x) = (x-a) mod 26'''
class Ceaser(Cypher):
    def __init__(self, a:int) -> None:
        # Define the letters to encode in the order you'd like it
        self.alphabet = alphabet
        self.modular  = len(alphabet)

        # Define E(x) and D(x)
        self.E = lambda x: (x + a) % self.modular
        self.D = lambda x: (x - a) % self.modular


'''Affine Cypher
encryption: E(x) = (ax+b) mod 26
decryption: D(x) = (dx+c) mod 26'''
class Affine(Cypher):
    def __init__(self, a:int, b:int) -> None:
        # Define the key offset and alphabet used
        self.alphabet = alphabet
        self.modular  = len(alphabet)

        # Defins encryption/decryption variables
        a        = a
        b        = b
        c        = 'Multiplicative Inverse (self.a)'
        d        = -a
        if c is "undefined": raise ValueError("Chosen 'a' has to be coprime to the alphabet length")

        # Define E(x) and D(x)
        self.E = lambda x: (a*x + b) % self.modular
        self.D = lambda x: (c*x + d) % self.modular

# '''Hill Cypher
# encryption: v -> Av       (v is vector, A is matrix)
# decryption: c -> A^{-1}c  (c is vector, A is matrix)'''
# import Matrix
# class Hill(Cypher):
#     def __init__(self, key:int, alphabet=latin_alphabet) -> None:
#         self.key      = key
#         self.alphabet = alphabet
#     def encrypt(self, phrase): pass
#     def decrypt(self, phrase): pass
#     def solve(self, encrypted_phrase, decrypted=None): pass

class RSA(Cypher):
    def __init__(self) -> None:
        # key generation
            "Choose 2 random large primes p and q, with a large difference"
            "Compute n = pq, where len(n)=key length and n will be a part of the public key"
            "Compute lambda(n)=lcm(p-1, q-1) where lambda is Carmcheal's Function"
            "Choose 2<e<lambda(n) where e is coprime to lambda(n). e will be a part of the public key."
            "determine d = e^{-1} (mod lambda(n))"
            "public key consists of the modulus n and the public (or encryption) exponent e."
            "The private key consists of the private (or decryption) exponent d."
            #'''public key (n, e)'''
            #'''private key d'''
        # key distribution
            "Alice transmits her public key (n, e) to Bob via a reliable, but not necessarily secret, route."
        # encryption
            "E(x) = (m^e) % n, where m is the padded plaintext"
        # decryption
            "D(x) = (c^d) % n, where c is the encrypted message."

    def signature(self):
        "Alice produces a hash value of the message"
        "Alice raises the hash value to the power d (mod n)"
        "Bob raises Alice's value to e (mod n)"
        "Bob compares his value to the hash value of the message"

    def generate_public_key(self): pass
    def generate_private_key(self): pass
    def encrypt(self, phrase, public_key): pass
    def decrypt(self, phrase, private_key): pass

# '''Diffie-Hellman Key Exchange:
# Used to create a shared secret.'''
# def key_exchange(g, p):
#     g = "primitive root for Z/pZ"
#     p = "a large prime"

#     # Alice's Information
#     secret_key_alice = "0 < a < p-1"

#     # Bob's Information
#     secret_key_bob   = "0 < b < p-1"

#     # Public Information (Eve's info)
#     message_Alice_1 = "g^a"
#     message_Bob_1   = "g^b"

#     # Encoding
#     recieved_key_Alice = "(g^a)^b"
#     recieved_key_Bob   = "(g^b)^a"

#     # Necessary problem for public decoding of key
#     "Given g^a (mod p) and g^b (mod p), compute g^ab (mod p)"

class Elliptic(Cypher): pass
class Quantum(Cypher): pass