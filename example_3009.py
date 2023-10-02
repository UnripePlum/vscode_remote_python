#input
x = {}
y = {}
for i in range(3):
    a, b = [int(i) for i in input().split()]
    if(a in x):
        x[a] += 1
    else :
        x[a] = 1
    if(b in y):
        y[b] += 1
    else :
        y[b] = 1
    
for key in x.keys():
    if(x[key] == 1):
        result_x = key
for key in y.keys():
    if(y[key] == 1):
        result_y = key

print(str(result_x) + " " + str(result_y))