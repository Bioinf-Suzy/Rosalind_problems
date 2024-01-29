#prot
with open('codons.txt') as f:
    codon_list = f.read().split()
#print(codon_list)
codon_dict = {}
for i in range(0, len(codon_list),2):
#    if codon_list[i+1] in codon_dict:
#        codon_dict[codon_list[i+1]] = i
    codon_dict[codon_list[i]] = codon_list[i+1]

with open('rosalind_prot.txt') as f:
    rna = f.readline().strip('\n')
protein_seq = ''
print(len(rna)/3)
for i in range(0, len(rna), 3):
    #print(codon_dict[rna[i:i+3]])
    if codon_dict[rna[i:i+3]] == 'Stop':
        break
    else:
        protein_seq += codon_dict[rna[i: i+3]]
    #protein_seq.append(protein)
#print(len(protein_seq))
print(protein_seq)
#print(len(codon_dict))
#print(rna)
#print(new_codon_list)
