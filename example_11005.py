#input
input_str = input().split()
N, B = int(input_str[0]), int(input_str[1])

def num_to_str(num):
    if(num<10):
        return str(num)
    else:
        return chr(num+55)
    
def convert_B_format(N, B):
    if(N == 0):
        return ""
    return convert_B_format(N//B, B) + num_to_str(N%B)

print(convert_B_format(N,B))