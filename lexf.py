#lexf
from itertools import product 

with open('rosalind_lexf.txt') as f:
    files = f.read().splitlines()
#print(files)

n_perm = int(files[1])
symbols = list(files[0])
sym_list = []


for symbol in symbols:
    if symbol == " ":
        continue
    else:
        sym_list.append(symbol)
print(sym_list)

#print(files[1],files[0])
def lexf(list, n):
    perm = product(list,repeat=n)
    for i in perm:
        string = ''
        for j in i:
            string += j
        print(string)
lexf(sym_list, n_perm)
#lexf(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],3)
