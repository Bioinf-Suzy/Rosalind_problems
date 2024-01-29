#grph

with open('rosalind_grph.txt') as f:
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

def overlap(seq1, seq2,k ):
    if seq1[-k:] == seq2[:k]:
        return True
graph = []    
def edges(seq_dict, k=3):
    for n1,seq1 in seq_dict.items():
        for n2,seq2 in seq_dict.items():
            if n1 != n2 and overlap(seq1, seq2, k):
                graph.append([n1, n2])
    for i in graph:
        print((str(i)[1:-1]).replace('\'', '').replace(',',''))    
edges(seq_dict)
