#input
n = int(input())

result = 0
for i in range(n-2):
    result += (n-2-i)*(n-1-i)//2

print(str(result) + "\n3")