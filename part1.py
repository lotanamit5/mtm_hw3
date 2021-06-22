def calcGrade(student_id: str, avg: str) -> int:
    length = len(student_id)
    sub = student_id[length-2:length]
    digits = int(sub)
    total = (digits+int(avg))//2
    return total


def numOfDigits(number: int) -> int:
    n = int(number)
    count = 0
    while(n > 0):
        count = count+1
        n = n//10
    return count


def final_grade(input_path: str, output_path: str) -> int:

    input_f = open(input_path, 'r')
    output_f = open(output_path, 'w')
    lines = input_f.readlines()

    dict = {}
    # get info from input and put in dict:
    for line in lines:
        #line=line.replace(' ', '').replace('\n', '')
        line = "".join(line.split()) #removes all whitespaces
        if(len(line) > 0):
            info = line.split(',')
            student_id = info[0]
            name = info[1]
            semester = info[2]
            avg = info[3]
            if(student_id.isnumeric() and student_id[0] != '0' and numOfDigits(student_id)
               and name.isalpha()
               and semester.isnumeric() and int(semester) >= 1
               and avg.isnumeric() and int(avg) > 50 and int(avg) <= 100):
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
    return totalgrade//len(dict)


# main
final_grade("./input.txt", "./output.txt")
