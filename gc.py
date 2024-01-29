#gc

with open('rosalind_gc.txt') as f:
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
    
    #print(new_strand)
#print(seq_dict)

highest_gc = 0
highest_gc_id = ''
for i in seq_dict.keys(): 
    c = seq_dict[i].count('C')
    g = seq_dict[i].count('G')
    gc_content = ((c+g)/len(seq_dict[i]))*100
    if gc_content> highest_gc:
        highest_gc = gc_content
        highest_gc_id = i
print(highest_gc)
print(highest_gc_id)
