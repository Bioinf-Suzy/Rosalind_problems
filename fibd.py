#fibd
with open('rosalind_fibd.txt') as f:
    n,m = [int(x) for x in next(f).split()]

dict1 = {1:1, 2:1}

def fibd(n,m, dict = {}):
    #print(n)
    if n in dict.keys():
        return dict[n]
    elif n == 1:
        dict[n] = 1
        return 1
    elif n <= 0:
        return 0
    elif n<=m:
        dict[n] = fibd(n - 1, m, dict) + fibd(n - 2, m, dict)
        return dict[n]
    elif n ==m+1:
        dict[n] = fibd(n - 1, m,dict) + fibd(n - 2, m, dict) - fibd(n - m, m, dict)
        return  dict[n]
    else:
        dict[n] = (fibd(n-1,m, dict) + fibd(n-2,m,dict) - fibd(n-m-1,m, dict))
        
        return(dict[n])
    
print(fibd(n,m))
