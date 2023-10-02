#input
a1, a0 = [int(i) for i in input().split()]
c = int(input())
n0 = int(input())

if((c-a1)*n0 - a0 < 0):
    print(0)
elif((c-a1) < 0):
    print(0)
else :
    print(1)