#3. Detect Conflicting Appointments
def find_appointment_conflicts(
    appointments: list[tuple[str, str, int, int]]
) -> list[
    tuple[
        tuple[str, str, int, int],
        tuple[str, str, int, int]
    ]
]:
    """
    Find appointments that overlap with each other.
    """

    sorted_appointments = sorted(
        appointments,
        key=lambda appointment: appointment[2]
    )

    conflicts = []

    for first_index in range(len(sorted_appointments)):
        first_appointment = sorted_appointments[first_index]

        for second_index in range(
            first_index + 1,
            len(sorted_appointments)
        ):
            second_appointment = sorted_appointments[second_index]

            first_start = first_appointment[2]
            first_end = first_appointment[3]

            second_start = second_appointment[2]
            second_end = second_appointment[3]

            if second_start >= first_end:
                break

            if first_start < second_end and second_start < first_end:
                conflicts.append(
                    (
                        first_appointment,
                        second_appointment
                    )
                )

    return conflicts


appointments = [
    ("APT-101", "Ali Khan", 9, 10),
    ("APT-102", "Sara Ahmed", 9, 11),
    ("APT-103", "Hamza Ali", 11, 12),
    ("APT-104", "Ayesha Noor", 11, 13),
    ("APT-105", "Usman Tariq", 14, 15)
]

conflicts = find_appointment_conflicts(appointments)

print("APPOINTMENT CONFLICT REPORT")
print("=" * 70)

if not conflicts:
    print("No appointment conflicts found.")
else:
    for first, second in conflicts:
        print(
            f"{first[0]} ({first[1]}) conflicts with "
            f"{second[0]} ({second[1]})"
        )