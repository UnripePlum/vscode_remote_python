#DEFINE CONST
CEQUEL = "c="
CMINUS = "c-"
DZEQUEL = "dz="
DMINUS = "d-"
LJ = "lj"
NJ = "nj"
SEQUEL = "s="
ZEQUEL = "z="

letter_list = [CEQUEL, CMINUS, DZEQUEL, DMINUS, LJ, NJ, SEQUEL, ZEQUEL]

word = input()

result = 0
isFind = False
i = 0
while(i < len(word)):
    #print(i)
    for j in range(len(letter_list)):
        target_str = ""
        for k in range(len(letter_list[j])):
            if(len(word) > i+k ):
                target_str += word[i+k]

        #print(target_str, letter_list[j])
        if(letter_list[j] == target_str):
            result += 1
            i += len(letter_list[j])
            isFind = True
            break
    
    if(not isFind):
       result += 1
       i += 1
    else :
        isFind = False
print(result)