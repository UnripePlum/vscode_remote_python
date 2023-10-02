#input
N = int(input())

x = N
y = 2
while(True):
    if(x==1):
        break
    if(x < y):
        break
    
    if(x%y==0):
        print(y)
        x = x//y
    else :
        y = y + 1