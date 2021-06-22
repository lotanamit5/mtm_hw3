def calcGrade(student_id: str, avg: str) -> int:
    n = len(student_id)
    sub = student_id[-2:]
    digits = int(sub)
    total = (digits+int(avg))//2
    return total


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


def check_strings(s1: str, s2: str) -> bool:
    s1 = s1.lower()
    s2 = s2.lower()
    for c in s1:
        if c in s2:
            s2.replace(c, "", 1)
        else:
            return False
    return True


print(check_strings("baNAna", "NNjd"))
