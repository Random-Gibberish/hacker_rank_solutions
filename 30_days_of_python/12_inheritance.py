class Person:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def print_person(self):
        print("Name:", self.last_name + ",", self.first_name)
        print("ID:", self.id_number)


class Student(Person):
    """ Returns the average letter grade of a
        Person from their grades out of 100 """

    def __init__(self, first_name, last_name, id_number, scores):
        super().__init__(first_name, last_name, id_number)
        self.scores = scores

    @staticmethod
    def calculate(scores):
        average = sum(i for i in scores) / len(scores)

        if 90 <= average <= 100:
            grade = 'O'
        elif 80 <= average < 90:
            grade = 'E'
        elif 70 <= average < 80:
            grade = 'A'
        elif 55 <= average < 70:
            grade = 'P'
        elif 40 <= average < 55:
            grade = 'D'
        else:
            grade = 'T'

        return grade


if __name__ == '__main__':
    line = input().split()
    person_first_name = line[0]
    person_last_name = line[1]
    id_num = line[2]

    num_scores = int(input())   # not needed for Python
    student_scores = list(map(int, input().split()))

    s = Student(person_first_name, person_last_name, id_num, student_scores)
    s.print_person()
    print("Grade:", s.calculate(student_scores))
