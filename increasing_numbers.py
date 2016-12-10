'''
Codewars - Increasing Numbers

Last Updated: 2016-Dec-07
First Created: 2016-Dec-07
Python 3.5
Chris

https://www.codewars.com/kata/increasing-numbers-with-n-digits/

'''

def increasing_numbers_brute(digits):
    '''
    An increasing number is one whose digits (left to right) increase in value. For example, 1235 is an increasing number.
    Write a function that finds the number of increasing numbers with N digits.
    You'll definitely need something smarter than brute force for large values of N!
    Note: A "3 digit" number includes zero-padded, smaller numbers, such as 001, 002, up to 999.
    '''
    if digits == 0:
        return 1

    answers = []
    number = 0
    while len(str(number)) <= digits:
        add_flag = True
        str_num = str(number).rjust(digits - len(str(number)) + 1, '0')
        print(str_num)
        for idx in range(len(str_num)):
            if idx > 0:
                if int(str_num[idx]) < int(str_num[idx - 1]):
                    add_flag = False
                    break
        if add_flag:
            answers.append(str_num)

        number += 1

    return len(answers)

def increasing_numbers(digits):
    '''
    An increasing number is one whose digits (left to right) increase in value. For example, 1235 is an increasing number.
    Write a function that finds the number of increasing numbers with N digits.
    You'll definitely need something smarter than brute force for large values of N!
    Note: A "3 digit" number includes zero-padded, smaller numbers, such as 001, 002, up to 999.
    '''
    answers = [[0]]

    if digits == 0:
        return 1

    while len(answers) <= digits:
        answers.append([])
        for prev_ans in answers[-2]:
            for num in range(int(str(prev_ans)[-1]), 10):
                answers[-1].append(int(str(prev_ans) + str(num)))
    return len(answers[-1])

from math import factorial
def increasing_numbers(digits):
    return factorial(9 + digits) / (factorial(digits) * factorial(9)) if digits > 0 else 1


def testing_brute():
    print(increasing_numbers_brute(0),1)
    print(increasing_numbers_brute(1),10)
    print(increasing_numbers_brute(2),55)
    print(increasing_numbers_brute(3),220)
    print(increasing_numbers_brute(3),220)
    print(increasing_numbers_brute(4),715)

def testing():
    print(increasing_numbers(0),1)
    print(increasing_numbers(1),10)
    print(increasing_numbers(2),55)
    print(increasing_numbers(3),220)
    print(increasing_numbers(3),220)
    print(increasing_numbers(4),715)
    print(increasing_numbers(10))

#testing()
#testing_brute()
