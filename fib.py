#fib

#import sys
#print(sys.getrecursionlimit())
#sys.setrecursionlimit(15000)
with open('rosalind_fib.txt') as f:
    n,k = [int(x) for x in next(f).split()]
#print(n,k)

def fib(n,k):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else: 
        return fib(n-1,k)+k*fib(n-2,k)
    
print(fib(n,k))
