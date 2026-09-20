def BMI (weight, height):
    return round(weight/(height**2)*10000, 2)

def BMR (sex, weight, height, age):
    if(sex == "male"):
        return round((10*weight) + (6.25*height) - (5*age) + 5, 2)
    elif(sex == "female"):
        return round((10*weight) + (6.25*height) - (5*age) - 161, 2)

def GFR (sex, age, Serum_creatinine):
    if(sex == "male"):
            k = 0.9
            a = -0.302
            return round(142 * min(Serum_creatinine/k, 1)**a * max(Serum_creatinine/k, 1)**-1.2 * 0.9938**age, 2)
    elif(sex == "female"):
            k = 0.7
            a = -0.241
            return round(142 * min(Serum_creatinine/k, 1)**a * max(Serum_creatinine/k, 1)**-1.2 * 0.9938**age * 1.012, 2)

patient_1 = {
     "patient_id": "PT-10492",
     "age": 54,
     "sex": "female",
     "weight_kg": 68.8,
     "height_cm": 162.5,
     "serum_creatinine_mg_dl": 1.15
}

print("For Patient_ID: ", patient_1["patient_id"])
print("BMI: ", BMI(patient_1["weight_kg"], patient_1["height_cm"]))
print("BMR: ", BMR(patient_1["sex"], patient_1["weight_kg"], patient_1["height_cm"], patient_1["age"]))
print("eGFR: ", GFR(patient_1["sex"], patient_1["age"], patient_1["serum_creatinine_mg_dl"]))