class Student:
    def __init__(self, id, name, course):
        self.id = str(id)
        self.name = str(name)
        self.course = str(course)
        self.mark = 0

    def __str__(self):
        return f"ID:{self.id}, Name:{self.name}, Course:{self.course}, Mark:{self.mark}"

    def set_mark(self, new_mark):
        try:
            if 0 <= int(new_mark) <= 100:
                self.mark = new_mark
                return True
            else:
                return False

        except ValueError:
            return False

    def get_mark(self):
        mark = ""
        if 100 >= self.mark >= 70:
            mark = "First"
        elif 70 > self.mark >= 60:
            mark = "2/1"
        elif 60 > self.mark >= 50:
            mark = "2/2"
        elif 50 > self.mark >= 40:
            mark = "Third"
        else:
            mark = "Fail"

        return mark


student1 = Student(1, "Jeff", "Com411")

print(student1.set_mark(60))

print(student1)
print(student1.get_mark())
