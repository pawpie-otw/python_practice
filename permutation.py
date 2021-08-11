import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']


for comb in it.permutations(notes, 4):
    print(comb)


def combinations_sum(items_list: list, k: int) -> int:
    """return sum of all k-word combiniontions
    from n-length list of items
    """
    n = len(items_list)
    numerator = math.factorial(n)
    denominator = math.factorial(n-k)
    return numerator//denominator


len([i for i in it.product(notes, repeat=4)])


print("suma combinacji bez powtorzen to", combinations_sum(notes, 4))
print("suma kombinacji z powtorzeniami to", math.pow(len(notes), 4))
