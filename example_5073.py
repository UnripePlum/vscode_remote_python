def max(p, q):
    if(p>q):
        return p
    else :
        return q
def min(p, q):
    if(p>q):
        return q
    else :
        return p

result = ""
while(True):
    a, b, c = [int(i) for i in input().split()]
    if(a == b and b == c and a == 0):
        break
    
    if((2 * max(max(a, b), c)) >= (a + b + c)):
        result += "Invalid\n"
        continue
    
    if(a == b and b == c):
        result += "Equilateral\n"
    elif(a==b or b==c or c==a):
        result += "Isosceles\n"
    else :
        result += "Scalene\n"

print(result[:len(result)-1])