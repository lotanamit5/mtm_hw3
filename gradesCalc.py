#### PART 1 ####
# calcGrade: Calculate the total final grade of a student
# student_id: the student's id as string
# avg: the student's homework averege as a string
def calcGrade(student_id: str, avg: str) -> int:
    n = len(student_id)
    sub = student_id[-2:]
    digits = int(sub)
    total = (digits+int(avg))//2
    return total

# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output


def final_grade(input_path: str, output_path: str) -> int:
    input_f = open(input_path, 'r')
    output_f = open(output_path, 'w')
    lines = input_f.readlines()

    dict = {}
    # get info from input and put in dict:
    for line in lines:
        line = "".join(line.split()).strip()  # removes all whitespaces
        if(len(line) > 0):
            # info = line.split(',')
            # student_id, name, semester, avg = info[0], info[1], info[2], info[3]\
            student_id, name, semester, avg = line.split(',', 4)
            
            print(student_id, name, semester, avg)
            print(student_id.isdecimal() and student_id[0] != '0' and len(student_id) == 8)
            print(name.isalpha())
            print(semester.isdecimal() and int(semester) >= 1)
            print(avg.isdecimal() and int(avg) > 50 and int(avg) <= 100)
            print()
            
            if(student_id.isdecimal() and student_id[0] != '0' and len(student_id) == 8
               and name.isalpha()
               and semester.isdecimal() and int(semester) >= 1
               and avg.isdecimal() and int(avg) > 50 and int(avg) <= 100):
                dict[student_id] = avg
                

    totalgrade = 0
    # write the dict to the output file and calculate the course avg:
    for key, val in sorted(dict.items()):
        final_grade = calcGrade(key, val)
        totalgrade += final_grade
        line = ", ".join((key, val, str(final_grade)))+'\n'
        output_f.write(line)
    # print(dict)

    # close files and return avg:
    input_f.close()
    output_f.close()
    if(len(dict) != 0):
        return totalgrade//len(dict)
    else:
        return 0


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:
    hist1 = [0]*26
    hist2 = [0]*26
    s1 = s1.lower()
    s2 = s2.lower()
    for s in s1:
        hist1[ord(s) - ord('a')] += 1
    for s in s2:
        hist2[ord(s) - ord('a')] += 1
    for i in range(0, 26, 1):
        if hist1[i] > 0 and hist2[i] == 0:
            return False
        if hist1[i] > 0 and hist2[i] > 0 and hist1[i] > hist2[i]:
            return False
    return True


def check_strings_v2(s1: str, s2: str) -> bool:
    s1 = s1.lower()
    letters = list(s2.lower())
    for c in s1:
        if c in letters:
            letters.remove(c)
        else:
            return False
    return True
