N = 20
SUBJECT_NAME = 0
SUBJECT_CREDIT = 1
SUBJECT_GRADE = 2

def convert_grade_to_point(grade_str):
    if(grade_str == "A+"):
        return 4.5
    elif(grade_str == "A0"):
        return 4.0
    elif(grade_str == "B+"):
        return 3.5
    elif(grade_str == "B0"):
        return 3.0
    elif(grade_str == "C+"):
        return 2.5
    elif(grade_str == "C0"):
        return 2.0
    elif(grade_str == "D+"):
        return 1.5
    elif(grade_str == "D0"):
        return 1.0
    elif(grade_str == "F"):
        return 0

total_score = 0
total_credit = 0
for _ in range(N):
    input_str_split = input().split()
    if(input_str_split[SUBJECT_GRADE] != "P"):
        total_score += float(input_str_split[SUBJECT_CREDIT]) * convert_grade_to_point(input_str_split[SUBJECT_GRADE])
        total_credit += float(input_str_split[SUBJECT_CREDIT])
print("{:.6f}".format(total_score/total_credit))