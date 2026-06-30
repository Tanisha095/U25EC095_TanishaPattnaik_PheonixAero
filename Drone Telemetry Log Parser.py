telemetry = "DRONE_ID:PX4_001|ALT:120.5m|SPEED:18.3kmph|BATT:67%|STATUS:HOVERING|GPS:23.0225N,72.5714E"

#1. Extracts Drone ID, Altitude (float), Speed (float), Battery (int), and GPS coordinates
data_list=telemetry.split("|") # converts the | separated values into a list 
data={}  # empty dictionary to store key value pairs
for item in data_list:
    key, value = item.split(":")
    data[key]=value  #stores the telemetry info in a dictionary

droneID=data["DRONE_ID"]
Altitude=float(data["ALT"].replace("m",""))
Speed=float(data["SPEED"].replace("kmph",""))
Battery=int(data["BATT"].replace("%",""))
status=data["STATUS"]
GPS_coordinates=data["GPS"]
     
#2. Checks if status contains "HOVER" (case-insensitive) — print True/False
if (data["STATUS"]=="HOVERING"): 
    print(True)
else:
    print (False)    

#3. Replaces "HOVERING" with "RETURNING_HOME"  
if (data["STATUS"]=="HOVERING"):
    data["STATUS"]="RETURNING_HOME"


# 4. Prints a formatted summary using f-strings: [PX4_001] Alt: 120.5m | Batt: 67% | Coords: 23.0225N, 72.5714E'''
print(f"[{droneID}] Alt: {Altitude}m | Batt: {Battery}% | Coords: {GPS_coordinates}")