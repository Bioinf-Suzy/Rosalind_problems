#cons 
import itertools
import numpy as np
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
#print(seq_dict)
#zero_list = list(itertools.repeat(0,len(seq_dict[new_strand])))
zero_arr = np.zeros(len(seq_list[0]))
data = {'A':zero_arr, 'G':zero_arr, 'C':zero_arr, 'T':zero_arr}
for key,value in seq_dict.items():
    for i in range(len(value)):
        data[value[i]] += 1
print(data)
