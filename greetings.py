class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = None

    def welcome(self):
        return f"Welcome to Albert School, {self.first_name}!"

    def register(self, registry):
        self.student_id = len(registry) + 1
        registry.append(self)
        return self.student_id


if __name__ == "__main__":
    registry = []
    student = Student("Tuka", "Bade")
    student.register(registry)
    print(student.welcome())
    print(f"Registered as student #{student.student_id}")
