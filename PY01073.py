from itertools import permutations

s=input()
a=permutations(s)
for i in a:
    print("".join(i))