from utils import bestResultFor, computeScoresXorAgainstAllChars

# Single-byte XOR cipher

x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

print bestResultFor(computeScoresXorAgainstAllChars(x)) # Cooking MC's like a pound of bacon
