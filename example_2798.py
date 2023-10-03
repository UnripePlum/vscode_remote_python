#input
N, M = [int(i) for i in input().split()]

arr = [int(i) for i in input().split()]

max_sum = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1,N):
            sum = arr[i] + arr[j] + arr[k]
            if(sum > M):
                continue
            if(max_sum < sum):
                max_sum = sum
print(max_sum)