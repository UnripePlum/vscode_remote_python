#input
N = int(input())

def cal_num_slide_point(index):
    if(index == 0):
        return 2
    
    return 2*cal_num_slide_point(index-1) - 1

print(cal_num_slide_point(N)**2)