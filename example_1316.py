# int N <= 100

N = int(input())

# input 
word_list = []
result = 0

for i in range(N):
    word_list.append(input())


def isFinished(target_list, index):
    if(len(target_list)-1 <= index):
        return True
    else :
        return False


for list_index in range(len(word_list)):

    # compression
    word_index = 0
    isProgress = True
    target_word = list(word_list[list_index])

    while(isProgress):
        if(not isFinished(target_word, word_index)):
            if(target_word[word_index] == target_word[word_index+1]):
                target_word.pop(word_index+1)
                continue
            word_index += 1
        else :
            break
    
    # cal group letter count
    isGroupLetter = True
    for i in range(len(target_word)):
        if(target_word.count(target_word[i]) > 1):
            isGroupLetter = False
            break

    if(isGroupLetter):
        result += 1

print(result)