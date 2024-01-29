#sseq
with open('rosalind_sseq.txt') as f:
    files = f.read().splitlines()

seqs = []
#print(files)
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
#print(seqs)
s = seqs[0]
t = seqs[1]

list = []
pos = 0

for i in t:
    for j in range(len(s)-1):
        if i == s[j]:
            if list == []:
                list.append(j+1)
                break
            elif j > list[pos]-1:
                list.append(j+1)
                pos += 1
                break
            else: 
                continue

print(len(t))
print(len(list))
print(*list)
