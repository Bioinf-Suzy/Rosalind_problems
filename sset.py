#sset
import itertools 
with open('rosalind_sset.txt') as f:
    n = int(f.read())

#def sset(s):
#  my_set = set(range(s))
#  ssets = list(map(lambda s: list(itertools.combinations(my_set, s)), range(1, len(my_set)+1)))  
#    sset_list = [item for sublist in ssets for item in sublist]  
#    print(len(sset_list)+1)
#sset(n)#for small n 
#print(set)
''' 
'''
#the functional sset
def sset(s):
    return (2**s)%1000000
print(sset(n))
