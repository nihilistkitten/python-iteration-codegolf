char_count=lambda x,y=0:{i:x.count(i) for i in x}
down_up=lambda x,y=0:[abs(i)+1 for i in range(1-x,x)]
def make_even(x):x[:]=[i&~1 for i in x]
has_duplicates=lambda x,y=0:len({*x})<len(x)
primes_list=lambda x,y=0:[i for i in range(2,2+x*x)if all(i%n for n in range(2,i))][:x]
filter=lambda x,y=0:[i for i in y if x(i)]
inverse=lambda x,y=0:{(v:=x[i]):[i for i in x if x[i]==v] for i in x}
counts=lambda x,y=0:[y.count(i) for i in range(x)]
