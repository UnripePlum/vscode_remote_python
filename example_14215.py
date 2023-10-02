#input
a, b, c = [int(i) for i in input().split()] 

def max(p, q):
    if(p>q):
        return p
    else :
        return q

if((2 * max(max(a,b), c)) >= a+b+c):
    print((a+b+c - max(max(a,b),c)) * 2 - 1)
else :
    print(a+b+c)