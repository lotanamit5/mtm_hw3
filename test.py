from gradesCalc import *


# Testing your implemented functions, feel free to add more tests below
def main():
    # Testing the `final_grade` function
    # input_path = 'tests/input'
    # output_path = 'tests/out'
    input_path = './input1.txt'
    output_path = './output1.txt'
    course_avg = final_grade(input_path=input_path, output_path=output_path)
    print(course_avg)
    # assert course_avg == 70

    # Testing the `check_strings` function
    bases = ['abcabc', 'baNaNa', '']
    tries = [['aabbcc', 'caba', 'aaa',''],
             ['naanb', 'ananas', 'bannn'],
             ['', 'f','1']]
    results = [[True, True, False,True],
               [True, False, False],
               [True, False,False]]

    for i, s2 in enumerate(bases):
        for j, s1 in enumerate(tries[i]):
            # print("Test", j+1, 'on', s2, "trying", s1)
            res = check_strings_v2(s1, s2)
            if(res != results[i][j]):
                print("TEST FAILED:", s1, s2, "returned:", res)


if __name__ == "__main__":
    main()
