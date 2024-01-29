#cons
import numpy as np
import sys

with open('rosalind_cons.txt') as f:
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

matrix = np.zeros((4, len(max(seq_dict.values(),key=len))))
#matrix = np.array((4, len(max(seq_dict.values(),key=len))))
base_dict = {'A':0, 'C':1, 'G':2, 'T':3}
bases = list(base_dict.keys())
#print(zero_matrix)
#print(len(max(seq_dict.values(),key=len)))
cons_seq = ''
for seq in seq_dict.values():
    for i in range(len(seq)):
        #print(i)
        base = seq[i]
        
        matrix[base_dict[base]][i] += 1

for i in range(len(matrix[0])):
    max = 0
    base = ''
    for j in range(4):
        if matrix[j][i] >= max:
            max = matrix[j][i]
            base = bases[j]
    cons_seq += base
    
#print(bases[1])    
#base_count_dict = dict.fromkeys(base_dict.keys(), list in matrix)
#dict(key:value for key in base_dict.keys(), value in matrix.astype(int))
#dict = {'A': 

#print(cons_seq)
print('A:', *matrix[0].astype(int))
#print('A:', (np.savetxt(sys.stdout,matrix[0].astype(int),fmt="%i",newline = ' ')))
print('C:', *matrix[1].astype(int))
print('G:', *matrix[2].astype(int))
print('T:', *matrix[3].astype(int))
