#dna
with open('rosalind_rna.txt') as f:
    dna = f.read()

a = dna.count('A')
c = dna.count('C')
g = dna.count('G')
t = dna.count('T')
print(a,c,g,t)
