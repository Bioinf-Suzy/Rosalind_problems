#tran
with open('rosalind_tran.txt') as f:
    files = f.read().splitlines()
#print(files)
seqs = []

for i in files:
    if 'Rosalind' in i:
        if files.index(i) == 0 or files.index(i) == 1:
            seq = ''
        else:
            seqs.append(seq)
            seq = ''
    else:
        seq += i 
        if files.index(i) == len(files)-1:
            seqs.append(seq)
            
transitions = 0
transversions = 0

trs = ['AG', 'CT', 'GA', 'TC']
trv = ['AC', 'AT', 'CA', 'CG', 'GC', 'GT', 'TA', 'TG']

for i in range(len(seqs[0])-1):
    str = seqs[0][i] + seqs[1][i]
    if seqs[0][i] == seqs[1][i]:
        continue
    elif str in trv: 
        transversions += 1
    elif str in trs:
        transitions += 1
    else: 
        print('Invalid base.')

print(transitions/transversions)
