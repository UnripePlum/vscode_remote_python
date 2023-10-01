#input
A, B, V = [int(i) for i in input().split()]

cur = 0

date = (V-A)//(A-B) + (0 if (V-A)%(A-B) == 0 else 1) + 1

print(date)