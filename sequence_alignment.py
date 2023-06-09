import Bio.Seq as seq
import random

def generate_random_sequence(length): # return Sequence object
    bases = ['A', 'T', 'G', 'C']
    chars = random.choices(bases, k=length)
    sequence = "".join(chars)
    return seq.Seq(sequence)

seq = generate_random_sequence(10)
print(seq)
print(seq.complement())

# Needleman-Wunsch Algorithm implementation (https://en.wikipedia.org/wiki/Needleman–Wunsch_algorithm#:~:text=The%20Needleman–Wunsch%20algorithm%20is,Needleman%20and%20Christian%20D.)

