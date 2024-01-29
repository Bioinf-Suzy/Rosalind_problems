#lia

from math import factorial as f

with open('rosalind_lia.txt') as f:
    files = f.read().splitlines()
    print(files)
k = int(files[0][0])
N = int(files[0][2])

def com(n,r):
    return (f(n)/(f(r)*(f(n-r))))
    
def lia(k,N):
    total = 2**k
    prob = 0
    for i in range(N,total+1):
        prob += (com(total,i) * (0.25**i) * (0.75**(total-i)))
    return round(prob,3)
        
print(lia(5,8))
