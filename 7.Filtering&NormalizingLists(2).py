raw_records = [
    {"id": "P01", "name": " Alice",  "sbp": 142, "dbp": 92,  "smoker": " YES ", "cholesterol": 240},
    {"id": "P02", "name": "Bob",     "sbp": 118, "dbp": 76,  "smoker": "no",    "cholesterol": 185},
    {"id": "P03", "name": " Charlie","sbp": 160, "dbp": 100, "smoker": "yes ",  "cholesterol": 265},
    {"id": "P04", "name": "Diana ",  "sbp": 122, "dbp": 80,  "smoker": " NO",   "cholesterol": 195},
    {"id": "P05", "name": "Evan",    "sbp": 135, "dbp": 88,  "smoker": "yes",   "cholesterol": 210},
    {"id": "P06", "name": "Fiona",   "sbp": 110, "dbp": 72,  "smoker": "no",    "cholesterol": 160}]

rectified_records = {entry["id"]: {"name": entry["name"].strip(), "map": round((entry["sbp"] + 2*entry["dbp"])/3, 2), "smoker": entry["smoker"].strip().lower() == "yes", "cholesterol": entry["cholesterol"]} for entry in raw_records}

high_risk_patients = [entry["name"] for entry in rectified_records.values() if(entry["smoker"] and ((entry["map"] >= 105.0) or (entry["cholesterol"] >= 220)))]

map_hrp = [entry["map"] for name in high_risk_patients for entry in rectified_records.values() if(entry["name"] == name)]
paired = list(zip(high_risk_patients, map_hrp))
ranked = list(enumerate(paired, start=1))
print([f"Rank {entry[0]}: {entry[1][0]} (MAP: {entry[1][1]})" for entry in ranked])
