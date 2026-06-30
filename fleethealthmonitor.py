fleet = {
"PX4_001": {"battery": 87, "altitude": 120, "status": "active", "payload_kg": 1.2},
"PX4_002": {"battery": 23, "altitude": 0, "status": "grounded", "payload_kg": 0},
"PX4_003": {"battery": 56, "altitude": 85, "status": "active", "payload_kg": 0.8},
"PX4_004": {"battery": 11, "altitude": 30, "status": "returning", "payload_kg": 0.5},
}
# 1. Add "PX4_005" with battery=95, altitude=0, status="standby", payload_kg=0
fleet["PX4_005"] = {"battery": 95, "altitude": 0, "status": "standby", "payload_kg": 0}

# 2.Removes "PX4_002" using .pop() and print it
data=fleet.pop("PX4_002")
print("removed item is: ", data)

#3. Prints all active drones and their battery levels
for i in fleet:
    print(f"{i} : battery= {fleet[i]['battery']}")

# 4. Find drone with lowest battery among drones in air (altitude > 0)
min_battery = float('inf')
low_batt_drone = None
for drone_id, data in fleet.items():
    if data["altitude"] > 0:  # drone is in air
        if data["battery"] < min_battery:
            min_battery = data["battery"]
            low_batt_drone = drone_id
print("Lowest battery drone in air:", low_batt_drone, "| Battery:", min_battery)

# 5. Update drones with battery < 30
for data in fleet.values():
    if data["battery"] < 30:
        data["status"] = "critical_low_battery"

# 6. Final formatted fleet summary
for drone_id, data in fleet.items():
    print(f"[{drone_id}] Alt: {data['altitude']}m | Batt: {data['battery']}% | Status: {data['status']} | Payload: {data['payload_kg']}kg")
