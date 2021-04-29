if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Sort students by grade
    sorted_students = sorted(students, key=lambda student: student[1])

    # Exclude students with the worst grades
    exclude_worst = [student for student in sorted_students
                     if student[1] != sorted_students[0][1]]

    # Select only the students with the second worst grades
    second_worst = [student[0] for student in exclude_worst
                    if student[1] == exclude_worst[0][1]]

    # Sort and print names in alphabetical order
    for name in sorted(second_worst):
        print(name)
