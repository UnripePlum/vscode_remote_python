#input
M = int(input())
N = int(input())

def isPrime(num):
    if(num <= 1):
        return False

    for i in range(num//2+1):
        if(i==0 or i==1):
            continue
        if(num%i==0):
            return False
    
    return True

result = 0
isMin = True
min_num = 0
for i in range(M,N+1):
    if(isPrime(i)):
        result += i

        if(isMin):
            min_num = i
            isMin = False
    
if(result == 0):
    print("-1")
else :
    print(str(result) + "\n" + str(min_num))

            
