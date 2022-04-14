R=range
down_up=lambda n:[*R(n,1,-1),*R(1,n+1)]
filter=lambda p,l:[x for x in l if p(x)]
def make_even(l):l[:]=[x&~1for x in l]
char_count=lambda s:{c:s.count(c)for c in s}
counts=lambda n,l:[*map(l.count,R(n))]
primes_list=f=lambda n,k=1,p=1:n*[0]and p%k*[k]+f(n-p%k,k+1,p*k*k)
has_duplicates=lambda l:len({*l})<len(l)
inverse=lambda d:{d[K]:[k for k in d if d[k]==d[K]]for K in d}
