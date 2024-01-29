#lcsm
with open('rosalind_lcsm.txt') as f:
    seq_list = f.read().splitlines()
#print(seq_list)
seq_dict = {}
for i in seq_list:
    if 'Rosalind' in i:
        if seq_list.index(i) != 0:
            seq_dict[new_strand] = seq
            seq = ''
            i = i.strip('>')
            seq_dict[i] = ''
            new_strand = i
        else:
            seq = ''
            i = i.strip('>')
            seq_dict[i] = ''
            new_strand = i
    else:
        seq += i
        if seq_list.index(i) == len(seq_list)-1:
            seq_dict[new_strand] = seq
new_seq_list = list(seq_dict.values())
subs_list = []
longest_seq = max(seq_dict.values(), key = len)
num_of_seqs = len(new_seq_list)

for i in range(len(longest_seq)):
    subseq = longest_seq[i]
    #print(subseq)
    common = True
    for j in range(i+1, len(longest_seq)-1,1):
        subseq += longest_seq[j]
        for k in range(num_of_seqs-1):
            #print(subseq)
            if new_seq_list[k] == longest_seq:
                continue
            if subseq in new_seq_list[k]:
                common = True
                #print(subseq)
            elif subseq not in new_seq_list[k]:
                #print(subseq)
                subseq = subseq[:-1]
                common = False
                break
        if common == False:
            if (len(subseq) > 1 and subseq not in subs_list):
                subs_list.append(subseq)
                break
        elif common == True:
            continue
for i in new_seq_list:
    #print(new_seq_list[i])
#    for j in subs_list:
#        print(j in new_seq_list[i])
    print(max(subs_list, key = len) in i)
print(max(subs_list, key=len))
#print(longest_seq)
#print(new_seq_list)
