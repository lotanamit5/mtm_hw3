from gradesCalc import *


# Testing your implemented functions, feel free to add more tests below
def main():
    # Testing the `final_grade` function
    # input_path = 'tests/input'
    # output_path = 'tests/out'
    input_path = './input'
    output_path = './out'
    course_avg = final_grade(input_path=input_path, output_path=output_path)
    print(course_avg)
    assert course_avg == 70

    # Testing the `check_strings` function
    bases = ['abcabc', 'baNaNa', '']
    tries = [['aabbcc', 'caba', 'aaa', ''],
             ['naanb', 'ananas', 'bannn'],
             ['', 'f', '1']]
    results = [[True, True, False, True],
               [True, False, False],
               [True, False, False]]

    for s1, s2, rs in zip(tries, bases, results):
        for s, r in zip(s1, rs):
            res = check_strings_v2(s, s2)
            if(res != r):
                print("TEST FAILED:", s, s2, "returned:", res)
    print("hi")

if __name__ == "__main__":
    main()
