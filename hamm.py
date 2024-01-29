#hamm
with open('rosalind_hamm.txt') as f:
    l_str = f.read().split('\n')
#print(l_str)
hamm_dist = 0
for i in range(len(l_str[0])):
    if l_str[1][i-1] == l_str[0][i-1]:
        hamm_dist += 0
    else: hamm_dist +=1
print(hamm_dist)
