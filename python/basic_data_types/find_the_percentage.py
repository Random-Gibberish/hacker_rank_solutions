if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()       # Student name and scores
        scores = list(map(float, line))
        student_marks[name] = scores        # key=name and values=scores

    query_name = input()

    # Print the average grade of a student
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f'{average:.2f}')
