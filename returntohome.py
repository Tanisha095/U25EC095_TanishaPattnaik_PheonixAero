drone_state = {
    "battery": 18,
    "altitude": 95,
    "signal_strength": 40,  # percent
    "distance_from_home": 850,  # metres
    "wind_speed": 38,  # km/h
    "obstacle_detected": True
}
triggered = False  # to track if any condition is triggered

# Low Battery
if drone_state["battery"] < 20:
    print("CRITICAL: RTH triggered — Low Battery")
    triggered = True

# Signal Strength
if drone_state["signal_strength"] < 30:
    print("WARNING: RTH triggered — Signal Lost")
    triggered = True

# High Wind
if drone_state["wind_speed"] > 35:
    print("WARNING: RTH triggered — High Wind")
    triggered = True

# Obstacle Detection
if drone_state["obstacle_detected"] is True:
    print("CAUTION: Obstacle detected — Rerouting")
    triggered = True

# If none triggered
if not triggered:
    print("All systems nominal")

#2.while loop simulating descent & drain battery by 1% per 15m
altitude = drone_state["altitude"]
battery = drone_state["battery"]
while altitude > 0:
    descent = min(15, altitude)  # descend by 15m 
    altitude -= descent
    battery -= 1   # drain battery    
    print(f"Altitude: {altitude} m | Battery: {battery}%")