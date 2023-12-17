# Input the following into the second box on this website: https://crypto.katestange.net/qkd-bb84/
# Note, L is NW/NE basis and V is horizontal/vertical. The bit's number corresponds to direction
import random

# ALICE
LENGTH = 16
Alice_bases  = ''.join([random.choice("LV") for i in range(LENGTH)])
Alice_bits   = ''.join([random.choice("01") for i in range(LENGTH)])
Alice_photons= [generate_photon(Alice_bases[i], Alice_bits[i]) for i in range(LENGTH)]
print("Alice's photons are: ", Alice_photons)

# BOB
Bob_bases    = ''.join([random.choice("LV") for i in range(LENGTH)])
Bob_photons  = [measure_photon(Bob_bases[i], Alice_photons[i]) for i in range(LENGTH)]
print("Bob has finished measuring.")

# RETRIEVE PUBLIC INFO
print("Bob's bases are:   ", Bob_bases)
print("Alice's bases are: ", Alice_bases)
mutual_bases = ''.join([ Bob_bases[i] if Bob_bases[i]==Alice_bases[i] else "_" for i in range(LENGTH)])
print("The kept bases are:", mutual_bases, end="\n\n")

shared_key   = ''.join([ Alice_bits[i] if Bob_bases[i]==Alice_bases[i] else "_" for i in range(LENGTH)])
print("The shared key is: ", shared_key)