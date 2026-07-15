#Marks are protected and can only be added after validation.
class Student:
    def __init__(
        self,
        roll_number: str,
        name: str,
        department: str
    ):
        self.__roll_number = roll_number
        self.__name = name
        self.__department = department
        self.__marks = {}

    @property
    def roll_number(self) -> str:
        return self.__roll_number

    @property
    def name(self) -> str:
        return self.__name

    @property
    def department(self) -> str:
        return self.__department

    def add_or_update_marks(
        self,
        subject: str,
        marks: float
    ) -> None:

        subject = subject.strip()

        if not subject:
            raise ValueError("Subject name cannot be empty.")

        if not 0 <= marks <= 100:
            raise ValueError(
                "Marks must be between 0 and 100."
            )

        self.__marks[subject] = marks

    def remove_subject(self, subject: str) -> None:
        if subject not in self.__marks:
            raise KeyError(
                f"{subject} does not exist in the record."
            )

        del self.__marks[subject]

    def get_marks(self) -> dict:
        return self.__marks.copy()

    def calculate_average(self) -> float:
        if not self.__marks:
            return 0.0

        return sum(self.__marks.values()) / len(self.__marks)

    def calculate_grade(self) -> str:
        average = self.calculate_average()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"

        return "F"

    def display_result(self) -> None:
        print("\nSTUDENT RESULT")
        print("=" * 55)
        print(f"Roll Number : {self.__roll_number}")
        print(f"Name        : {self.__name}")
        print(f"Department  : {self.__department}")

        print("\nSubject Marks")

        for subject, marks in self.__marks.items():
            print(f"{subject:<25}: {marks}")

        print("-" * 55)
        print(f"Average     : {self.calculate_average():.2f}")
        print(f"Grade       : {self.calculate_grade()}")


try:
    student = Student(
        "23SW001",
        "Abdul Majid",
        "Software Engineering"
    )

    student.add_or_update_marks("Python Programming", 91)
    student.add_or_update_marks("Database Systems", 88)
    student.add_or_update_marks("Data Structures", 86)
    student.add_or_update_marks("Software Design", 90)

    student.display_result()

except (ValueError, KeyError) as error:
    print(f"Student record error: {error}")