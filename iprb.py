#iprb
def iter_factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def rec_factorial(n):
    if n == 1:
        return 1
    else:
        res = n * rec_factorial(n-1)
        return res
      
print(rec_factroial(4))
