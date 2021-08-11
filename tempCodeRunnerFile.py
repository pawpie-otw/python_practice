import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
for i in it.product(notes, repeat=4):
    print(i)