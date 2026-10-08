import sys
from pathlib import Path

from greetings.roster import process_roster
from greetings.student import Student


def demo() -> None:
    registry: list[Student] = []
    student = Student("Othmane", "Eddaqqaq", "oedaqqaq@albertschool.com")
    student.register(registry)
    print(student.welcome())
    print(f"Registered as student #{student.student_id} of {len(registry)}")
    print(f"Confirmation sent to {student.email}")
    print(student.enroll("MSc 1 Data"))
    print(student.farewell())


def main(argv: list[str] | None = None) -> None:
    args = sys.argv[1:] if argv is None else argv
    if len(args) == 2 and args[0] == "roster":
        process_roster(Path(args[1]))
    else:
        demo()
