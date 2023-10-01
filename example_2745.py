#input
input_str = input().split()
B_format_N, B = list(input_str[0]), int(input_str[1])

def convert_10_format(num_str, square_num, index):
    if(len(num_str) == 0):
        return 0
    
    
    num = str_to_num(num_str.pop())
    multi_num = square_num**index
    return num * multi_num + convert_10_format(num_str, square_num, index+1)

def str_to_num(one_str):
    if(one_str.isnumeric()):
        return int(one_str)
    else:
        return ord(one_str) - 55

print(convert_10_format(B_format_N, B, 0))