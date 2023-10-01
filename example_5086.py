# input
result = ""
while(True):
    a,b = [int(i) for i in input().split()]

    if(a == 0 and b == 0):
        break

    if(b%a == 0):
        result += "factor" + "\n"
    elif(a%b == 0):
        result += "multiple" + "\n"
    else :
        result += "neither" + "\n"

print(result[:len(result) - 1])
