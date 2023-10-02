#input
x, y, w, h = [int(i) for i in input().split()]

def get_min(p, q):
    if(p>q):
        return q
    else :
        return p

print(get_min(get_min(x, w-x), get_min(y, h-y)))