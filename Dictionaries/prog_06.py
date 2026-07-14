'''
This program stores employee information in a nested dictionary, 
calculates average performance, and finds the best employee.
'''
from typing import Dict, List
EmployeeRecord = Dict[str, object]
def calculate_average(scores: List[int]) -> float:
    if not scores:
        return 0.0

    return sum(scores) / len(scores)


def generate_performance_report(
    employees: Dict[int, EmployeeRecord]
) -> None:

    if not employees:
        print("No employee records are available.")
        return

    top_employee_name = ""
    highest_average = -1.0

    print("\nEMPLOYEE PERFORMANCE REPORT")
    print("-" * 60)

    for employee_id, employee in employees.items():
        scores = employee["performance_scores"]
        average = calculate_average(scores)

        if average >= 85:
            rating = "Excellent"
        elif average >= 70:
            rating = "Good"
        elif average >= 50:
            rating = "Satisfactory"
        else:
            rating = "Needs Improvement"

        print(f"Employee ID : {employee_id}")
        print(f"Name        : {employee['name']}")
        print(f"Department  : {employee['department']}")
        print(f"Average     : {average:.2f}")
        print(f"Rating      : {rating}")
        print("-" * 60)

        if average > highest_average:
            highest_average = average
            top_employee_name = str(employee["name"])

    print(
        f"\nTop Performer: {top_employee_name} "
        f"with an average score of {highest_average:.2f}"
    )


employees = {
    101: {
        "name": "Ali Khan",
        "department": "Software Development",
        "performance_scores": [88, 92, 85, 90]
    },
    102: {
        "name": "Sara Ahmed",
        "department": "Data Analytics",
        "performance_scores": [91, 95, 89, 93]
    },
    103: {
        "name": "Usman Tariq",
        "department": "Cybersecurity",
        "performance_scores": [75, 80, 72, 78]
    },
    104: {
        "name": "Hina Malik",
        "department": "Quality Assurance",
        "performance_scores": [65, 70, 68, 72]
    }
}


generate_performance_report(employees)