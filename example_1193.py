#input
N = int(input())

def sum_integer(target_num):
    total = 0
    count = 0
    remain = 0
    while(total < target_num):
        count += 1
        total += count
    remain = target_num - (total - count)
    return count, remain

def cal_fraction(sum, index):
    if(sum % 2 == 1):
        return str(sum-index+1) + "/" + str(index)
    else :
        return str(index) +"/"+ str(sum-index+1)
sum, index = sum_integer(N)
print(cal_fraction(sum, index))