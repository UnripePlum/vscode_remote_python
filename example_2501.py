#input
N, K = [int(i) for i in input().split()]

count = 0
var_x = 0
while (count < K):

    var_x += 1
    if(var_x > N):
        var_x = 0
        break
    if(N%var_x == 0):
        count += 1
    
print(var_x)