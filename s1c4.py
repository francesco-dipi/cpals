from utils import *

# Detect single-character XOR

x = open('4.txt', 'r').read().splitlines()

print bestResultFor(sum([computeScoresXorAgainstAllChars(s) for s in x], []))   # Now that the party is jumping
