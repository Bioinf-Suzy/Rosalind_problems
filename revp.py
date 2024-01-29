#revp
with open('rosalind_revp.txt') as f:
    files = f.read().splitlines()

seqs = ''   
for i in files:
    if 'Rosalind' in i:
        continue
    else:
        seqs += i 
        #if files.index(i) == len(files)-1:
        #    seqs.append(seq)   
    
#print(files)
#seqs = files[1]
#print(seqs)
#print(seqs[:4:-1])
#print(len(seqs))
rev = seqs.replace('A', '+')
rev = rev.replace('T', 'A')
rev = rev.replace('+', 'T')
rev = rev.replace('G', '*')
rev = rev.replace('C', 'G')
rev = rev.replace('*', 'C')
#print(rev)
for i in range(len(seqs)):
    for j in range(2,7):
        #print(j)
        #print(seqs[i:(i+j)])
        seq  = seqs[i:(i+j)]

        #print(rev)
        #print(seq[::-1])##
        coseq = rev[i+j:i+j+j]
        if seq == coseq[::-1]:
            #print(seqs[i:i+j+j], coseq)
            
            #print(seq+coseq)
            print(i+1, j*2)
