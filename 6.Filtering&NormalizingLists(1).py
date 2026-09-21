raw_records = [
    {"id": "P01", "name": " Alice",  "sbp": 142, "dbp": 92,  "smoker": " YES ", "cholesterol": 240},
    {"id": "P02", "name": "Bob",     "sbp": 118, "dbp": 76,  "smoker": "no",    "cholesterol": 185},
    {"id": "P03", "name": " Charlie","sbp": 160, "dbp": 100, "smoker": "yes ",  "cholesterol": 265},
    {"id": "P04", "name": "Diana ",  "sbp": 122, "dbp": 80,  "smoker": " NO",   "cholesterol": 195},
    {"id": "P05", "name": "Evan",    "sbp": 135, "dbp": 88,  "smoker": "yes",   "cholesterol": 210},
    {"id": "P06", "name": "Fiona",   "sbp": 110, "dbp": 72,  "smoker": "no",    "cholesterol": 160}]

keyslist = [entry["id"] for entry in raw_records]

nameslist = [entry["name"].strip().lower() for entry in raw_records]

map_list = [round((entry["sbp"] + 2*entry["dbp"])/3, 2) for entry in raw_records]

smoker_list = [entry["smoker"].strip().lower() == "yes" for entry in raw_records]

cholesterol_list = [entry["cholesterol"] for entry in raw_records]

rectified_records = {}
i = 0
while(i < len(keyslist)):
    rectified_records[keyslist[i]] = {"name": nameslist[i], "map": map_list[i], "smoker": smoker_list[i], "cholesterol": cholesterol_list[i]}
    i += 1

high_risk_patients = [value['name'] for value in rectified_records.values() if(value['smoker'] and ((value['map'] >= 105.0) or (value['cholesterol'] >= 220)))]

ranked_priority_log = []
i = 1
for name in high_risk_patients:
    for value in rectified_records.values():
        if(name == value['name']):
            ranked_priority_log.append(f"Rank {i}: {name.capitalize()} (MAP: {value['map']})")
            break
    i += 1

print(ranked_priority_log)
