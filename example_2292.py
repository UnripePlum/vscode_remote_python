#input
N = int(input())

def room_count(total, target_num, count):
    if(total > target_num):
        return 1
    return room_count(total+(count+1)*6, target_num, count+1) + 1

if(N==1):
    print("1")
else :
    count = 0
    total = 0
    target_num = N-2
    while(total <= target_num):
        count += 1
        total += 6*(count)
    print(count+1)

