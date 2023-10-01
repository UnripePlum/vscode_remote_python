#input
result = ""
while(True):
    n = int(input())
    if(n == -1):
        print(result[:len(result)-1])
        break
    
    isPerfect = False
    l_list = []
    sum = 0
    for i in range(n//2 + 1):
        if(i == 0):
            continue
        
        if(n%i == 0):
            l_list.append(i)
            sum += i
        
        if(sum > n):
            isPerfect = False
            break

        if(sum == n):
            isPerfect = True
    
    if(isPerfect):
        result += str(n) + " = "
        for j in range(len(l_list)):
            if(j == len(l_list) - 1):
                result += str(l_list[j])
                continue
            result += str(l_list[j]) + " + "
    else :
        result += str(n) + " is NOT perfect."
    result += "\n"
