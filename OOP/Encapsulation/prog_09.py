#This program protects medical details and allows controlled access.
class Patient:
    def __init__(
        self,
        patient_id: str,
        name: str,
        age: int
    ):
        if age <= 0:
            raise ValueError(
                "Patient age must be greater than zero."
            )

        self.__patient_id = patient_id
        self.__name = name
        self.__age = age
        self.__medical_history = []
        self.__current_medications = []

    @property
    def patient_id(self) -> str:
        return self.__patient_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    def add_medical_record(
        self,
        diagnosis: str,
        doctor: str,
        date: str
    ) -> None:

        if not diagnosis.strip():
            raise ValueError("Diagnosis cannot be empty.")

        self.__medical_history.append({
            "diagnosis": diagnosis.strip(),
            "doctor": doctor.strip(),
            "date": date
        })

    def prescribe_medication(
        self,
        medicine_name: str,
        dosage: str
    ) -> None:

        if not medicine_name.strip():
            raise ValueError(
                "Medicine name cannot be empty."
            )

        self.__current_medications.append({
            "medicine": medicine_name.strip(),
            "dosage": dosage.strip()
        })

    def remove_medication(
        self,
        medicine_name: str
    ) -> None:

        for medication in self.__current_medications:
            if medication["medicine"].lower() == medicine_name.lower():
                self.__current_medications.remove(medication)
                return

        raise KeyError("Medication not found.")

    def get_medical_summary(
        self,
        access_role: str
    ) -> dict:

        authorized_roles = {
            "doctor",
            "nurse",
            "administrator"
        }

        if access_role.lower() not in authorized_roles:
            raise PermissionError(
                "You are not authorized to view medical records."
            )

        return {
            "patient_id": self.__patient_id,
            "name": self.__name,
            "age": self.__age,
            "medical_history": self.__medical_history.copy(),
            "medications": self.__current_medications.copy()
        }


try:
    patient = Patient(
        "PAT-1001",
        "Ali Khan",
        32
    )

    patient.add_medical_record(
        "Seasonal allergy",
        "Dr. Ahmed",
        "2026-07-10"
    )

    patient.prescribe_medication(
        "Antihistamine",
        "One tablet daily"
    )

    summary = patient.get_medical_summary("doctor")

    print("\nPATIENT MEDICAL SUMMARY")
    print("=" * 60)
    print(f"Patient ID : {summary['patient_id']}")
    print(f"Name       : {summary['name']}")
    print(f"Age        : {summary['age']}")

    print("\nMedical History")

    for record in summary["medical_history"]:
        print(
            f"{record['date']} | "
            f"{record['diagnosis']} | "
            f"{record['doctor