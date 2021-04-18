#!/bin/python3

import os


def grading_students(grades):
    """ Returns rounded grades """

    rounded_grades = []

    for grade in grades:
        if grade > 37 and grade % 5 > 2:             # If grade ends with 3, 4, 8 or 9
            rounded_grade = grade + (5 - grade % 5)  # Round up to nearest multiple of 5
        else:
            rounded_grade = grade

        rounded_grades.append(rounded_grade)

    return rounded_grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    student_grades = []   # Grades

    for _ in range(grades_count):
        grades_item = int(input().strip())
        student_grades.append(grades_item)

    result = grading_students(student_grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
