#perm
from itertools import permutations
with open('rosalind_perm.txt') as f:
    n = int(f.read())


perm = permutations(list(range(1,n+1)))
perm1 = permutations(list(range(1,n+1)))
n_perm = sum(1 for i in perm1)
print(n_perm)
for j in perm:
    print(*j)
