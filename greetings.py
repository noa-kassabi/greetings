class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def welcome(self):
        return f"Welcome to Albert School, {self.first_name}!"


if __name__ == "__main__":
    student = Student("Tuka", "Bade")
    print(student.welcome())
