#input
N = int(input())

def power_10(x):
    result = 0
    while(x != 0):
        x = x//10
        result += 1
    return result
def add_all_digit(x):
    result = 0
    while(x != 0):
        result += (x%10)
        x = x//10
    return result

isFind = False

for i in range(N-9*power_10(N), N):
    if(i<=0):
        continue
    if((add_all_digit(i)+i) == N):
        print(i)
        isFind = True 
        break
if(not isFind):
    print(0)