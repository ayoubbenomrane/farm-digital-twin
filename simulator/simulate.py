import requests
import random
import time

ORION_URL = "http://localhost:1026/v2/entities"
parcels = ["A1", "A2", "A3", "B1", "B2", "B3"]
crop_types = ["Wheat", "Corn", "Tomato"]

# Create entities initially
for p in parcels:
    payload = {
        "id": f"Parcel:{p}",
        "type": "Parcel",
        "humidity": {"type": "Number", "value": random.uniform(30, 70)},
        "pH": {"type": "Number", "value": random.uniform(5.5, 7.5)},
        "cropType": {"type": "Text", "value": random.choice(crop_types)},
        "plantGrowth": {"type": "Number", "value": random.randint(0, 10)}
    }
    requests.post(ORION_URL, json=payload, headers={"Content-Type": "application/json"})

# Simulate updates every hour (or faster for demo)
while True:
    for p in parcels:
        update = {
            "humidity": {"value": round(random.uniform(30, 80), 1)},
            "pH": {"value": round(random.uniform(5.5, 7.5), 1)},
            "plantGrowth": {"value": random.randint(10, 100)}
        }
        url = f"{ORION_URL}/Parcel:{p}/attrs"
        res = requests.patch(url, json=update, headers={"Content-Type": "application/json"})
        print(f"Updated Parcel {p}: {res.status_code}")
    time.sleep(3600)  # every hour — change to time.sleep(5) for fast testing
