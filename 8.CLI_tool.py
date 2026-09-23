import json
data = []
while(1>0):
    print("=== CLINIC REGISTRY SYSTEM ===")
    print("1. Add New Patient")
    print("2. Search Patient by ID")
    print("3. Display All Patients & Flag High-Risk")
    print("4. Save & Exit")

    Command = input("Choose an option (1-4): ")
    if(Command == "1"):
        patient_data = {}
        patient_data["id"] = input("Enter Patient ID: ")
        patient_data["name"] = input("Enter Name: ")
        try:
            patient_data["age"] = int(input("Enter Age: "))
        except ValueError:
            patient_data["age"] = "-"
            print("Invalid entry.")
        try:
            patient_data["systolic_bp"] = int(input("Enter Systolic BP: "))
        except ValueError:
            patient_data["systolic_bp"] = "-"
            print("Invalid entry.")
        try:
            patient_data["diastolic_bp"] = int(input("Enter Diastolic BP: "))
        except ValueError:
            patient_data["diastolic_bp"] = "-"
            print("Invalid entry.")
        try:
            patient_data["weight_kg"] = float(input("Enter Weight (kg): "))
        except ValueError:
            patient_data["weight_kg"] = "-"
            print("Invalid entry.")
        try:
            patient_data["height_m"] = float(input("Enter Height (m): "))
        except ValueError:
            patient_data["height_m"] = "-"
            print("Invalid entry.")
        if((patient_data["weight_kg"] == "-") or (patient_data["height_m"] == "-")):
            patient_data["bmi"] = "-"
        else:
            patient_data["bmi"] = round(patient_data["weight_kg"]/(patient_data["height_m"]**2), 2)
        data.append(patient_data)
        with open("patients_database.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"Patient {patient_data["id"]} successfully registered!")
    elif(Command == "2"):
        requested_id = input("Enter Patient ID to search: ")
        with open("patients_database.json", "r") as file:
            reader = json.load(file)
            for patient in reader:
                if(patient["id"] == requested_id):
                    print(f"ID: {patient["id"]} | Name: {patient["name"]} | Age: {patient["age"]} | BP: {patient["systolic_bp"]}/{patient["diastolic_bp"]} | BMI: {patient["bmi"]}")
                    break
                else:
                    print("Patient not found.")
    elif(Command == "3"):
        print("--- PATIENT REGISTRY ---")
        with open("patients_database.json", "r") as file:
            reader = json.load(file)
            for patient in reader:
                    risk = ""
                    if((patient["systolic_bp"] == "-") or (patient["bmi"] == "-")):
                        risk = "-"
                    elif((patient["systolic_bp"] >= 140) or (patient["bmi"] >= 30.0)):
                        risk = "[HIGH RISK]"
                    else:
                        risk = "[NORMAL]"
                    print(f"- {patient["id"]}: {patient["name"]} | BP: {patient["systolic_bp"]}/{patient["diastolic_bp"]} | BMI: {patient["bmi"]} -> {risk}")
    elif(Command == "4"):
        print("Data saved to 'patients_database.json'. Exiting program.")
        break


