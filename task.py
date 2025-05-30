class student:
    def __init__(self, name, school):
        self.name = name
        self.school = school

    def average(self, marks):
        average = sum(marks)/len(marks)
        return average


class working(student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def info(self):
        print(f'Name:{self.name} \nSchool:{self.school} \nSalary:{self.salary}')


marks = [95, 99, 98]
std = student('Alice', 'Borderland High')
avg = std.average(marks)
print('Average Marks:',avg)

wrk = working('Bob', 'Sunrise School', 200000)
wrk.info()