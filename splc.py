#splc
with open('codons.txt') as f:
    codon_list = f.read().split()
    
codon_dict = {}
for i in range(0, len(codon_list),2):
    codon_dict[codon_list[i]] = codon_list[i+1]

with open('rosalind_splc.txt') as f:
    seqs = f.read().splitlines()

introns = []
for i in seqs:
    if 'Rosalind' in i:
        if seqs.index(i) == 0 or seqs.index(i) == 1:
            seq = ''
        else:
            introns.append(seq)
            seq = ''
    else:
        seq += i 
        if seqs.index(i) == len(seqs)-1:
            introns.append(seq)
seq = introns[0]
new_seq = seq
introns = introns[1:]
for intron in introns:
    if intron in seq:
        seq = seq.replace(intron, '')
    
rna = ''
for i in seq:
    if i == 'T':
        rna += 'U'
    else: 
        rna += i

protein_seq = ''
for i in range(0, len(rna), 3):
    
    if len(rna[i:i+3]) < 3:
        break
    elif codon_dict[rna[i:i+3]] == 'Stop':
        break
    else:
        protein_seq += codon_dict[rna[i: i+3]]

print(protein_seq)
