#fib

#import sys
#print(sys.getrecursionlimit())
#sys.setrecursionlimit(15000)

def fib(n,k):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else: 
        return fib(n-1,k)+k*fib(n-2,k)
    
print(fib(31,5))
