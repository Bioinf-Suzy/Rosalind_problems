#iprb
with open('rosalind_iprb.txt') as f:
    k,m,n = [int(x) for x in next(f).split()]

def dominant_prob(k,m,n):
    t = k+m+n

    kk = k/t * ((k-1)/(t-1))
    km = k/t * (m/(t-1))
    kn = k/t * (n/(t-1))

    mm = (m/t)*((m-1)/(t-1))
    mk = (m/t)*(k/(t-1))
    mn = (m/t)*(n/(t-1))

    nk = (n/t)*(k/(t-1))
    nm = (n/t)*(m/(t-1))

    prob = round((kk + km + kn + mk + nk + 0.75*mm + 0.5*mn + 0.5*nm),5)
    return prob
print(dominant_prob(k,m,n))
