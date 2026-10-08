from greetings.student import Student


def main() -> None:
    registry: list[Student] = []
    student = Student("Othmane", "Eddaqqaq", "oedaqqaq@albertschool.com")
    student.register(registry)
    print(student.welcome())
    print(f"Registered as student #{student.student_id} of {len(registry)}")
    print(f"Confirmation sent to {student.email}")
    print(student.enroll("MSc 1 Data"))
    print(student.farewell())
