#input
N = int(input())

def max(p, q):
    if(p>q):
        return p
    else :
        return q
def min(p, q):
    if(p>q):
        return q
    else :
        return p
    

for i in range(N):
    x, y = [int(i) for i in input().split()]
    if(i == 0):
        min_x = x
        max_x = x
        min_y = y
        max_y = y
    else :
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

print((max_x - min_x) * (max_y - min_y))
