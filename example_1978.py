#input
N = int(input())

num_list = [int(i) for i in input().split()]
result = 0
for i in range(len(num_list)):
    
    if(num_list[i] == 1):
        continue
    
    isPrime = True
    for j in range(num_list[i]):
        
        if(j == 0 or j == 1):
            continue
        
        if(num_list[i]%j==0):
            isPrime = False
            break
    
    if(isPrime):
        result += 1
    
print(result)