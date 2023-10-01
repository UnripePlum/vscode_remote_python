CENT = 1
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1

unit_list = [QUARTER, DIME, NICKEL, PENNY]

#input
T = int(input())
test_list = [int(input()) for i in range(T)]

def convert_to_unit(num, unit_list, index):
    if(len(unit_list) <= index):
        return ""

    return (str(num//unit_list[index]) 
            + " " 
            + convert_to_unit(num%unit_list[index], unit_list, index+1))
 
for i in range(T):
    print(convert_to_unit(test_list[i], unit_list, 0))