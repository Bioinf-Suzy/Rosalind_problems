#mrna
with open('codons.txt') as f:
    codon_list = f.read().split()
#print(codon_list)
codon_dict = {}
for i in range(0, len(codon_list),2):
#    if codon_list[i+1] in codon_dict:
#        codon_dict[codon_list[i+1]] = i
    codon_dict[codon_list[i]] = codon_list[i+1]
#print(codon_dict)
with open('rosalind_mrna.txt') as f:
    aa_seq = f.readline().strip('\n')
#print(aa_seq)
aa_freq = {}
for codon, aa in codon_dict.items():
    if aa in aa_freq.keys():
        aa_freq[aa] += 1
    else:
        aa_freq[aa] = 1
#print(aa_freq)
n_encodings = aa_freq['Stop']
for aa in aa_seq:
    n_encodings = n_encodings*aa_freq[aa]
#print(n_encodings)
mod_n_encod = (n_encodings) % 1000000
print(mod_n_encod)
